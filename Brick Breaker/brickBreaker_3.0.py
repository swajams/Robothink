import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 4
BALL_SPEED_Y = -4

# Power-up settings
POWERUP_SIZE = 20
POWERUP_TYPES = ["extra_life", "extra_ball"]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker 3.0")

# Font setup
font = pygame.font.SysFont("arial", 30)

def show_game_over():
    screen.fill(BLACK)
    game_over_text = font.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    exit()

# Function to generate bricks
def generate_bricks(rows, cols):
    bricks = []
    brick_width = WIDTH // cols
    brick_height = 20
    for row in range(rows):
        for col in range(cols):
            brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width -5, brick_height-5)
            bricks.append(brick)
    return bricks

# Game variables
level = 1
score = 0
lives = 5

while level <= 5:
    # Increase difficulty
    BRICK_ROWS = 3 + level
    BRICK_COLS = 6 + level // 2
    bricks = generate_bricks(BRICK_ROWS, BRICK_COLS)
    
    # Paddle and ball setup
    paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
    balls = [pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)]
    ball_speeds = [(BALL_SPEED_X, BALL_SPEED_Y)]
    powerups = []
    running = True
    
    while running:
        screen.fill(BLACK)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += PADDLE_SPEED
        
        # Move balls
        for i in range(len(balls)):
            balls[i].x += ball_speeds[i][0]
            balls[i].y += ball_speeds[i][1]
        
        # Ball collision with walls and paddle
        for i in range(len(balls)):
            if balls[i].left <= 0 or balls[i].right >= WIDTH:
                ball_speeds[i] = (-ball_speeds[i][0], ball_speeds[i][1])
            if balls[i].top <= 0 :
                ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])
            if balls[i].colliderect(paddle):
                ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])
        
        # Ball collision with bricks
        for ball in balls:
            for brick in bricks[:]:
                if ball.colliderect(brick):
                    bricks.remove(brick)
                    index = balls.index(ball)
                    ball_speeds[index] = (ball_speeds[index][0], -ball_speeds[index][1])
                    score += 10
                    
                    # Randomly spawn a power-up
                    if random.random() < 0.3:
                        brick_width = WIDTH // BRICK_COLS  # Calculate brick width based on current level
                        powerup = {
                            "rect": pygame.Rect(brick.x + brick_width // 4, brick.y, POWERUP_SIZE, POWERUP_SIZE),
                            "type": random.choice(POWERUP_TYPES),
                            "color": "yellow"
                        }
                        powerups.append(powerup)
                    break
        
        # Move power-ups
        for powerup in powerups[:]:
            powerup["rect"].y += 2
            if powerup["rect"].colliderect(paddle):
                if powerup["type"] == "extra_life":
                    lives += 1
                elif powerup["type"] == "extra_ball":
                    new_ball = pygame.Rect(paddle.x + PADDLE_WIDTH // 2, paddle.y - BALL_SIZE, BALL_SIZE, BALL_SIZE)
                    balls.append(new_ball)
                    ball_speeds.append((random.choice([-4, 4]), -4))
               
                powerups.remove(powerup)
            elif powerup["rect"].y > HEIGHT:
                powerups.remove(powerup)
        
        # Check for win condition
        if not bricks:
            screen.fill(BLACK)
            win_text = font.render(f"Level {level} Complete!", True, GREEN)
            screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            level += 1
            break
        
        # Game over condition
        for ball in balls[:]:
            if ball.bottom >= HEIGHT:
                index = balls.index(ball)
                balls.pop(index)
                ball_speeds.pop(index)
                if not balls:
                    lives -= 1
                    if lives <= 0:
                        show_game_over()
                    else:
                        balls.append(pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE))
                        ball_speeds.append((BALL_SPEED_X, BALL_SPEED_Y))
        
        # Draw elements
        pygame.draw.rect(screen, WHITE, paddle)
        for ball in balls:
            pygame.draw.ellipse(screen, RED, ball)
        for brick in bricks:
            pygame.draw.rect(screen, BLUE, brick)
        for powerup in powerups:
            pygame.draw.ellipse(screen, YELLOW, powerup["rect"])
   
        
        # Display score and lives
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))
        screen.blit(level_text, (WIDTH // 2 - 50, 10))
        
        pygame.display.flip()
        pygame.time.delay(16)  # Limit frame rate

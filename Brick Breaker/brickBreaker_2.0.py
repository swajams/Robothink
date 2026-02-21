import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

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
PADDLE_SPEED = 7

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 4
BALL_SPEED_Y = -4

# Brick settings
BRICK_ROWS = 4
BRICK_COLS = 6
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 20

# Power-up settings
POWERUP_SIZE = 20
POWERUP_TYPES = ["extra_life", "extra_ball"]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker V2")

# Paddle setup
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
balls = [pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)]
ball_speeds = [(BALL_SPEED_X, BALL_SPEED_Y)]

# Brick setup
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH - 5, BRICK_HEIGHT - 5)
        bricks.append(brick)

# Power-ups
powerups = []

# Game variables
score = 0
lives = 5
font = pygame.font.SysFont("comicsansms", 30)

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
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
        if balls[i].top <= 0:
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
                    powerup = {
                        "rect": pygame.Rect(brick.x + BRICK_WIDTH // 4, brick.y, POWERUP_SIZE, POWERUP_SIZE),
                        "type": random.choice(POWERUP_TYPES)
                    }
                    powerups.append(powerup)
                break
    
    # Move power-ups
    for powerup in powerups[:]:
        powerup["rect"].y += 3
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
        win_text = font.render("You Win!", True, GREEN)
        screen.blit(win_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
    
    # Game over condition
    for ball in balls[:]:
        if ball.bottom >= HEIGHT:
            index = balls.index(ball)
            balls.pop(index)
            ball_speeds.pop(index)
            if not balls:
                lives -= 1
                if lives <= 0:
                    running = False
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
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))
    
    pygame.display.flip()
    pygame.time.delay(16)  # Limit frame rate

pygame.quit()

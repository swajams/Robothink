import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 900
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 4
BALL_SPEED_Y = -4

# Brick settings
BRICK_ROWS = 4
BRICK_COLS = 8
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Paddle setup
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

# Brick setup
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH-5, BRICK_HEIGHT-5 )
        bricks.append(brick)

# Score
score = 0
font = pygame.font.SysFont("magneto", 30)

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
    
    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy
    
    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1
    
    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_dy *= -1
    
    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            score += 10
            break
    
    # Game over condition
    if ball.bottom >= HEIGHT:
        running = False
    
    # Draw elements
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    pygame.time.delay(16)  # Limit frame rate

pygame.quit()

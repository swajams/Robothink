import pygame
import random

# Initialize
pygame.init()

# Constants
TILE_SIZE = 30
MAP_WIDTH = 20
MAP_HEIGHT = 15
WIDTH = MAP_WIDTH * TILE_SIZE
HEIGHT = MAP_HEIGHT * TILE_SIZE
FPS = 60
MOVE_DELAY = 80  # milliseconds between player moves
ENEMY_DELAY = 300  # milliseconds between enemy moves

# Colors
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Map (W = Wall, . = Floor, P = Player, E = Enemy, L = Loot)
dungeon_map = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W......E......W...EW",
    "W.WW..WW.WWWW.W.WW.W",
    "W.W....W.W...E..WL.W",
    "W.W.WW.W.W.WWWW.WW.W",
    "W.W.W..W.WLW...E...W",
    "W.W.WW.W.W.WW.W.WWWW",
    "W.....W.L.W....W.L.W",
    "WWW.W.WWWWWWWWW...WW",
    "WL..W.......E....W.W",
    "WWWWWWWWWWWWWWWW..WW",
    "W...............E..W",
    "W.WWWWWWWWWWWWWWWW.W",
    "W.E...............PW",
    "WWWWWWWWWWWWWWWWWWWW",
]

# Load images
tile_floor = pygame.Surface((TILE_SIZE, TILE_SIZE))
tile_floor.fill(GRAY)
tile_wall = pygame.Surface((TILE_SIZE, TILE_SIZE))
tile_wall.fill(BLACK)
player_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_img.fill(GREEN)
enemy_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
enemy_img.fill(RED)
loot_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
loot_img.fill(YELLOW)

# Find player start position
player_pos = [0, 0]
loot_positions = []
enemy_positions = []

for y, row in enumerate(dungeon_map):
    for x, tile in enumerate(row):
        if tile == "P":
            player_pos = [x, y]
        elif tile == "L":
            loot_positions.append([x, y])
        elif tile == "E":
            enemy_positions.append([x, y, 1])  # x, y, direction

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Bit Pac-Man")
clock = pygame.time.Clock()

score = 0
last_move_time = pygame.time.get_ticks()
last_enemy_move = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 48)

def draw_win_screen():
    screen.fill(BLACK)
    win_text = font.render("You Win!", True, GREEN)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(win_text, ((WIDTH - win_text.get_width()) // 2, HEIGHT // 2 - 30))
    screen.blit(score_text, ((WIDTH - score_text.get_width()) // 2, HEIGHT // 2 + 30))
    pygame.display.flip()
    pygame.time.wait(3000)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input (with delay)
    dx, dy = 0, 0
    if current_time - last_move_time > MOVE_DELAY:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: dx = -1
        elif keys[pygame.K_RIGHT]: dx = 1
        elif keys[pygame.K_UP]: dy = -1
        elif keys[pygame.K_DOWN]: dy = 1

        new_x = player_pos[0] + dx
        new_y = player_pos[1] + dy
        if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
            if dungeon_map[new_y][new_x] != "W":
                player_pos = [new_x, new_y]
                last_move_time = current_time

    # Enemy movement (with delay)
    if current_time - last_enemy_move > ENEMY_DELAY:
        for enemy in enemy_positions:
            ex, ey, direction = enemy
            new_ex = ex + direction
            if 0 <= new_ex < MAP_WIDTH and dungeon_map[ey][new_ex] != "W":
                enemy[0] = new_ex
            else:
                enemy[2] *= -1  # Change direction
        last_enemy_move = current_time

    # Check for collision with enemy
    for ex, ey, _ in enemy_positions:
        if player_pos == [ex, ey]:
            print("You were caught by an enemy!")
            running = False

    # Check for loot
    for loot in loot_positions[:]:
        if player_pos == loot:
            loot_positions.remove(loot)
            score += 1
            print(f"Loot collected! Score: {score}")
            if score >= 5:
                draw_win_screen()
                running = False

    # Draw map
    for y, row in enumerate(dungeon_map):
        for x, tile in enumerate(row):
            if tile == "W":
                screen.blit(tile_wall, (x * TILE_SIZE, y * TILE_SIZE))
            else:
                screen.blit(tile_floor, (x * TILE_SIZE, y * TILE_SIZE))

    # Draw loot
    for x, y in loot_positions:
        screen.blit(loot_img, (x * TILE_SIZE, y * TILE_SIZE))

    # Draw enemies
    for x, y, _ in enemy_positions:
        screen.blit(enemy_img, (x * TILE_SIZE, y * TILE_SIZE))

    # Draw player
    screen.blit(player_img, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

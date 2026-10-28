
import pygame
import random
import math
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 11 - Image Transformations")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28, bold=True)
small_font = pygame.font.SysFont("arial", 19)

# Colors
GRASS = (67, 145, 75)
LIGHT_GRASS = (85, 160, 85)
DARK_GRASS = (50, 115, 60)
WHITE = (255, 255, 255)
GOLD = (255, 215, 75)
DARK = (30, 50, 38)

# Load images
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

original_player = pygame.image.load(
    str(IMAGE_DIR / "player.png")
).convert_alpha()

original_coin = pygame.image.load(
    str(IMAGE_DIR / "coin.png")
).convert_alpha()

# Resize images
original_player = pygame.transform.smoothscale(
    original_player, (55, 55)
)
original_coin = pygame.transform.smoothscale(
    original_coin, (40, 40)
)

# Player
player = pygame.Rect(100, 200, 55, 55)
player_image = original_player
facing_left = False
speed = 5

# Coin
coin = pygame.Rect(400, 300, 40, 40)
score = 0

# Grass decoration
random.seed(10)
grass_marks = [
    (random.randint(0, WIDTH), random.randint(85, HEIGHT))
    for _ in range(180)
]
random.seed()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
        facing_left = True

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
        facing_left = False

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

    player.clamp_ip(screen.get_rect())

    # Flip player to face the movement direction
    if facing_left:
        player_image = pygame.transform.flip(
            original_player, True, False
        )
    else:
        player_image = original_player

    # Rotate coin continuously
    angle = (pygame.time.get_ticks() * 0.15) % 360
    rotated_coin = pygame.transform.rotate(
        original_coin, angle
    )

    # Keep the rotating coin centered
    coin_draw_rect = rotated_coin.get_rect(
        center=coin.center
    )

    # Collect coin
    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(40, WIDTH - 50)
        coin.y = random.randint(100, HEIGHT - 50)

    # Background
    screen.fill(GRASS)

    for i, (gx, gy) in enumerate(grass_marks):
        color = LIGHT_GRASS if i % 2 == 0 else DARK_GRASS
        pygame.draw.line(
            screen, color, (gx, gy), (gx + 4, gy - 5), 2
        )

    # Sandy path
    pygame.draw.rect(
        screen, (160, 137, 99), (0, 350, WIDTH, 105)
    )
    pygame.draw.rect(
        screen, (205, 184, 137), (0, 355, WIDTH, 95)
    )

    # Score panel
    pygame.draw.rect(
        screen, DARK, (15, 12, 210, 55),
        border_radius=12
    )

    score_text = font.render(
        f"Coins: {score}", True, GOLD
    )
    screen.blit(score_text, (30, 20))

    help_text = small_font.render(
        "Move: Arrow keys or WASD", True, WHITE
    )
    screen.blit(help_text, (WIDTH - 285, 22))

    # Draw transformed images
    screen.blit(rotated_coin, coin_draw_rect)
    screen.blit(player_image, player.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

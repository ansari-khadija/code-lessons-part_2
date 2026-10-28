
import pygame
import random
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 9 - Display Text")

clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.SysFont("arial", 36, bold=True)
font = pygame.font.SysFont("arial", 26, bold=True)
small_font = pygame.font.SysFont("arial", 18)

# Colors
GRASS = (67, 145, 75)
DARK_GRASS = (50, 115, 60)
LIGHT_GRASS = (85, 160, 85)
WHITE = (255, 255, 255)
GOLD = (255, 215, 75)
DARK = (30, 50, 38)
RED = (255, 90, 90)

# Load images
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

player_image = pygame.image.load(
    str(IMAGE_DIR / "player.png")
).convert_alpha()

coin_image = pygame.image.load(
    str(IMAGE_DIR / "coin.png")
).convert_alpha()

player_image = pygame.transform.smoothscale(
    player_image, (55, 55)
)
coin_image = pygame.transform.smoothscale(
    coin_image, (38, 38)
)

# Player
player = pygame.Rect(100, 200, 55, 55)
speed = 5

# Coin
coin = pygame.Rect(
    random.randint(40, WIDTH - 50),
    random.randint(100, HEIGHT - 50),
    38, 38
)

score = 0
game_over = False
running = True

random.seed(10)
grass_marks = [
    (random.randint(0, WIDTH), random.randint(85, HEIGHT))
    for _ in range(180)
]
random.seed()

while running:

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Restart game using R
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player.x, player.y = 100, 200
                coin.x = random.randint(40, WIDTH - 50)
                coin.y = random.randint(100, HEIGHT - 50)
                score = 0
                game_over = False

    # MOVEMENT
    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += speed

        player.clamp_ip(screen.get_rect())

        # COLLECT COIN
        if player.colliderect(coin):
            score += 1
            coin.x = random.randint(40, WIDTH - 50)
            coin.y = random.randint(100, HEIGHT - 50)

            if score >= 10:
                game_over = True

    # BACKGROUND
    screen.fill(GRASS)

    for i, (gx, gy) in enumerate(grass_marks):
        color = LIGHT_GRASS if i % 2 == 0 else DARK_GRASS
        pygame.draw.line(
            screen, color, (gx, gy), (gx + 4, gy - 5), 2
        )

    # PATH
    pygame.draw.rect(screen, (160, 137, 99), (0, 350, WIDTH, 105))
    pygame.draw.rect(screen, (205, 184, 137), (0, 355, WIDTH, 95))

    # SCORE PANEL
    pygame.draw.rect(
        screen, DARK, (15, 12, 250, 75), border_radius=14
    )

    # Display text using font.render()
    title = title_font.render("COIN COLLECTOR", True, WHITE)
    score_text = font.render(f"Score: {score}/10", True, GOLD)
    controls = small_font.render(
        "Move: Arrows or WASD", True, WHITE
    )

    screen.blit(title, (285, 18))
    screen.blit(score_text, (30, 20))
    screen.blit(controls, (30, 53))

    # DRAW IMAGES
    screen.blit(coin_image, coin.topleft)
    screen.blit(player_image, player.topleft)

    # GAME OVER MESSAGE
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 175))
        screen.blit(overlay, (0, 0))

        message = title_font.render("YOU WIN!", True, GOLD)
        restart = font.render("Press R to play again", True, WHITE)

        screen.blit(
            message,
            message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25))
        )
        screen.blit(
            restart,
            restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25))
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

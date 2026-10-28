
import pygame
import random
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 10 - Game Buttons")

clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.SysFont("arial", 44, bold=True)
font = pygame.font.SysFont("arial", 26, bold=True)
small_font = pygame.font.SysFont("arial", 19)

# Colors
GRASS = (67, 145, 75)
LIGHT_GRASS = (85, 160, 85)
DARK_GRASS = (50, 115, 60)
WHITE = (255, 255, 255)
GOLD = (255, 215, 75)
DARK = (30, 50, 38)
BLUE = (55, 130, 220)
BLUE_HOVER = (90, 170, 255)
RED = (200, 65, 65)
RED_HOVER = (245, 90, 90)

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

# Background decoration
random.seed(10)
grass_marks = [
    (random.randint(0, WIDTH), random.randint(80, HEIGHT))
    for _ in range(180)
]
random.seed()

# Game objects
player = pygame.Rect(100, 200, 55, 55)
coin = pygame.Rect(400, 300, 38, 38)

score = 0
game_state = "menu"
running = True


def draw_button(text, rect, mouse_pos, normal_color, hover_color):
    # Change color when mouse hovers over button
    color = hover_color if rect.collidepoint(mouse_pos) else normal_color

    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=12)

    label = font.render(text, True, WHITE)
    screen.blit(label, label.get_rect(center=rect.center))


def reset_game():
    global score, game_state

    score = 0
    player.x, player.y = 100, 200
    coin.x = random.randint(40, WIDTH - 50)
    coin.y = random.randint(100, HEIGHT - 50)
    game_state = "playing"


# Button positions
start_button = pygame.Rect(300, 250, 200, 60)
restart_button = pygame.Rect(300, 330, 200, 60)
exit_button = pygame.Rect(300, 410, 200, 60)

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if game_state == "menu":
                    if start_button.collidepoint(event.pos):
                        reset_game()

                    elif exit_button.collidepoint(event.pos):
                        running = False

                elif game_state == "game_over":
                    if restart_button.collidepoint(event.pos):
                        reset_game()

                    elif exit_button.collidepoint(event.pos):
                        running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r and game_state == "game_over":
                reset_game()

    # Update game
    if game_state == "playing":
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += 5

        player.clamp_ip(screen.get_rect())

        if player.colliderect(coin):
            score += 1
            coin.x = random.randint(40, WIDTH - 50)
            coin.y = random.randint(100, HEIGHT - 50)

            if score >= 10:
                game_state = "game_over"

    # Draw background
    screen.fill(GRASS)

    for i, (gx, gy) in enumerate(grass_marks):
        color = LIGHT_GRASS if i % 2 == 0 else DARK_GRASS
        pygame.draw.line(
            screen, color, (gx, gy), (gx + 4, gy - 5), 2
        )

    pygame.draw.rect(screen, (160, 137, 99), (0, 350, WIDTH, 105))
    pygame.draw.rect(screen, (205, 184, 137), (0, 355, WIDTH, 95))

    if game_state == "menu":
        # Start menu
        title = title_font.render("COIN COLLECTOR", True, WHITE)
        subtitle = small_font.render(
            "Collect 10 coins to win!", True, WHITE
        )

        screen.blit(
            title, title.get_rect(center=(WIDTH // 2, 150))
        )
        screen.blit(
            subtitle, subtitle.get_rect(center=(WIDTH // 2, 205))
        )

        draw_button(
            "START", start_button, mouse_pos, BLUE, BLUE_HOVER
        )
        draw_button(
            "EXIT", exit_button, mouse_pos, RED, RED_HOVER
        )

    elif game_state == "playing":
        screen.blit(player_image, player.topleft)
        screen.blit(coin_image, coin.topleft)

        score_text = font.render(
            f"Score: {score}/10", True, WHITE
        )
        screen.blit(score_text, (20, 20))

        help_text = small_font.render(
            "Move: Arrows / WASD     ESC: Quit", True, WHITE
        )
        screen.blit(help_text, (20, 55))

    elif game_state == "game_over":
        title = title_font.render("YOU WIN!", True, GOLD)
        screen.blit(
            title, title.get_rect(center=(WIDTH // 2, 210))
        )

        draw_button(
            "PLAY AGAIN", restart_button,
            mouse_pos, BLUE, BLUE_HOVER
        )
        draw_button(
            "EXIT", exit_button, mouse_pos, RED, RED_HOVER
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

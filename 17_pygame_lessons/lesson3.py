
import pygame
import random

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Coins!")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
BLUE = (25, 45, 90)
RED = (255, 80, 80)
YELLOW = (255, 220, 40)
WHITE = (255, 255, 255)
GREEN = (60, 220, 140)

# Player
player = pygame.Rect(100, 100, 40, 40)
speed = 5

# Coin
coin = pygame.Rect(
    random.randint(0, WIDTH - 24),
    random.randint(60, HEIGHT - 24),
    24, 24
)

score = 0
running = True

while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Move the player
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Keep the player inside the window
    player.clamp_ip(screen.get_rect())

    # 3. Collect the coin
    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(0, WIDTH - coin.width)
        coin.y = random.randint(60, HEIGHT - coin.height)

    # 4. Draw everything
    screen.fill(BLUE)

    pygame.draw.rect(screen, RED, player)
    pygame.draw.circle(screen, YELLOW, coin.center, 12)

    title = font.render("Collect the Coins!", True, WHITE)
    score_text = font.render(f"Score: {score}", True, GREEN)

    screen.blit(title, (20, 15))
    screen.blit(score_text, (620, 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

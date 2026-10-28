
import pygame
import random

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 5 - Keyboard Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
BACKGROUND = (20, 25, 50)
RED = (255, 70, 70)
YELLOW = (255, 220, 50)
WHITE = (255, 255, 255)
GREEN = (50, 230, 140)

# Player and coin
player = pygame.Rect(100, 100, 40, 40)
coin = pygame.Rect(400, 300, 24, 24)

speed = 5
score = 0
running = True

while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Respond to a single key press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_SPACE:
                print("Space pressed!")

    # 2. Check held keys and move player
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

    # Keep player inside the window
    player.clamp_ip(screen.get_rect())

    # 3. Collect coin
    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(0, WIDTH - coin.width)
        coin.y = random.randint(60, HEIGHT - coin.height)

    # 4. Draw the game
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, RED, player, border_radius=8)
    pygame.draw.circle(screen, YELLOW, coin.center, 12)

    screen.blit(
        font.render(f"Score: {score}", True, WHITE),
        (20, 15)
    )
    screen.blit(
        font.render("Move: Arrows / WASD", True, GREEN),
        (20, 50)
    )
    screen.blit(
        font.render("ESC: Exit", True, WHITE),
        (20, 85)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

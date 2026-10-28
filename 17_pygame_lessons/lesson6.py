
import pygame
import random

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 7 - Shapes Collector")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# Colors
BACKGROUND = (18, 25, 45)
WHITE = (255, 255, 255)
GREEN = (50, 230, 130)
YELLOW = (255, 210, 50)
RED = (255, 75, 85)
BLUE = (70, 150, 255)

# Player
player = pygame.Rect(60, 100, 35, 35)
speed = 5

# Collectible
coin_radius = 14
coin_x = random.randint(coin_radius, WIDTH - coin_radius)
coin_y = random.randint(80, HEIGHT - coin_radius)

# Obstacles
obstacles = [
    pygame.Rect(250, 150, 120, 35),
    pygame.Rect(450, 270, 35, 140),
    pygame.Rect(170, 420, 140, 35),
]

score = 0
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Keep player inside window
    player.clamp_ip(screen.get_rect())

    # Circle collision: use a rectangle around the coin
    coin_rect = pygame.Rect(
        coin_x - coin_radius,
        coin_y - coin_radius,
        coin_radius * 2,
        coin_radius * 2
    )

    if player.colliderect(coin_rect):
        score += 1
        coin_x = random.randint(coin_radius, WIDTH - coin_radius)
        coin_y = random.randint(80, HEIGHT - coin_radius)

    # Draw background
    screen.fill(BACKGROUND)

    # Draw grid lines
    for x in range(0, WIDTH, 40):
        pygame.draw.line(
            screen, (35, 45, 65), (x, 70), (x, HEIGHT), 1
        )

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle, border_radius=5)

    # Draw player
    pygame.draw.rect(screen, GREEN, player, border_radius=6)

    # Draw coin
    pygame.draw.circle(
        screen, YELLOW, (coin_x, coin_y), coin_radius
    )
    pygame.draw.circle(
        screen, WHITE, (coin_x, coin_y), coin_radius, 2
    )

    # Draw score and instructions
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, 65))

    screen.blit(
        font.render(f"Score: {score}", True, WHITE),
        (20, 20)
    )
    screen.blit(
        font.render("Move with arrow keys", True, WHITE),
        (200, 20)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

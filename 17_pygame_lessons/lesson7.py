
import pygame
import random
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28, bold=True)
small_font = pygame.font.SysFont("arial", 18)

# Load your images
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

# Colors
GRASS = (67, 145, 75)
DARK_GRASS = (57, 128, 65)
LIGHT_GRASS = (78, 158, 82)
PATH = (205, 184, 137)
PATH_EDGE = (160, 137, 99)
WHITE = (255, 255, 255)
DARK = (35, 48, 39)
GOLD = (255, 215, 75)

# Player
player = pygame.Rect(100, 200, 55, 55)
speed = 5

# Coin
coin = pygame.Rect(
    random.randint(50, WIDTH - 50),
    random.randint(100, HEIGHT - 50),
    38, 38
)

score = 0
running = True

# Decorative grass details
random.seed(10)
grass_marks = [
    (random.randint(0, WIDTH),
     random.randint(90, HEIGHT))
    for _ in range(180)
]

random.seed()

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

    # Keep player inside the screen
    player.clamp_ip(screen.get_rect())

    # Collect coin
    if player.colliderect(coin):
        score += 1

        coin.x = random.randint(20, WIDTH - 58)
        coin.y = random.randint(100, HEIGHT - 58)

    # Background grass
    screen.fill(GRASS)

    # Grass texture
    for i, (gx, gy) in enumerate(grass_marks):
        color = LIGHT_GRASS if i % 2 == 0 else DARK_GRASS
        pygame.draw.line(
            screen, color,
            (gx, gy), (gx + 4, gy - 5), 2
        )

    

   

    # Score panel
    pygame.draw.rect(
        screen, (30, 55, 40), (15, 12, 230, 65),
        border_radius=14
    )
    pygame.draw.rect(
        screen, (100, 180, 95), (15, 12, 230, 65),
        width=2, border_radius=14
    )

    screen.blit(
        font.render(f"Coins: {score}", True, GOLD),
        (30, 18)
    )
    screen.blit(
        small_font.render("Collect as many as you can!", True, WHITE),
        (30, 49)
    )

    # Draw coin and player
    screen.blit(coin_image, coin.topleft)
    screen.blit(player_image, player.topleft)

    # Controls
    screen.blit(
        small_font.render("Move: Arrow keys or WASD", True, WHITE),
        (WIDTH - 265, 25)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

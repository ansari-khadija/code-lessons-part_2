
import pygame
import random
from pathlib import Path

pygame.init()

# ---------------------------------
# 1. CREATE THE GAME WINDOW
# ---------------------------------

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 12 - Coin Collector")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 28, bold=True)
small_font = pygame.font.SysFont("arial", 18)

# ---------------------------------
# 2. LOAD YOUR IMAGES
# ---------------------------------

# Find the folder containing this Python file.
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

player_image = pygame.image.load(
    str(IMAGE_DIR / "player.png")
).convert_alpha()

coin_image = pygame.image.load(
    str(IMAGE_DIR / "coin.png")
).convert_alpha()

# Resize the images.
player_image = pygame.transform.scale(
    player_image, (55, 55)
)

coin_image = pygame.transform.scale(
    coin_image, (38, 38)
)

# ---------------------------------
# 3. SOUND TUTORIAL — FOR LATER
# ---------------------------------

# Sound effects are useful for collecting coins,
# jumping, losing, and winning.
#
# AT HOME, when you have a sound file:
#
# 1. Create a folder called "sounds" beside this file.
# 2. Put a short sound named "collect.wav" inside it.
# 3. After pygame.init(), add:
#
#    pygame.mixer.init()
#
# 4. After defining BASE_DIR, add:
#
#    SOUND_DIR = BASE_DIR / "sounds"
#    collect_sound = pygame.mixer.Sound(
#        str(SOUND_DIR / "collect.wav")
#    )
#
# 5. Inside the coin collision block below, add:
#
#    collect_sound.play()
#
# Sound() loads the audio file.
# play() plays the sound.
# set_volume(0.5) sets the volume to 50%.
#
# Everything is commented out for now,
# so this game will be silent during class!

# ---------------------------------
# 4. PLAYER AND COIN
# ---------------------------------

player = pygame.Rect(100, 200, 55, 55)

coin = pygame.Rect(
    random.randint(0, WIDTH - 38),
    random.randint(100, HEIGHT - 38),
    38, 38
)

speed = 5
score = 0
running = True

# ---------------------------------
# 5. MAIN GAME LOOP
# ---------------------------------

while running:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN detects a key press.
        # Example: event.key == pygame.K_SPACE
        # can detect the Space key.

    # ---------------------------------
    # 6. MOVE THE PLAYER
    # ---------------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

    # Keep the player inside the screen.
    player.clamp_ip(screen.get_rect())

    # ---------------------------------
    # 7. COLLECT THE COIN
    # ---------------------------------

    if player.colliderect(coin):

        score += 1

        # SOUND GOES HERE LATER:
        # collect_sound.play()

        # Move the coin to a new random position.
        coin.x = random.randint(0, WIDTH - coin.width)
        coin.y = random.randint(90, HEIGHT - coin.height)

    # ---------------------------------
    # 8. DRAW THE BACKGROUND
    # ---------------------------------

    # Green grass background.
    screen.fill((67, 145, 75))

    # Decorative grass marks.
    for i in range(100):

        x = (i * 83) % WIDTH
        y = 90 + (i * 47) % (HEIGHT - 90)

        pygame.draw.line(
            screen,
            (85, 160, 85),
            (x, y),
            (x + 4, y - 5),
            2
        )

    # Draw player and coin images.
    screen.blit(player_image, player.topleft)
    screen.blit(coin_image, coin.topleft)

    # ---------------------------------
    # 9. DISPLAY TEXT
    # ---------------------------------

    score_text = font.render(
        f"Coins: {score}", True, (255, 215, 75)
    )

    screen.blit(score_text, (20, 20))

    controls_text = small_font.render(
        "Move: Arrow keys or WASD", True, (255, 255, 255)
    )

    screen.blit(controls_text, (20, 55))

    # Update the display.
    pygame.display.flip()

    # Limit the game to 60 FPS.
    clock.tick(60)

pygame.quit()

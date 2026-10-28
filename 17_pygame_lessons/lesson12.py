
import pygame
import random
from pathlib import Path

pygame.init()

# --------------------------------
# 1. CREATE THE WINDOW
# --------------------------------

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 13 - Sprite Module")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 28, bold=True)
small_font = pygame.font.SysFont("arial", 18)

# --------------------------------
# 2. LOAD IMAGES
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

player_image = pygame.image.load(
    str(IMAGE_DIR / "player.png")
).convert_alpha()

coin_image = pygame.image.load(
    str(IMAGE_DIR / "coin.png")
).convert_alpha()

player_image = pygame.transform.scale(
    player_image, (55, 55)
)

coin_image = pygame.transform.scale(
    coin_image, (38, 38)
)

# --------------------------------
# 3. PLAYER SPRITE CLASS
# --------------------------------

# A class is a blueprint for creating objects.
# A Sprite represents an object in the game.
#
# self.image = what the sprite looks like.
# self.rect = its position and collision area.
# update() contains the sprite's movement logic.

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = player_image
        self.rect = self.image.get_rect(
            topleft=(100, 200)
        )

        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Keep player inside the window.
        self.rect.clamp_ip(screen.get_rect())


# --------------------------------
# 4. COIN SPRITE CLASS
# --------------------------------

class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = coin_image
        self.rect = self.image.get_rect()

        self.move_to_random_position()

    def move_to_random_position(self):
        self.rect.x = random.randint(
            0, WIDTH - self.rect.width
        )

        self.rect.y = random.randint(
            90, HEIGHT - self.rect.height
        )


# --------------------------------
# 5. CREATE SPRITES AND GROUP
# --------------------------------

player = Player()
coin = Coin()

# A Group manages multiple sprites together.
all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(coin)

# --------------------------------
# 6. SCORE
# --------------------------------

score = 0
running = True

# --------------------------------
# 7. MAIN GAME LOOP
# --------------------------------

while running:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # UPDATE SPRITES
    # Calls update() on every sprite in the group.
    all_sprites.update()

    # --------------------------------
    # 8. COLLISION DETECTION
    # --------------------------------

    # Detect whether the player touches the coin.
    if pygame.sprite.collide_rect(player, coin):

        score += 1
        coin.move_to_random_position()

        # SOUND TUTORIAL — ADD LATER AT HOME:
        # 1. Create a folder called "sounds".
        # 2. Put collect.wav inside that folder.
        # 3. After pygame.init(), add:
        #
        #    pygame.mixer.init()
        #
        # 4. Load the sound:
        #
        #    SOUND_DIR = BASE_DIR / "sounds"
        #    collect_sound = pygame.mixer.Sound(
        #        str(SOUND_DIR / "collect.wav")
        #    )
        #
        # 5. Inside this collision block, add:
        #
        #    collect_sound.play()
        #
        # Sound() loads a sound effect.
        # play() plays it when the coin is collected.

    # --------------------------------
    # 9. DRAW BACKGROUND
    # --------------------------------

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

    # Draw every sprite in the group.
    all_sprites.draw(screen)

    # --------------------------------
    # 10. DISPLAY SCORE
    # --------------------------------

    score_text = font.render(
        f"Coins: {score}",
        True,
        (255, 215, 75)
    )

    screen.blit(score_text, (20, 20))

    controls = small_font.render(
        "Move: Arrows or WASD",
        True,
        (255, 255, 255)
    )

    screen.blit(controls, (20, 55))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

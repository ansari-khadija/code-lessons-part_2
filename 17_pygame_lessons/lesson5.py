
import pygame
import random

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 6 - Click the Target")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 48)

# Colors
BACKGROUND = (20, 25, 55)
WHITE = (255, 255, 255)
YELLOW = (255, 210, 40)
RED = (255, 80, 80)
GREEN = (60, 230, 140)

# Target
radius = 28
target_x = random.randint(radius, WIDTH - radius)
target_y = random.randint(100 + radius, HEIGHT - radius)

score = 0
misses = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = event.pos

                # Distance from click to target center
                dx = mx - target_x
                dy = my - target_y

                if dx * dx + dy * dy <= radius * radius:
                    score += 1
                    target_x = random.randint(radius, WIDTH - radius)
                    target_y = random.randint(
                        100 + radius, HEIGHT - radius
                    )
                else:
                    misses += 1

    # Draw background
    screen.fill(BACKGROUND)

    # Header
    title = big_font.render("CLICK THE TARGET!", True, WHITE)
    screen.blit(title, (20, 20))

    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (20, 65))

    miss_text = font.render(f"Misses: {misses}", True, RED)
    screen.blit(miss_text, (200, 65))

    # Draw target
    pygame.draw.circle(
        screen, YELLOW, (target_x, target_y), radius
    )
    pygame.draw.circle(
        screen, RED, (target_x, target_y), radius, 4
    )

    # Show mouse position
    mx, my = pygame.mouse.get_pos()
    mouse_text = font.render(
        f"Mouse: {mx}, {my}", True, WHITE
    )
    screen.blit(mouse_text, (20, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

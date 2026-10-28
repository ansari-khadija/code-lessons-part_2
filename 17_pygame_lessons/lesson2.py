
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colorful Shapes")

# Colors
BLACK = (20, 20, 30)
RED = (255, 60, 60)
GREEN = (50, 220, 100)
BLUE = (60, 120, 255)
YELLOW = (255, 220, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw colorful shapes
    pygame.draw.rect(screen, RED, (100, 100, 150, 100))
    pygame.draw.circle(screen, GREEN, (400, 150), 60)
    pygame.draw.rect(screen, BLUE, (550, 100, 120, 120))
    pygame.draw.circle(screen, YELLOW, (400, 400), 80)

    pygame.display.flip()

pygame.quit()

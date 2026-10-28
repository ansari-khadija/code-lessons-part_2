
import pygame

# Initialize Pygame
pygame.init()

# Create the display window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lesson 1 - My First Game")

# Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)

# Main game loop
running = True

while running:
    # Handle window events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.fill(BLUE)

    # Update the display
    pygame.display.flip()

# Close Pygame
pygame.quit()

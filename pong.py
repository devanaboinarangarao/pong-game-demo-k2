import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black color
    window.fill((0, 0, 0))

    # Update the display with the new frame
    pygame.display.flip()

# Quit Pygame when the loop ends
pygame.quit()
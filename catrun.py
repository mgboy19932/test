import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chasing Cat")

# Load cat image
cat_image = pygame.image.load("cat.png")
cat_rect = cat_image.get_rect()

# Main loop
while True:
    # Clear the screen
    screen.fill((255, 255, 255))

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate cat position to chase the mouse
    cat_rect.centerx += (mouse_x - cat_rect.centerx) * 0.05
    cat_rect.centery += (mouse_y - cat_rect.centery) * 0.05

    # Draw the cat
    screen.blit(cat_image, cat_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()

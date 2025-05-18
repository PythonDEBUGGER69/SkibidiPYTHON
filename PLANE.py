import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Plane settings
PLANE_WIDTH = 50
PLANE_HEIGHT = 50
PLANE_SPEED = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Plane Game")

# Load realistic plane image
if not os.path.exists("realistic_plane.png"):
    print("Please make sure you have a realistic plane image named 'realistic_plane.png' in the same directory.")
    sys.exit()

plane_image = pygame.image.load("realistic_plane.png")
plane_image = pygame.transform.scale(plane_image, (PLANE_WIDTH, PLANE_HEIGHT))

# Plane initial position
plane_x = SCREEN_WIDTH // 2
plane_y = SCREEN_HEIGHT // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move plane
    if keys[pygame.K_LEFT]:
        plane_x -= PLANE_SPEED
    if keys[pygame.K_RIGHT]:
        plane_x += PLANE_SPEED
    if keys[pygame.K_UP]:
        plane_y -= PLANE_SPEED
    if keys[pygame.K_DOWN]:
        plane_y += PLANE_SPEED

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the plane
    screen.blit(plane_image, (plane_x, plane_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
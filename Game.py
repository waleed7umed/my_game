# game.py

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Define game variables
clock = pygame.time.Clock()
color = (255, 0, 0)  # Red

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Fill the screen with color
    screen.fill(color)
    
    # Update the screen
    pygame.display.flip()
    
    # Set the frame rate
    clock.tick(60)

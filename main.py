import pygame
from sys import exit

# Initialize pygame
pygame.init()

# Set up pygame screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Runner")

# Framerate control
clock = pygame.time.Clock()

# In-game features
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Update screen
    pygame.display.update()
    clock.tick(60) # Frame ceiling
    
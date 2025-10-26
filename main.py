import pygame
from sys import exit
from helpers import load_font

def display_text(x, y, text=None, font_type=None, font_size=50):
    
    font = load_font(x, y, text, font_type, font_size)
    
    screen.blit(font[0], font[1]) 
    
# Initialize pygame
pygame.init()

# Set up pygame screen
WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")

# Framerate control
clock = pygame.time.Clock()

# Text surface display

# Principal menu

# In-game features
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Background color
    screen.fill((94,129,162))
    
    # Text display
    
    x = WIDTH / 2
    menu_options = ["Play", "Editor", "Tutorial", "Options", "Credits", "Exit"]
    display_text(x, 50, "My game", "Exo2-Regular")
    
    for i in range(len(menu_options)):
        display_text(x, 250 + 80*i, menu_options[i], "Lato-Regular")
    
    # Update screen
    pygame.display.update()
    clock.tick(60) # Frame ceiling
    
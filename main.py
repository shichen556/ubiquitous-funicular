import pygame
from os import path
from sys import exit
    
# Initialize pygame
pygame.init()

# Set up pygame screen
WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")

# Framerate control
clock = pygame.time.Clock()

# Menu buttons setup
font_title = pygame.font.SysFont("Trebuchet MS", 80)
font_text = pygame.font.SysFont("Tahoma", 50)
font_button = pygame.font.SysFont("Arial Rounded MT Bold", 40)

central_pos_x = WIDTH / 2


title_surf = font_title.render("My game", True, "Black")
title_rect = title_surf.get_rect(center = (central_pos_x, 80))

pos_y = 250
inter_pos_y = 80
i=0
in_menu = 1

play_button_surf = font_text.render("Play", True, "Black")
play_button_rect = play_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

editor_button_surf = font_text.render("Editor", True, "Black")
editor_button_rect = editor_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

tutorial_button_surf = font_text.render("Tutorial", True, "Black")
tutorial_button_rect = tutorial_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

options_button_surf = font_text.render("Options", True, "Black")
options_button_rect = options_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

credits_button_surf = font_text.render("Credits", True, "Black")
credits_button_rect = credits_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

exit_button_surf = font_text.render("Exit", True, "Black")
exit_button_rect = exit_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))

back_button_surf = font_button.render("Back", True, "Black")
back_button_rect = back_button_surf.get_rect(center = (50, 40))

# In-game features
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                # Start the game
                in_menu = 0
                
                pygame.draw.circle(screen, "yellow", (500,500), 5)
                
            elif editor_button_rect.collidepoint(event.pos):
                # Open the editor
                in_menu = 0
                
            elif tutorial_button_rect.collidepoint(event.pos):
                # Open the tutorial
                in_menu = 0
                
            elif options_button_rect.collidepoint(event.pos):
                # Open options menu
                in_menu = 0
                
            elif credits_button_rect.collidepoint(event.pos):
                # Show credits
                in_menu = 0
                
            elif exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()
            elif back_button_rect.collidepoint(event.pos):
                in_menu = 1
    
    # Background color
    screen.fill((94,129,162))
    
    # Text display
    
    # Principal menu
    
    if in_menu:
        # Game title
        screen.blit(title_surf, title_rect)
        
        # Menu options
        screen.blit(play_button_surf, play_button_rect)
        screen.blit(editor_button_surf, editor_button_rect)
        screen.blit(tutorial_button_surf, tutorial_button_rect)
        screen.blit(options_button_surf, options_button_rect)
        screen.blit(credits_button_surf, credits_button_rect)
        screen.blit(exit_button_surf, exit_button_rect)
    else:
        screen.blit(back_button_surf, back_button_rect)
        
    # Update screen
    pygame.display.update()
    clock.tick(60) # Frame ceiling
    
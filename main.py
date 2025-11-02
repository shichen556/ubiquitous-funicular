import pygame
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
central_pos_x = WIDTH / 2

font_title = pygame.font.Font("assets/font/Exo2-regular.ttf", 50)
title_surf = font_title.render("My game", True, "Black")
title_rect = title_surf.get_rect(center = (central_pos_x, 50))

font_text = pygame.font.Font("assets/font/Lato-Regular.ttf", 50)

play_button_surf = font_text.render("Play", True, "Black")
play_button_rect = play_button_surf.get_rect(center = (central_pos_x, 200))

editor_button_surf = font_text.render("Editor", True, "Black")
editor_button_rect = editor_button_surf.get_rect(center = (central_pos_x, 260))

tutorial_button_surf = font_text.render("Tutorial", True, "Black")
tutorial_button_rect = tutorial_button_surf.get_rect(center = (central_pos_x, 320))

options_button_surf = font_text.render("Options", True, "Black")
options_button_rect = options_button_surf.get_rect(center = (central_pos_x, 380))

credits_button_surf = font_text.render("Credits", True, "Black")
credits_button_rect = credits_button_surf.get_rect(center = (central_pos_x, 440))

exit_button_surf = font_text.render("Exit", True, "Black")
exit_button_rect = exit_button_surf.get_rect(center = (central_pos_x, 500))


# In-game features
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                # Start the game
                pass
            elif editor_button_rect.collidepoint(event.pos):
                # Open the editor
                pass
            elif tutorial_button_rect.collidepoint(event.pos):
                # Open the tutorial
                pass
            elif options_button_rect.collidepoint(event.pos):
                # Open options menu
                pass
            elif credits_button_rect.collidepoint(event.pos):
                # Show credits
                pass
            elif exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()
    
    # Background color
    screen.fill((94,129,162))
    
    # Text display
    
    # Principal menu
    
    # Game title
    screen.blit(title_surf, title_rect)
    
    # Menu options
    screen.blit(play_button_surf, play_button_rect)
    screen.blit(editor_button_surf, editor_button_rect)
    screen.blit(tutorial_button_surf, tutorial_button_rect)
    screen.blit(options_button_surf, options_button_rect)
    screen.blit(credits_button_surf, credits_button_rect)
    screen.blit(exit_button_surf, exit_button_rect)
    
    # Update screen
    pygame.display.update()
    clock.tick(60) # Frame ceiling
    
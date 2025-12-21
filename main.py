import pygame
from os import path
from sys import exit

def draw_electric_field(rect, color, spacing = 50):
    area_subsurf = screen.subsurface(rect)
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    width, height = area_subsurf.get_size()
    
    arrow_length = 20
    arrow_size = 6
    
    for y in range(spacing//2, height, spacing):
        # Horizontal lines
        pygame.draw.line(area_subsurf, color, (0,y), (width, y), 2)
        
        # Arrow after a interval
        for x in range(0, width, 100):
            pygame.draw.line(area_subsurf, color,
                             (x, y),
                             (x + arrow_length, y - arrow_size), 2)
            pygame.draw.line(area_subsurf, color,
                             (x, y),
                             (x + arrow_length, y + arrow_size), 2)
            
def draw_magnetic_field_out(rect, color_out, spacing=60):
    area_subsurf = screen.subsurface(rect)
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    width, height = area_subsurf.get_size()
    
    for y in range(spacing//3, height, spacing):
        for x in range(spacing//3, width, spacing):
            # Campo saliente (·)
            pygame.draw.circle(area_subsurf, color_out, (x, y), 12, 1)
            pygame.draw.circle(area_subsurf, color_out, (x, y), 4)
                
def draw_magnetic_field_in(rect, color_in, spacing=60):
    area_subsurf = screen.subsurface(rect)
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    width, height = area_subsurf.get_size()
    for y in range(spacing//3, height, spacing):
        for x in range(spacing//3, width, spacing):
            # Campo entrante (x)
            pygame.draw.circle(area_subsurf, color_in, (x, y), 12, 1)
            pygame.draw.line(area_subsurf, color_in, (x-4, y-4), (x+4, y+4), 2)
            pygame.draw.line(area_subsurf, color_in, (x-4, y+4), (x+4, y-4), 2)

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


title_surf = font_title.render("My game", True, "#B0C4FF")
title_rect = title_surf.get_rect(center = (central_pos_x, 80))

pos_y = 250
inter_pos_y = 80
i=0
in_menu = 0
in_play = 1

pos_x = 50        
vel = 3
            
button_color = ["#00BFFF", "#2A3B7A"]
on_button = 0

play_button_surf = font_text.render("Play", True, button_color[on_button])
play_button_rect = play_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

editor_button_surf = font_text.render("Editor", True, button_color[on_button])
editor_button_rect = editor_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

tutorial_button_surf = font_text.render("Tutorial", True, button_color[on_button])
tutorial_button_rect = tutorial_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

options_button_surf = font_text.render("Options", True, button_color[on_button])
options_button_rect = options_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

credits_button_surf = font_text.render("Credits", True, button_color[on_button])
credits_button_rect = credits_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))
i+=1

exit_button_surf = font_text.render("Exit", True, button_color[on_button])
exit_button_rect = exit_button_surf.get_rect(center = (central_pos_x, pos_y+inter_pos_y*i))

back_button_surf = font_button.render("Back to menu", True, button_color[on_button])
back_button_rect = back_button_surf.get_rect(center = (100, 40))

area_pos_x = 450
area_pos_y = 350
            
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
                
                in_play = 1
                
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
                in_play = 0
    
    # Text display
    
    # Principal menu
    
    if in_menu:
        # Background color
        screen.fill("#0A0A23")
        # Game title
        screen.blit(title_surf, title_rect)
        
        # Menu options
        screen.blit(play_button_surf, play_button_rect)
        screen.blit(editor_button_surf, editor_button_rect)
        screen.blit(tutorial_button_surf, tutorial_button_rect)
        screen.blit(options_button_surf, options_button_rect)
        screen.blit(credits_button_surf, credits_button_rect)
        screen.blit(exit_button_surf, exit_button_rect)
        
    if not in_menu:
        screen.fill("#0A0A23")
        
        screen.blit(back_button_surf, back_button_rect)
        if in_play:
            pos_x += vel
            
            if pos_x >= 1000:
                pos_x = -100
            
            E_field_color = "#FFD700"
            B_out_color = "#00FFCC"
            B_in_color = "#9B30FF"
            
            area_rect = pygame.Rect(area_pos_x - 50, area_pos_y - 50, 100, 100)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                area_pos_x, area_pos_y = pygame.mouse.get_pos()
                print(area_pos_x, area_pos_y)
                 
            draw_magnetic_field_in(area_rect, B_in_color)
            
            # Negative charge
            electron = pygame.draw.circle(screen, "#1E90FF", (pos_x, 200), 10)
            
            # Positive charge
            proton = pygame.draw.circle(screen, "#FF4500", (pos_x,300), 10)
            
            
    # Update screen
    pygame.display.update()
    clock.tick(60) # Frame ceiling
    
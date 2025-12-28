import pygame
from os import path
from sys import exit
from math import sin, cos

class Options:
    def __init__(self, font, text):
        self.font=font
        self.text=text
        self.central_pos_x=WIDTH / 2
        
class Title(Options):
    def __init__(self, font, text):
        super().__init__(font, text, central_pos_x)
    
class Button(Options):
    def __init__(self, font, text):
        super().__init__(font, text, central_pos_x)

class Menu:
    def __init__(self):
        self.title=Title()
        self.button=Button()
        self.opciones = []
        
    def display_menu():
        pass
        

class Particle:
    def __init__(self, pos_x, pos_y, charge):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.charge = charge
    
    def draw_particle(color):
        pygame.draw.circle(screen, color, (pos_x, pos_y), 10)


def draw_electric_field(rect, spacing = 50):
    color = "#FFD700"
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
            
def draw_magnetic_field_out(rect, spacing=60):
    color = "#00FFCC"
    area_subsurf = screen.subsurface(rect)
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    width, height = area_subsurf.get_size()
    
    for y in range(spacing//3, height, spacing):
        for x in range(spacing//3, width, spacing):
            # Campo saliente (·)
            pygame.draw.circle(area_subsurf, color, (x, y), 12, 1)
            pygame.draw.circle(area_subsurf, color, (x, y), 4)
                
def draw_magnetic_field_in(rect, spacing=60):
    color =  "#9B30FF"
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    for y in range(rect.top + 20, rect.bottom, spacing):
        for x in range(rect.left + 20, rect.right, spacing):
            # Campo entrante (x)
            pygame.draw.circle(screen, color, (x, y), 12, 1)
            pygame.draw.line(screen, color, (x-4, y-4), (x+4, y+4), 2)
            pygame.draw.line(screen, color, (x-4, y+4), (x+4, y-4), 2)

def rotate(x, y):
    angulo += vel_ang
    
    v_x = vel * cos(angulo)
    v_y = vel * sin(angulo)
    
    x += v_x
    y += v_y
    
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

vel = 5
v_x = vel
v_y = 0

e_pos_x=50
e_pos_y=200

            
# p_pos_x=200
# p_pos_y=300

# Constantes
q = 1.602
m = 9.11
B = 1

# valores MCU
radio = m*vel/(q*B)
angulo = 0
vel_ang = vel/radio

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
            # electron = Particle(e_pos_x, e_pos_y, "Negative")
            # proton = Particle(p_pos_x, p_pos_y, "Positive")
            
            area_rect = pygame.Rect(area_pos_x - 50, area_pos_y - 50, 100, 100)
            draw_magnetic_field_in(area_rect)
            
            # Negative charge
            # electron.draw_particle(color = "#1E90FF")
            electron = pygame.draw.circle(screen, "#1E90FF", (e_pos_x, e_pos_y), 10)
            
            # Positive charge
            # proton = pygame.draw.circle(screen, "#FF4500", (pos_x,300), 10)
            
            if e_pos_x > 1000 or e_pos_x < -100 or e_pos_y > 800 or e_pos_y < -100:
                e_pos_x = -100
                e_pos_y = 200
                
                angulo = 0
                v_x = vel
                v_y = 0
            
            if electron.colliderect(area_rect):
                # MCU
                angulo -= vel_ang
    
                v_x = vel * cos(angulo)
                v_y = vel * sin(angulo)
                
                e_pos_x += v_x
                e_pos_y += v_y
            else:
                # MRU
                e_pos_x += v_x
                e_pos_y += v_y
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                area_pos_x, area_pos_y = pygame.mouse.get_pos()
                print(area_pos_x, area_pos_y)
                 
    # Update screen
    pygame.display.update()
    clock.tick(60) # Frame ceiling
    
import pygame
from math import sin, cos

# Allow autocomplete in circular import (AI)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

class Object:
    def __init__(self, game: "Game"):
        self.game = game
        
        self.run_display = True
    
    def blit_scren(self):
        self.game.window.blit(self.game.display, (0,0))

        pygame.display.update()
        self.game.reset_keys()

class Field(Object):
    def __init__(self, game):
        super().__init__(game)
        self.square = pygame.Rect(200, 200, 100, 100)
        
class ElectricField(Field):
    def __init__(self, game):
        super().__init__(game)
        
        # (AI)
        self.spacing = 30
        
        self.color = "#FFD700"
        
        self.arrow_length = 10
        self.arrow_size = 6
        
        self.arrow_spacing = 50
    
    # (AI)
    def draw_left(self):
        pygame.draw.rect(self.game.display, "white", self.square, 1)
        
        for y in range(self.square.top + 20, self.square.bottom, self.spacing):
            # Horizontal lines
            pygame.draw.line(self.game.display, self.color, (self.square.left, y), (self.square.right, y), 2)
            
            # Arrow after a interval
            for x in range(self.square.left + 20, self.square.right, self.arrow_spacing):
                pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_length, y - self.arrow_size), 2)
                pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_length, y + self.arrow_size), 2)
    
    def draw_right(self):
        pygame.draw.rect(self.game.display, "white", self.square, 1)
        
        for y in range(self.square.top + 20, self.square.bottom, self.spacing):
            # Horizontal lines
            pygame.draw.line(self.game.display, self.color, (self.square.left, y), (self.square.right, y), 2)
            
            # Arrow after a interval
            for x in range(self.square.right + 20, self.square.left, -self.arrow_spacing):
                pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_length, y - self.arrow_size), 2)
                pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_length, y + self.arrow_size), 2)
    
    
    def draw_up(self):
        pygame.draw.rect(self.game.display, "white", self.square, 1)
        
        for x in range(self.square.left + 20, self.square.right, self.spacing):
            # Vertical lines
            pygame.draw.line(self.game.display, self.color, (x, self.square.top), (x, self.square.bottom), 2)
            
            # Arrow after a interval
            for y in range(self.square.top + 20, self.square.bottom, self.arrow_spacing):
                pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_size, y + self.arrow_length), 2)
                pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_size, y + self.arrow_length), 2)
    
    
    def draw_down(self):
        pygame.draw.rect(self.game.display, "white", self.square, 1)
        
        for x in range(self.square.left + 20, self.square.right, self.spacing):
            # Horizontal lines
            pygame.draw.line(self.game.display, self.color, (x, self.square.top), (x, self.square.bottom), 2)
            
            # Arrow after a interval
            for y in range(self.square.top + 20, self.square.bottom, self.arrow_spacing):
                pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_size, y + self.arrow_length), 2)
                pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_size, y + self.arrow_length), 2)
    
    
class MagneticField(Field):
    def __init__(self, game):
        super().__init__(game)
        
        # (AI)
        self.spacing = 60
    
    # (AI)
    def draw_in(self):
        self.color_in =  "#9B30FF"
        pygame.draw.rect(self.game.display, "white", self.square, 1)
    
        for y in range(self.square.top + 20, self.square.bottom, self.spacing):
            for x in range(self.square.left + 20, self.square.right, self.spacing):
                # Campo entrante (x)
                pygame.draw.circle(self.game.display, self.color_in, (x, y), 12, 1)
                pygame.draw.line(self.game.display, self.color_in, (x-4, y-4), (x+4, y+4), 2)
                pygame.draw.line(self.game.display, self.color_in, (x-4, y+4), (x+4, y-4), 2)
    
    # (AI)
    def draw_out(self):
        self.color_out = "#00FFCC"
        pygame.draw.rect(self.game.display, "white", self.square, 1)
        
        for y in range(self.square.top + 20, self.square.bottom, self.spacing):
            for x in range(self.square.left + 20, self.square.right, self.spacing):
                # Campo saliente (·)
                pygame.draw.circle(self.game.display, self.color_out, (x, y), 12, 1)
                pygame.draw.circle(self.game.display, self.color_out, (x, y), 4)

class Particle(Object):
    def __init__(self, game):
        super().__init__(game)
        
        
    def draw_e(self): 
        self.color = "#1E90FF"
        self.e_posx = 50
        self.e_posy = 200
        
        self.electron = pygame.draw.circle(self.game.display, self.color, (e_pos_x, e_pos_y), 10)

    def draw_p(self):
        self.color = "#FF4500"
        self.p_posx = 50
        self.p_posy = 300
        
        self.proton = pygame.draw.circle(self.game.display, self.color, (self.p_posx, self.p_posy), 10)
    
def rotate(x, y):
    angulo += vel_ang
    
    v_x = vel * cos(angulo)
    v_y = vel * sin(angulo)
    
    x += v_x
    y += v_y

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
B = 0.5

# valores MCU
radio = m*vel/(q*B)
angulo = 0
vel_ang = vel/radio
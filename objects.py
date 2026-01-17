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
        
class ElectricField(Object):
    def __init__(self, game, type):
        super().__init__(game)

        self.square = pygame.Rect(200, 200, 100, 100)
        
        self.spacing = 30
        
        self.color = "#FFD700"
        
        self.arrow_length = 10
        self.arrow_size = 6
        
        self.arrow_spacing = 50
        
        self.type = type
    
    def draw(self):
        pygame.draw.rect(self.game.display, "white", self.square, 1)
        
        if self.type == "left" or self.type == "right":
            for y in range(self.square.top + 20, self.square.bottom, self.spacing):
                # Horizontal lines
                pygame.draw.line(self.game.display, self.color, (self.square.left, y), (self.square.right, y), 2)
                
                # Arrow after a interval
                if self.type == "left":
                    for x in range(self.square.left + 20, self.square.right, self.arrow_spacing):
                        pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_length, y - self.arrow_size), 2)
                        pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_length, y + self.arrow_size), 2)
                else:
                    for x in range(self.square.right - 20, self.square.left, -self.arrow_spacing):
                        pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_length, y - self.arrow_size), 2)
                        pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_length, y + self.arrow_size), 2)
        elif self.type == "up" or self.type == "down":
            for x in range(self.square.left + 20, self.square.right, self.spacing):
                # Vertical lines
                pygame.draw.line(self.game.display, self.color, (x, self.square.top), (x, self.square.bottom), 2)
                
                # Arrow after a interval
                if self.type == "up":
                    for y in range(self.square.top + 20, self.square.bottom, self.arrow_spacing):
                        pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_size, y + self.arrow_length), 2)
                        pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_size, y + self.arrow_length), 2)
                else:
                    for y in range(self.square.bottom - 20, self.square.top, -self.arrow_spacing):
                        pygame.draw.line(self.game.display, self.color, (x,y), (x - self.arrow_size, y - self.arrow_length), 2)
                        pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_size, y - self.arrow_length), 2)
    
class MagneticField(Object):
    def __init__(self, game, type):
        super().__init__(game)
        
        self.square = pygame.Rect(200, 400, 100, 100)
        
        self.spacing = 60
    
        self.type=type
        
    def draw(self):
        self.color_in =  "#9B30FF"
        self.color_out = "#00FFCC"
        pygame.draw.rect(self.game.display, "white", self.square, 1)
    
        for y in range(self.square.top + 20, self.square.bottom, self.spacing):
            for x in range(self.square.left + 20, self.square.right, self.spacing):
                # Campo entrante (x)
                if self.type == "in":
                    pygame.draw.circle(self.game.display, self.color_in, (x, y), 12, 1)
                    pygame.draw.line(self.game.display, self.color_in, (x-4, y-4), (x+4, y+4), 2)
                    pygame.draw.line(self.game.display, self.color_in, (x-4, y+4), (x+4, y-4), 2)
                # Campo saliente (·)
                else:
                    pygame.draw.circle(self.game.display, self.color_out, (x, y), 12, 1)
                    pygame.draw.circle(self.game.display, self.color_out, (x, y), 4)

class Particle(Object):
    def __init__(self, game, posx, posy):
        super().__init__(game)
        
        self.vel = [2, 0]
        self.MASS = 9.11
        self.CHARGE_VALUE = 1.602
        self.CHARGE_SIGN = ""
        
        self.posx = posx
        self.posy = posy

    def draw(self):    
        self.particle = pygame.draw.circle(self.game.display, self.color, (self.posx, self.posy), 10)
    
class Proton(Particle):
    def __init__(self, game, posx, posy):
        super().__init__(game, posx, posy)
        self.color = "#FF4500"
        self.CHARGE_SIGN = "+"
        
        
class Electron(Particle):
    def __init__(self, game, posx, posy):
        super().__init__(game, posx, posy)
        self.color = "#1E90FF"
        self.CHARGE_SIGN = "-"
    
    
# def rotate(x, y):
#     angulo += vel_ang
    
#     v_x = vel * cos(angulo)
#     v_y = vel * sin(angulo)
    
#     x += v_x
#     y += v_y

# # valores MCU
# radio = m*vel/(q*B)
# angulo = 0
# vel_ang = vel/radio
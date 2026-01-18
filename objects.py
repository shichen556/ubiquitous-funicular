import pygame

# Allow autocomplete in circular import (AI)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

class Object():
    def __init__(self, game: "Game"):
        self.game = game
        
        self.run_display = True
    
    def blit_scren(self):
        self.game.window.blit(self.game.display, (0,0))

        pygame.display.update()
        self.game.reset_keys()
        
class ElectricField(Object):
    def __init__(self, game, pos, size, type, E):
        super().__init__(game)

        self.square = pygame.Rect(pos[0], pos[1], size[0], size[1])
        
        self.spacing = 30
        
        self.color = "#FFD700"
        
        self.arrow_length = 10
        self.arrow_size = 6
        
        self.arrow_spacing = 50
        
        self.type = type
        self.E = E
    
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
    def __init__(self, game, pos, size, type, B):
        super().__init__(game)
        
        self.square = pygame.Rect(pos[0], pos[1], size[0], size[1])
        
        self.spacing = 60
    
        self.type=type
        self.B = B
        
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
    def __init__(self, game, pos, vel, charge_sign):
        super().__init__(game)
        
        self.MASS = 9.11
        self.CHARGE_VALUE = 1.602
        self.charge_sign = charge_sign
        
        self.pos0x = pos[0]
        self.pos0y = pos[1]
        self.rect = pygame.Rect(self.pos0x, self.pos0y, 10, 10)
        
        self.vel0x = vel[0]
        self.vel0y = vel[1]
        self.vel = [vel[0], vel[1]]
        from math import sqrt
        self.mod_vel = sqrt(vel[0]**2+vel[1]**2)
        self.angle = 0
        self.ang_vel = 0.05
        
        
    def draw(self):   
        if self.charge_sign == "+": 
            self.color = "#FF4500"
        else:
            self.color = "#1E90FF"
        
        pygame.draw.circle(self.game.display, self.color, self.rect.center, 10)
    
    def move(self):
        from math import pi
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
        
        if self.rect.left < 0 or self.rect.right > self.game.DISPLAY_W:
            self.vel[0] = -self.vel[0]
        if self.rect.top < 0 or self.rect.bottom > self.game.DISPLAY_H:
            self.vel[1] = -self.vel[1]
        if self.angle > 2*pi:
            self.angle -= 2*pi
    
    def reset_pos(self):
        # Set to initial position
        self.rect.x = self.pos0x
        self.rect.y = self.pos0y
        self.angle = 0
        
        self.vel = [self.vel0x, self.vel0y]
            
    def check_eF_collision(self, e_field_rect):
        if self.rect.colliderect(e_field_rect):
            self.apply_e_force()
    
    def apply_e_force(self):
        if self.charge_sign == "+":
            self.vel[0] += 1
        if self.charge_sign == "-":
            self.vel[0] -= 0.5
        
    def check_mgF_collision(self, mg_field):
        if self.rect.colliderect(mg_field.square):
            self.apply_mg_force(mg_field.type, mg_field.B)
            
    def apply_mg_force(self, type, B):
        from math import sin, cos, sqrt, atan2
        mod_vel = sqrt(self.vel[0]**2 + self.vel[1]**2)
        radio = self.MASS * mod_vel / (self.CHARGE_VALUE * B)
        self.vel_ang = mod_vel / radio
        self.angle = atan2(self.vel[1], self.vel[0])
        
        if self.charge_sign == "+":
            if type == "out":
                self.angle += self.ang_vel
            if type == "in":
                self.angle -= self.ang_vel
                
        if self.charge_sign == "-":
            if type == "out":
                self.angle -= self.ang_vel
            if type == "in":
                self.angle += self.ang_vel
        
        self.vel[0] = mod_vel * cos(self.angle)
        self.vel[1] = mod_vel * sin(self.angle)
        
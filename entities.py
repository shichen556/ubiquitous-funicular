import pygame
from math import sin, cos

class Entity:
    pass

class Particle:
    def __init__(self, pos_x, pos_y, charge):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.charge=charge
        self.mass=9.11
        self.q=1.602
        self.vel = 5
        self.v_x = self.vel
        self.v_y = 0
        self.angulo = 0
        if charge == "Negative":
            self.color = "#1E90FF"
        else:
            self.color = "#FF4500"
    
    def update(self, dt):
        if self.pos_x > 1000 or self.pos_x < -100 or self.pos_y > 800 or self.pos_y < -100:
            self.reset_pos()
            
        if self.is_in_field():
            # MCU
            self.v_x = self.vel * cos(self.angulo)
            self.v_y = self.vel * sin(self.angulo)
        
        # MRU
        self.pos_x += self.v_x
        self.pos_y += self.v_y
    
    def reset_pos(self):
        self.pos_x = -100
        self.pos_y = 200
        self.v_x = self.vel
        self.v_y = 0
        self.angulo = 0
    
    def is_in_field(self):
        # Este método será usado por las partículas
        # pero necesita ser actualizado por la escena de juego
        if not hasattr(self, 'field_rect'):
            return False
        return self.field_rect.collidepoint(self.pos_x, self.pos_y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), 10)
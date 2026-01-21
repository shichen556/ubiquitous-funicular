import pygame
from title import Menu
from debug import debug

class HUD(Menu):
    def __init__(self, game, pos, size, B=None, particle=None, field=None):
        super().__init__(game)
        
        self.rect_ext = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.rect_in = pygame.Rect(pos[0] + 5, pos[1] + 5, size[0] - 10, size[1]- 10)
        
        # Particle base stats
        if particle:
            # Constant values
            self.B = B
            self.field=None
            
            from math import degrees
            self.particle = particle
            self.mass = self.particle.MASS
            self.charge_sign = self.particle.charge_sign
            self.charge_value = self.particle.CHARGE_VALUE
            if self.charge_sign == "+":
                self.name = "Proton"
            else:
                self.name = "Electron"
            
            self.decimal_pres = 2
            
            # Variables values
            self.mod_vel = self.particle.mod_vel
            self.velx = round(self.particle.vel[0], self.decimal_pres)
            self.vely = round(self.particle.vel[1]*(-1), self.decimal_pres)
            self.pos = [self.particle.rect.x, self.particle.rect.y]
            self.angle = round(degrees(self.particle.angle), self.decimal_pres)
            
            self.radio = round(self.mass * self.mod_vel / (self.charge_value * self.B), self.decimal_pres)
            self.ang_vel = round((self.mod_vel / self.radio), self.decimal_pres)
            
        # Field base stats
        if field:
            self.particle=None
            
            self.field = field
            if self.field.type in ["left", "right", "up", "down"]:
                self.name = "Electric field"
                self.strength = self.field.E
            elif self.field.type in ["in", "out"]:
                self.name = "Magnetic field"
                self.strength = self.field.B
            
            self.pos = [self.field.square.x, self.field.square.y]
            self.type = self.field.type
 
    def draw_HUD_rect(self):
        pygame.draw.rect(self.game.display, "#3C3C3C", self.rect_ext)
        pygame.draw.rect(self.game.display, "#787878", self.rect_in)
    
    def show(self):
        self.draw_HUD_rect()
        
        size = 10
        color = "black"
        
        # First column
        sepx = 10
        x1 = self.rect_in.x + sepx
        sepy = 10
        y = self.rect_in.y + sepy
        offsety = 20
        
        # Second column
        x2 = x1 + (self.rect_ext.width*0.5)
        
        if self.particle:
            # First column: Constants
            self.draw_text(f"Particle: {self.name}", size, x1, y + offsety*0, color)
            self.draw_text(f"Mass: {self.mass}*10^-31 kg", size, x1, y + offsety*1, color)
            self.draw_text(f"Charge sign: {self.charge_sign}", size, x1, y + offsety*2, color)
            self.draw_text(f"Charge value: {self.charge_value}*10^-19 C", size, x1, y + offsety*3, color)
            self.draw_text(f"Velocity: {self.mod_vel:.3} m/s", size, x1, y + offsety*4, color)
            
            # Second Column: Variables
            self.draw_text(f"Position (x, y): ({self.pos[0]}, {self.pos[1]}) m", size, x2, y + offsety*0, color)
            self.draw_text(f"Velocity (vx, vy): ({self.velx}, {self.vely}) m/s", size, x2, y + offsety*1, color)
            self.draw_text(f"Angle: {self.angle}°", size, x2, y + offsety*2, color)
            self.draw_text(f"Radio: {self.radio} m", size, x2, y + offsety*3, color)
            self.draw_text(f"Angular velocity: {self.ang_vel} rad/s", size, x2, y + offsety*4, color)
        
        if self.field:
            # Constants
            self.draw_text(f"Field: {self.name}", size, x1, y + offsety*0, color)
            self.draw_text(f"Type: {self.type}", size, x1, y + offsety*1, color)
            if self.name == "Electric field":
                self.draw_text(f"E: {self.strength} V/m", size, x1, y + offsety*2, color)
            else:
                self.draw_text(f"B: {self.strength} T", size, x1, y + offsety*2, color)
            self.draw_text(f"Position (x, y): {self.pos[0], self.pos[1]} m", size, x1, y + offsety*3, color)
    
    def update(self, particle):
        self.particle=particle
        from math import degrees
        self.mod_vel = self.particle.mod_vel
        self.velx = round(self.particle.vel[0], self.decimal_pres)
        self.vely = round(self.particle.vel[1]*(-1), self.decimal_pres)
        self.pos = [self.particle.rect.x, self.particle.rect.y]
        self.angle = round(degrees(self.particle.angle), self.decimal_pres)
        
        self.radio = round(self.particle.radio, self.decimal_pres)
        self.ang_vel = round(self.particle.ang_vel, self.decimal_pres)
        
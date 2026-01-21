import pygame

from debug.debug import debug

class Menu:
    def __init__(self, game):
        self.game = game
    
    def draw_text(self, text, size, x, y, color):
        font = pygame.font.SysFont(self.game.font_name, size)
        
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(topleft = (x,y))
        
        self.game.display.blit(text_surf, text_rect)

class HUD(Menu):
    def __init__(self, game, pos, size):
        super().__init__(game)
        
        self.rect_ext = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.rect_in = pygame.Rect(pos[0] + 5, pos[1] + 5, size[0] - 10, size[1]- 10)

        self.size = 10
        self.color = "black"
        
        # First column
        self.sepx = 10
        self.x1 = self.rect_in.x + self.sepx
        self.sepy = 10
        self.y = self.rect_in.y + self.sepy
        self.offsety = 20
        
        # Second column
        self.x2 = self.x1 + (self.rect_ext.width*0.5)
        
    def draw_HUD_rect(self):
        pygame.draw.rect(self.game.display, "#3C3C3C", self.rect_ext)
        pygame.draw.rect(self.game.display, "#787878", self.rect_in)
        
class ParticleHUD(HUD):
    def __init__(self, game, pos, size, B, particle):
        super().__init__(game, pos, size)
        
        # Particle base stats

        # Constant values
        self.B = B
        
        self.particle = particle
        self.mass = self.particle.MASS
        self.charge_sign = self.particle.charge_sign
        self.charge_value = self.particle.CHARGE_VALUE
        if self.charge_sign == "+":
            self.name = "Proton"
        else:
            self.name = "Electron"
        
        self.decimal_pres = 2
        
        # Variables values in certain cases
        self.velx = round(self.particle.vel[0], self.decimal_pres)
        self.vely = round(self.particle.vel[1]*(-1), self.decimal_pres)
        
        # Electric field: tangencial acceleration (change vel)
        self.mod_vel = self.particle.mod_vel
        
        # Magnetic field: normal acceleration (change direction, vx, vy)
        from math import degrees
        self.angle = round(degrees(self.particle.angle), self.decimal_pres)
        self.radio = round(self.mass * self.mod_vel / (self.charge_value * self.B), self.decimal_pres)
        self.ang_vel = round((self.mod_vel / self.radio), self.decimal_pres)
        
        # Variables values
        self.pos = [self.particle.rect.x, self.particle.rect.y]
    
    def show_constants(self):
        text = [f"Particle: {self.name}", 
                f"Mass: {self.mass}*10^-31 kg", 
                f"Charge sign: {self.charge_sign}", 
                f"Charge value: {self.charge_value}*10^-19 C"]
        
        for i in range(len(text)):
            self.draw_text(text[i], self.size, self.x1, self.y + self.offsety*i, self.color)
    
    def show_variables(self):
        self.draw_text(f"Velocity: {self.mod_vel:.3} m/s", self.size, self.x1, self.y + self.offsety*4, self.color)
        self.draw_text(f"Position (x, y): ({self.pos[0]}, {self.pos[1]}) m", self.size, self.x2, self.y + self.offsety*0, self.color)
        self.draw_text(f"Velocity (vx, vy): ({self.velx}, {self.vely}) m/s", self.size, self.x2, self.y + self.offsety*1, self.color)
        self.draw_text(f"Angle: {self.angle}°", self.size, self.x2, self.y + self.offsety*2, self.color)
        self.draw_text(f"Radio: {self.radio} m", self.size, self.x2, self.y + self.offsety*3, self.color)
        self.draw_text(f"Angular velocity: {self.ang_vel} rad/s", self.size, self.x2, self.y + self.offsety*4, self.color)
        
    def show(self):
        self.draw_HUD_rect()
        
        # First column: Constants
        self.show_constants()
        # Second Column: Variables
        self.show_variables()

    def update(self, particle):
        self.particle=particle
        from math import degrees
        self.mod_vel = self.particle.mod_vel
        self.pos = [self.particle.rect.x, self.particle.rect.y]
        self.velx = round(self.particle.vel[0], self.decimal_pres)
        self.vely = round(self.particle.vel[1]*(-1), self.decimal_pres)
        self.angle = round(degrees(self.particle.angle), self.decimal_pres)
        
        self.radio = round(self.particle.radio, self.decimal_pres)
        self.ang_vel = round(self.particle.ang_vel, self.decimal_pres)
        
class FieldHUD(HUD):
    def __init__(self, game, pos, size, field):
        super().__init__(game, pos, size)
        
        # Field base stats
        self.field = field
        if self.field.type in ["left", "right", "up", "down"]:
            self.name = "Electric field"
            self.strength = self.field.E
        elif self.field.type in ["in", "out"]:
            self.name = "Magnetic field"
            self.strength = self.field.B
        
        self.pos = [self.field.square.x, self.field.square.y]
        self.type = self.field.type
    
    def show(self):
        self.draw_HUD_rect()
        
        # Constants
        self.draw_text(f"Field: {self.name}", self.size, self.x1, self.y + self.offsety*0, self.color)
        self.draw_text(f"Type: {self.type}", self.size, self.x1, self.y + self.offsety*1, self.color)
        if self.name == "Electric field":
            self.draw_text(f"E: {self.strength} V/m", self.size, self.x1, self.y + self.offsety*2, self.color)
        else:
            self.draw_text(f"B: {self.strength} T", self.size, self.x1, self.y + self.offsety*2, self.color)
        self.draw_text(f"Position (x, y): {self.pos[0], self.pos[1]} m", self.size, self.x1, self.y + self.offsety*3, self.color)
import pygame

class Object():
    def __init__(self, game):
        self.game = game
        
        self.run_display = True
    
    def blit_scren(self):
        self.game.window.blit(self.game.display1, (0,0))

        pygame.display.update()
        self.game.reset_keys()

# Fields
class Field(Object):
    def __init__(self, game, pos, size, type, strength):
        super().__init__(game)
        self.type = type
        self.strength = strength
        self.square = pygame.Rect(pos[0], pos[1], size[0], size[1])
        
class ElectricField(Field):
    def __init__(self, game, pos, size, type, strength):
        super().__init__(game, pos, size, type, strength)
        
        self.spacing = 30
        self.E = strength
    
    def draw(self):
        self.color = "#FFD700"
        
        self.arrow_length = 10
        self.arrow_size = 6
        self.arrow_spacing = 50
        pygame.draw.rect(self.game.display1, "white", self.square, 1)
        
        if self.type == "left" or self.type == "right":
            for y in range(self.square.top + 20, self.square.bottom, self.spacing):
                # Horizontal lines
                pygame.draw.line(self.game.display1, self.color, (self.square.left, y), (self.square.right, y), 2)
                
                # Arrow after a interval
                if self.type == "left":
                    for x in range(self.square.left + 20, self.square.right, self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_length, y - self.arrow_size), 2)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_length, y + self.arrow_size), 2)
                else:
                    for x in range(self.square.right - 20, self.square.left, -self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_length, y - self.arrow_size), 2)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_length, y + self.arrow_size), 2)
        elif self.type == "up" or self.type == "down":
            for x in range(self.square.left + 20, self.square.right, self.spacing):
                # Vertical lines
                pygame.draw.line(self.game.display1, self.color, (x, self.square.top), (x, self.square.bottom), 2)
                
                # Arrow after a interval
                if self.type == "up":
                    for y in range(self.square.top + 20, self.square.bottom, self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_size, y + self.arrow_length), 2)
                        pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_size, y + self.arrow_length), 2)
                else:
                    for y in range(self.square.bottom - 20, self.square.top, -self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_size, y - self.arrow_length), 2)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_size, y - self.arrow_length), 2)
    
class MagneticField(Field):
    def __init__(self, game, pos, size, type, strength):
        super().__init__(game, pos, size, type, strength)
        
        self.spacing = 60
        self.B = strength
        
    def draw(self):
        self.color_in =  "#9B30FF"
        self.color_out = "#00FFCC"
        pygame.draw.rect(self.game.display1, "white", self.square, 1)
    
        for y in range(self.square.top + 20, self.square.bottom, self.spacing):
            for x in range(self.square.left + 20, self.square.right, self.spacing):
                # Campo entrante (x)
                if self.type == "in":
                    pygame.draw.circle(self.game.display1, self.color_in, (x, y), 12, 1)
                    pygame.draw.line(self.game.display1, self.color_in, (x-4, y-4), (x+4, y+4), 2)
                    pygame.draw.line(self.game.display1, self.color_in, (x-4, y+4), (x+4, y-4), 2)
                # Campo saliente (·)
                else:
                    pygame.draw.circle(self.game.display1, self.color_out, (x, y), 12, 1)
                    pygame.draw.circle(self.game.display1, self.color_out, (x, y), 4)

# Particles
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
        self.vel0 = self.mod_vel
        self.angle = 0.0
        self.ang_vel = 0.05
        
        self.radio = 500
    
    def move(self):
        # Movement
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
        
        from math import pi
        if self.edge_collision():
            if self.rect.left < 0 or self.rect.right > self.game.DISPLAY_W:
                self.vel[0] = -self.vel[0]
                self.angle = pi - self.angle
            if self.rect.top < 0 or self.rect.bottom > (self.game.DISPLAY_H-280):
                self.vel[1] = -self.vel[1]
                self.angle = 2*pi - self.angle
        
        # Angle reset
        if self.angle > 2*pi:
            self.angle -= 2*pi
        if self.angle < -2*pi:
            self.angle += 2*pi
    
    def edge_collision(self):
        # Edge collision
        from math import pi
        if self.rect.left < 0 or self.rect.right > self.game.DISPLAY_W:
            return True
        if self.rect.top < 0 or self.rect.bottom > (self.game.DISPLAY_H-280):
            return True
        return False
            
    def reset_pos(self):
        # Set to initial position and velocity
        self.rect.x = self.pos0x
        self.rect.y = self.pos0y
        self.angle = 0.0
        self.radio = 0.0
        
        self.mod_vel = self.vel0
        self.vel = [self.vel0x, self.vel0y]

    def update_mod_vel(self):
        from math import sqrt
        self.mod_vel = sqrt(self.vel[0]**2 + self.vel[1]**2)

    def draw(self):
        if self.charge_sign == "+":
            self.color = "#FF4500"
        else:  
            self.color = "#1E90FF"
        pygame.draw.circle(self.game.display1, self.color, self.rect.center, 10)
    
    def eF_collision(self, e_field):
        if self.rect.colliderect(e_field.square):
            self.apply_e_force(e_field.type, e_field.E)
            return True
        return False
            
    # Electric Field
    def apply_e_force(self, type, E):
        acc = self.CHARGE_VALUE * E / self.MASS
        
        # before_vel = self.vel
        if type == "up":
            if self.charge_sign == "+":
                self.vel[1] -= acc
            else:
                self.vel[1] += acc
        if type == "down":
            if self.charge_sign == "+":
                self.vel[1] += acc
            else:
                self.vel[1] -= acc
        if type == "left":
            if self.charge_sign == "+":
                self.vel[0] -= acc
            else:
                self.vel[0] += acc
        if type == "right":
            if self.charge_sign == "+":
                self.vel[0] += acc
            else:
                self.vel[0] -= acc
                
        # after_vel = self.vel
        self.update_mod_vel()
            
    def mgF_collision(self, mg_field):
        if self.rect.colliderect(mg_field.square):
            return True
        return False
            
    # Magnetic Field
    def apply_mg_force(self, type, B):
        from math import sin, cos, atan2
        
        if B != 0:
            self.radio = self.MASS * self.mod_vel / (self.CHARGE_VALUE * B)
        if self.radio != 0:
            self.vel_ang = self.mod_vel / self.radio
        self.angle = atan2(self.vel[1], self.vel[0])
    
        if type == "out":
            if self.charge_sign == "+":
                self.angle += self.ang_vel
            elif self.charge_sign == "-":
                self.angle -= self.ang_vel
                
        if type == "in":
            if self.charge_sign == "+":
                self.angle -= self.ang_vel
            elif self.charge_sign == "-":
                self.angle += self.ang_vel
                

        self.vel[0] = self.mod_vel * cos(self.angle)
        self.vel[1] = self.mod_vel * sin(self.angle)
        
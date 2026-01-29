import pygame
import utils.vector as vector

class Object():
    def __init__(self, game):
        self.game = game
        
        self.run_display = True
        
        self.scale = 1
    
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
        
        
        self.square = pygame.Rect(pos[0], pos[1], size[0] * self.scale, size[1] * self.scale)
        
        self.edge_color = "#E3F2FD"
        
class ElectricField(Field):
    def __init__(self, game, pos, size, type, strength):
        super().__init__(game, pos, size, type, strength)
        
        self.line_spacing = 32 * self.scale
        self.E = strength
    
    def draw(self):
        self.color = "#FFD700"
        
        self.offset = 24 * self.scale
        self.arrow_length = 10 * self.scale
        self.arrow_size = 6 * self.scale
        self.arrow_spacing = 50 * self.scale
        
        self.line_width = 2
        self.square_width = 1
        pygame.draw.rect(self.game.display1, self.edge_color, self.square, self.square_width)
        
        if self.type == "left" or self.type == "right":
            for y in range(self.square.top + self.offset, self.square.bottom, self.line_spacing):
                # Horizontal lines
                pygame.draw.line(self.game.display1, self.color, (self.square.left, y), (self.square.right, y), self.line_width)
                
                # Arrow
                if self.type == "left":
                    for x in range(self.square.left + self.offset, self.square.right, self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_length, y - self.arrow_size), self.line_width)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_length, y + self.arrow_size), self.line_width)
                else:
                    for x in range(self.square.right - self.offset, self.square.left, -self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_length, y - self.arrow_size), self.line_width)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_length, y + self.arrow_size), self.line_width)
        elif self.type == "up" or self.type == "down":
            for x in range(self.square.left + self.offset, self.square.right, self.line_spacing):
                # Vertical lines
                pygame.draw.line(self.game.display1, self.color, (x, self.square.top), (x, self.square.bottom), self.line_width)
                
                # Arrow
                if self.type == "up":
                    for y in range(self.square.top + self.offset, self.square.bottom, self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_size, y + self.arrow_length), self.line_width)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_size, y + self.arrow_length), self.line_width)
                else:
                    for y in range(self.square.bottom - self.offset, self.square.top, -self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_size, y - self.arrow_length), self.line_width)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_size, y - self.arrow_length), self.line_width)
    
class MagneticField(Field):
    def __init__(self, game, pos, size, type, strength):
        super().__init__(game, pos, size, type, strength)
        
        self.B = strength
        
        self.circle_r = 12 * self.scale
        self.offset = int((self.square.width - 4*self.circle_r) / 3) + self.circle_r
        self.spacing = (self.offset + self.circle_r)
        
        self.in_r = 4 * self.scale
        
    def draw(self):
        self.color_in =  "#9B30FF"
        self.color_out = "#00FFCC"
        pygame.draw.rect(self.game.display1, self.edge_color, self.square, 1)
    
        for y in range(self.square.top + self.offset, self.square.bottom, self.spacing):
            for x in range(self.square.left + self.offset, self.square.right, self.spacing):
                # Campo entrante (x)
                if self.type == "in":
                    pygame.draw.circle(self.game.display1, self.color_in, (x, y), self.circle_r, 1)
                    pygame.draw.line(self.game.display1, self.color_in, (x-4 * self.scale, y-4 * self.scale), (x+4 * self.scale, y+4 * self.scale), 2)
                    pygame.draw.line(self.game.display1, self.color_in, (x-4 * self.scale, y+4 * self.scale), (x+4 * self.scale, y-4 * self.scale), 2)
                # Campo saliente (·)
                else:
                    pygame.draw.circle(self.game.display1, self.color_out, (x, y), self.circle_r, 1)
                    pygame.draw.circle(self.game.display1, self.color_out, (x, y), self.in_r)









# Particles
class Particle(Object):
    def __init__(self, game, pos, vel, charge_sign):
        super().__init__(game)
        
        self.MASS = 9.11
        self.CHARGE_VALUE = 1.602
        self.charge_sign = charge_sign
        
        self.pos0x = pos[0]
        self.pos0y = pos[1]
        self.pos = [self.pos0x, self.pos0y]
        
        self.rect = pygame.Rect(self.pos0x, self.pos0y, 10, 10)
        
        self.vel0x = vel[0]
        self.vel0y = vel[1]
        self.vel = [vel[0], vel[1]]
        from math import sqrt
        self.mod_vel = sqrt(vel[0]**2+vel[1]**2)
        self.vel0 = self.mod_vel
        self.angle = 0.0
        self.ang_vel = 2.5
        
        self.radius = 500
    
    def move(self, dt):
        # Movement
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt
        
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        
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
        
    def draw_circular_trajectory(self, type):
        # Vector direction
        if self.charge_sign == "+":
            if type == "out": # proton + in
                dir = "+"
            elif type == "in":
                dir = "-"
        if self.charge_sign == "-":
            if type == "out": # proton + in
                dir = "-"
            elif type == "in":
                dir = "+"
                
        n_hat = vector.norm_perpen(self.vel, dir)
        cx = self.rect.centerx - self.radius * n_hat[0]
        cy = self.rect.centery - self.radius * n_hat[1]

        pygame.draw.circle(self.game.display1, "white", (cx, cy), self.radius, 1)
    
    def edge_collision(self):
        # Edge collision
        from math import pi
        if self.rect.left < 0 or self.rect.right > self.game.DISPLAY_W:
            return True
        if self.rect.top < 0 or self.rect.bottom > (self.game.DISPLAY_H-260):
            return True
        return False
            
    def reset_pos(self):
        # Set to initial position and velocity
        self.rect.x = self.pos0x
        self.rect.y = self.pos0y
        self.pos = [self.pos0x, self.pos0y]
        self.angle = 0.0
        self.radius = 0.0
        
        self.mod_vel = self.vel0
        self.vel = [self.vel0x, self.vel0y]

    def update_mod_vel(self):
        from math import sqrt
        self.mod_vel = sqrt(self.vel[0]**2 + self.vel[1]**2)

    def draw(self):
        self.line_length = 4 * self.scale
        self.line_thighness = 2 * self.scale
        self.circle_r = 8 * self.scale
        if self.charge_sign == "+":
            self.color = "#FF4500"
            self.color1 = "#8B0000"
            pygame.draw.circle(self.game.display1, self.color, self.rect.center, self.circle_r)
            pygame.draw.line(self.game.display1, self.color1, (self.rect.centerx - self.line_length, self.rect.centery), (self.rect.centerx + self.line_length, self.rect.centery), self.line_thighness)
            pygame.draw.line(self.game.display1, self.color1, (self.rect.centerx, self.rect.centery - self.line_length), (self.rect.centerx, self.rect.centery + self.line_length), self.line_thighness)
        else:  
            self.color = "#1E90FF"
            self.color1 = "#0000CD"
            pygame.draw.circle(self.game.display1, self.color, self.rect.center, self.circle_r)
            pygame.draw.line(self.game.display1, self.color1, (self.rect.centerx - self.line_length, self.rect.centery), (self.rect.centerx + self.line_length, self.rect.centery), self.line_thighness)
            
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
            
    def mgF_collision(self, mg_field, dt):
        if self.rect.colliderect(mg_field.square):
            self.apply_mg_force(mg_field.type, mg_field.B, dt)
            return True
        return False
            
    # Magnetic Field
    def apply_mg_force(self, type, B, dt):
        from math import sin, cos, atan2
        
        if B != 0:
            self.radius = self.MASS * self.mod_vel / (self.CHARGE_VALUE * B)
        if self.radius != 0:
            self.ang_vel = self.CHARGE_VALUE * B / self.MASS
        self.angle = atan2(self.vel[1], self.vel[0])
    
        if type == "out":
            if self.charge_sign == "+":
                self.angle -= self.ang_vel * dt
            elif self.charge_sign == "-":
                self.angle += self.ang_vel * dt
                
        if type == "in":
            if self.charge_sign == "+":
                self.angle += self.ang_vel * dt
            elif self.charge_sign == "-":
                self.angle -= self.ang_vel * dt
        
        self.vel[0] = self.mod_vel * cos(self.angle)
        self.vel[1] = self.mod_vel * sin(self.angle)
        
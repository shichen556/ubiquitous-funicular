import pygame

# Allow autocomplete in circular import (AI)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    
class Menu:
    def __init__(self, game: "Game"):
        self.game = game
        
        self.mid_w = self.game.DISPLAY_W/2
        self.mid_h = self.game.DISPLAY_H/2
        
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offsetx = -int(self.game.DISPLAY_W*0.2)

        self.SIZE = int(self.game.DISPLAY_H * 0.1)
        self.TXT_SIZE = int(self.SIZE*0.8)
        
    def draw_cursor(self):
        self.game.draw_text("->", int(self.SIZE*0.4), self.cursor_rect.x, self.cursor_rect.y, self.game.TXT_COLOR)
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Start"
        
        SEP = 30
        OFFSET = int(self.game.DISPLAY_H*0.1)
        
        self.startx, self.starty = self.mid_w, self.mid_h + SEP + 0*OFFSET
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + SEP + 1*OFFSET
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + SEP + 2*OFFSET
        self.exitx, self.exity = self.mid_w, self.mid_h + SEP + 3*OFFSET
        self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty)
        
    def display_menu(self):
        self.run_display = True
        
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Main Menu", self.SIZE, self.mid_w, self.mid_h - int(self.game.DISPLAY_H*0.2), self.game.TITLE_COLOR)
            self.game.draw_text("Start Game", self.TXT_SIZE, self.startx, self.starty, self.game.MENU_COLOR[int(self.state == "Start")])
            self.game.draw_text("Options", self.TXT_SIZE, self.optionsx, self.optionsy, self.game.MENU_COLOR[int(self.state == "Options")])
            self.game.draw_text("Credits", self.TXT_SIZE, self.creditsx, self.creditsy, self.game.MENU_COLOR[int(self.state == "Credits")])
            self.game.draw_text("Exit", self.TXT_SIZE, self.exitx, self.exity, self.game.MENU_COLOR[int(self.state == "Exit")])
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offsetx, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditsx + self.offsetx, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.exitx + self.offsetx, self.exity)
                self.state = "Exit"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Exit":
                self.cursor_rect.midtop = (self.creditsx + self.offsetx, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionsx + self.offsetx, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty)
                self.state = "Start"
            elif self.state == "Start":
                self.cursor_rect.midtop = (self.exitx + self.offsetx, self.exity)
                self.state = "Exit"
    
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                self.game.curr_menu = self.game.options
            elif self.state == "Credits":
                self.game.curr_menu = self.game.credits
            elif self.state == "Exit":
                self.game.running = False
            self.run_display = False
            
class OptionsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Volume"
        
        SEP = 20
        OFFSET = int(self.game.DISPLAY_H*0.1)
        
        self.volx, self.voly = self.mid_w, self.mid_h + SEP + 0*OFFSET
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + SEP + 1*OFFSET
        self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Options", self.SIZE, self.mid_w, self.mid_h - int(self.game.DISPLAY_H*0.2), self.game.TITLE_COLOR)
            self.game.draw_text("Volume", self.TXT_SIZE, self.volx, self.voly, self.game.MENU_COLOR[int(self.state == "Volume")])
            self.game.draw_text("Controls", self.TXT_SIZE, self.controlsx, self.controlsy, self.game.MENU_COLOR[int(self.state == "Controls")])
            self.draw_cursor()
            self.blit_screen()
    
    def check_inputs(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Volume":
                self.cursor_rect.midtop = (self.controlsx + self.offsetx, self.controlsy)
                self.state = "Controls"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly)
                self.state = "Volume"
        elif self.game.START_KEY:
            # TODO: Create a volume menu and a controls menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Credits", self.SIZE, self.mid_w, self.mid_h - int(self.game.DISPLAY_H*0.2), self.game.TITLE_COLOR)
            self.game.draw_text("Made by CDcodes", self.TXT_SIZE, self.mid_w, self.mid_h + 10, self.game.TXT_COLOR)
            self.blit_screen()

class GameMenu(Menu):
    def __init__(self, game, pos, size, B, particle=None, field=None):
        super().__init__(game)
        
        self.rect_ext = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.rect_in = pygame.Rect(pos[0] + 5, pos[1] + 5, size[0] - 10, size[1]- 10)
        
        # Particle base stats
        if particle:
            from math import degrees
            self.particle = particle
            self.mass = self.particle.MASS
            self.charge_sign = self.particle.charge_sign
            self.charge_value = self.particle.CHARGE_VALUE
            if self.charge_sign == "+":
                self.name = "Proton"
            else:
                self.name = "Electron"
            
            decimal_pres = 2
            self.mod_vel = self.particle.mod_vel
            self.velx = round(self.particle.vel[0], decimal_pres)
            self.vely = round(self.particle.vel[1]*(-1), decimal_pres)
            self.pos = [self.particle.rect.x, self.particle.rect.y]
            self.angle = round(degrees(self.particle.angle), decimal_pres)
            
            self.radio = round(self.mass * self.mod_vel / (self.charge_value * B), decimal_pres)
            self.ang_vel = round((self.mod_vel / self.radio), decimal_pres)
            
        self.B = B
        
        # Field base stats
        if field:
            self.field = field
    
    def draw_text(self, text, size, x, y, color):
        font = pygame.font.SysFont(self.game.font_name, size)
        
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(topleft = (x,y))
        
        self.game.display.blit(text_surf, text_rect)
        
    def show(self):
        pygame.draw.rect(self.game.display, "#3C3C3C", self.rect_ext)
        pygame.draw.rect(self.game.display, "#787878", self.rect_in)
        
        # First column
        sepx = 10
        x1 = self.rect_in.x + sepx
        sepy = 10
        y = self.rect_in.y + sepy
        offsety = 20
        size = 10
        color = "black"
        
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
            
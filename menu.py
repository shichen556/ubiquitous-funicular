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
        self.offsetx = -75
    
    def draw_cursor(self):
        self.game.draw_text("->", 15, self.cursor_rect.x, self.cursor_rect.y)
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Start"
        
        SEP = 30
        OFFSET = 30
        
        self.startx, self.starty = self.mid_w, self.mid_h + SEP + 0*OFFSET
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + SEP + 1*OFFSET
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + SEP + 2*OFFSET
        self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Main Menu", 20, self.mid_w, self.mid_h - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
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
                self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offsetx, self.creditsy)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionsx + self.offsetx, self.optionsy)
                self.state = "Options"
    
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                self.game.curr_menu = self.game.options
            elif self.state == "Credits":
                self.game.curr_menu = self.game.credits
            self.run_display = False
    
class OptionsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Options", 20, self.mid_w, self.mid_h - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
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
            self.game.draw_text("Credits", 20, self.mid_w, self.mid_h - 20)
            self.game.draw_text("Made by CDcodes", 15, self.mid_w, self.mid_h + 10)
            self.blit_screen()
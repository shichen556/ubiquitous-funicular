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
        self.offsetx = -100
    
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
        self.state_list = ["Start", "Options", "Credits"]
        self.state_dic = {}
        
        SEP = 30
        OFFSET = 20
        
        # Initialize dic
        for i in range(len(self.state_list)):
            self.state_dic[self.state_list[i]] = (self.mid_w, self.mid_w + SEP + i*OFFSET)

        self.cursor_rect.midtop = (self.state_dic["Start"][0] + self.offsetx, self.state_dic["Start"][1])
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            
            self.game.display.fill(self.game.BG_COLOR)
            
            self.game.draw_text("Main Menu", 20, self.mid_w, self.mid_h -20)
            for menu_state in self.state_dic:
                self.game.draw_text(menu_state, 20, menu_state[0], menu_state[1])
            
            self.draw_cursor()
            self.blit_screen()
    
    def search(self, state):
        for i in range(len(self.state_list) - 1):
            if state == self.state_list[i]:
                return i
        return 0
    
    def move_cursor(self):
        n = self.search(self.state)
        
        if self.game.DOWN_KEY:
            self.cursor_rect.midtop = (self.state_dic[self.state_list[n + 1]][0] + self.offsetx, self.state_dic[self.state_list[n + 1]][1])
            self.state = self.state_dic[self.state_list[n + 1]]
        elif self.game.UP_KEY:
            self.cursor_rect.midtop = (self.state_dic[self.state_list[n - 1]][0] + self.offsetx, self.state_dic[self.state_list[n - 1]][1])
            self.state = self.state_dic[self.state_list[n - 1]]
    
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
        
        self.state

class CreditsMenu(Menu):
    pass
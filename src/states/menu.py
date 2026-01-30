import pygame
from states.state import State

from debug.debug import debug

class Menu(State):
    def __init__(self, game):
        super().__init__(game)
        
        self.mid_w = self.game.DISPLAY_W/2
        self.mid_h = self.game.DISPLAY_H/2
        
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offsetx = -int(self.game.DISPLAY_W*0.2)

        self.SIZE = int(self.game.DISPLAY_H * 0.1)
        self.TXT_SIZE = int(self.SIZE*0.8)
        
    def draw_cursor(self):
        self.game.draw_text("->", int(self.SIZE*0.4), self.cursor_rect.x, self.cursor_rect.y, self.game.TXT_COLOR)
    
    def move_cursor(self):
        if self.game.actions["down"]:
            self.state_index = (self.state_index + 1) % len(self.menu_options)
        elif self.game.actions["up"]:
            self.state_index = (self.state_index - 1) % len(self.menu_options)
            
        self.cursor_rect.x = self.menu_options_pos[self.state_index][0] + self.offsetx
        self.cursor_rect.y = self.menu_options_pos[self.state_index][1]
        
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state_index = 0
        self.menu_options = {0: "Resume", 1: "Options", 2: "Credits", 3: "Exit"}
        
        SEP = 30
        OFFSET = int(self.game.DISPLAY_H*0.1)
        
        self.menu_options_pos = {}
        for i in range(len(self.menu_options)):
            self.menu_options_pos[i] = (self.mid_w, self.mid_h + SEP + i*OFFSET)

        self.cursor_rect.midtop = (self.menu_options_pos[0][0] + self.offsetx, self.menu_options_pos[0][1])
        
    def display_menu(self):
        self.run_display = True
        
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Main Menu", self.SIZE, self.mid_w, self.mid_h - int(self.game.DISPLAY_H*0.2), self.game.TITLE_COLOR)
            for i in range(len(self.menu_options)):
                text = self.menu_options[i]
                posx = self.menu_options_pos[i][0]
                posy = self.menu_options_pos[i][1]
                hover_color = self.game.MENU_COLOR[int(self.state_index == i)]
                
                self.game.draw_text(text, self.TXT_SIZE, posx, posy, hover_color)
            self.draw_cursor()
            
            debug(f"{self.game.clock.get_fps():.2f}", self.game.display) 
            self.game.clock.tick(self.game.FPS)
            self.blit_screen()
        
    def check_input(self):
        self.move_cursor()
        if self.game.actions["start"]:
            if self.state_index == 0:
                self.game.playing = True
            elif self.state_index == 1:
                self.game.curr_menu = self.game.options
            elif self.state_index == 2:
                self.game.curr_menu = self.game.credits
            elif self.state_index == 3:
                self.game.running = False
            self.run_display = False
    
    def transition_state(self):
        if self.menu_options[self.state_index] == "Resume":
            new_state = ""
            new_state.enter_state()
        elif self.menu_options[self.state_index] == "Options":
            pass
        elif self.menu_options[self.state_index] == "Credits":
            pass
        elif self.menu_options[self.state_index] == "Exit":
            self.game.running = False
        


class CreditsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.actions["start"] or self.game.actions["back"]:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Credits", self.SIZE, self.mid_w, self.mid_h - int(self.game.DISPLAY_H*0.2), self.game.TITLE_COLOR)
            self.game.draw_text("Made by CDcodes", self.TXT_SIZE, self.mid_w, self.mid_h + 10, self.game.TXT_COLOR)
            self.blit_screen()
            
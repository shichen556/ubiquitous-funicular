import pygame
from menu import Menu

class Options(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state_index = 0
        self.menu_options = {0: "Volume", 1: "Controls"}
        
        SEP = 20
        OFFSET = int(self.game.DISPLAY_H*0.1)
        
        self.menu_options_pos = {}
        for i in range(len(self.menu_options)):
            self.menu_options_pos[i] = (self.mid_w, self.mid_h + SEP + i*OFFSET)

        self.cursor_rect.midtop = (self.menu_options_pos[0][0] + self.offsetx, self.menu_options_pos[0][1])
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            self.game.display.fill(self.game.BG_COLOR)
            self.game.draw_text("Options", self.SIZE, self.mid_w, self.mid_h - int(self.game.DISPLAY_H*0.2), self.game.TITLE_COLOR)
            for i in range(len(self.menu_options)):
                text = self.menu_options[i]
                posx = self.menu_options_pos[i][0]
                posy = self.menu_options_pos[i][1]
                hover_color = self.game.MENU_COLOR[int(self.state_index == i)]
                
                self.game.draw_text(text, self.TXT_SIZE, posx, posy, hover_color)
            self.draw_cursor()
            self.blit_screen()
            
    def check_inputs(self):
        self.move_cursor()
        if self.game.actions["back"]:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        
        elif self.game.actions["start"]:
            # TODO: Create a screensize menu
            pass
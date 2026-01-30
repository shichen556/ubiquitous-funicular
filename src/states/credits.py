from menu import Menu

class Credits(Menu):
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
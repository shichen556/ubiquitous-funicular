import pygame
from states.state import State

class PauseMenu(State):
    def __init__(self, game):
        super().__init__(game)
        
        self.mid_width = self.game.DISPLAY_W / 2
        self.mid_height = self.game.DISPLAY_H / 2
        self.menu_rect = pygame.rect.Rect(self.mid_width, 10, 10, 10)
        
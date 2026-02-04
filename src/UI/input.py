import pygame
import pygame_widgets

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

class Control:
    def __init__(self, surf: pygame.Surface, pos: tuple[int], size: tuple[int] , min: float, max: float, step: float, initial: float) -> None:
        self.surf = surf
        self.pos = pos
        self.size = size
        self.min = min
        self.max = max
        self.step = step
        self.initial = initial
        
        self.slider = Slider(self.surf, self.pos[0], self.pos[1], self.size[0], self.size[1], min=self.min, max=self.max, step=self.step, initial=self.initial)
        self.slider.disable() # Act as label instead of textbox

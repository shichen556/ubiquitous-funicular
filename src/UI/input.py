import pygame
import pygame_widgets

from pygame_widgets.textbox import TextBox

class Control:
    def __init__(self, surf: pygame.Surface, pos: tuple[int], size: tuple[int], on_submit, placeholder_text: str = "") -> None:
        self.surf = surf
        self.pos = pos
        self.size = size
        self.on_submit = on_submit
        self.placeholder_text = placeholder_text
        
        self.font_size = 20
        self.border_color = "black"
        self.text_color = "black"
        self.radius = 10
        self.border_thickness = 5
        
        self.textbox = TextBox(self.surf, 
                          pos[0], pos[1], 
                          size[0], size[1], 
                          fontSize=self.font_size, 
                          borderColour=self.border_color, 
                          textColour=self.text_color, 
                          onSubmit=self.on_submit,
                          radius=self.radius,
                          borderThickness=self.border_thickness,
                          placeholderText=self.placeholder_text)
        
    def run(self):
        events = pygame.event.get()
        pygame_widgets.update(events)

import pygame

from pygame_widgets.textbox import TextBox

class Control:
    def __init__(self, surf: pygame.Surface, pos: tuple[int], size: tuple[int], placeholder_text: str = ""):
        self.surf = surf
        self.pos = pos
        self.size = size
        self.placeholder_text = placeholder_text
        
        self.font_size = 20
        self.border_color = "red"
        self.text_color = "green"
        self.radius = 10
        self.border_thickness = 5
        
        self.textbox = TextBox(self.surf, 
                          pos[0], pos[1], 
                          size[0], size[1], 
                          fontSize=self.font_size, 
                          borderColour=self.border_color, 
                          textColour=self.text_color, 
                          onSubmit=self.output,
                          radius=self.radius,
                          borderThickness=self.border_thickness,
                          placeholderText=self.placeholder_text)
    
    def output(self):
            print(self.textbox.getText())

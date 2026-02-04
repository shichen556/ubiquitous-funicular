import pygame
import pygame_widgets

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()
win = pygame.display.set_mode((1000, 600))

slider1 = Slider(win, 100, 100, 800, 40, min=0, max=99, step=1, initial=0)
output1 = TextBox(win, 475, 150, 60, 60, fontSize=30)

slider2 = Slider(win, 100, 220, 100, 40, min=0, max=99, step=1, initial=0)
output2 = TextBox(win, 475, 280, 60, 60, fontSize=30)

slider3 = Slider(win, 100, 350, 400, 400, min=0, max=99, step=1, initial=0)
output3 = TextBox(win, 475, 400, 60, 60, fontSize=30)

output1.disable()  # Act as label instead of textbox
output2.disable()  # Act as label instead of textbox
output3.disable()  # Act as label instead of textbox

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))

    output1.setText(slider1.getValue())
    output2.setText(slider2.getValue())
    output3.setText(slider3.getValue())
    
    pygame_widgets.update(events)
    pygame.display.update()

pygame.quit()
import pygame
from sys import exit

def load_font(x, y, text=None, font_type=None, font_size=50):
    # Load and render font
    if text is None and font_type is not None:
        font = pygame.font.Font(f"assets/font/{font_type}.ttf", font_size)
        font_surf = font.render(font_type, True, "Black")    

    else:
        font = pygame.font.Font(f"assets/font/{font_type}.ttf", font_size)
        font_surf = font.render(text, True, "Black")
        
    font_rect = font_surf.get_rect(center = (x, y))
    
    return (font_surf, font_rect)

def display_text(x, y, text=None, font_type=None, font_size=50):
    # load and render font
    font = load_font(x, y, text, font_type, font_size)
    
    # display font
    screen.blit(font[0], font[1]) # surf, rect
    
# Initialize pygame
pygame.init()

# Set up pygame screen
WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")

# Framerate control
clock = pygame.time.Clock()

# Menu buttons setup



# In-game features
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event_type == MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                # Start the game
                pass
            elif editor_button_rect.collidepoint(event.pos):
                # Open the editor
                pass
            elif tutorial_button_rect.collidepoint(event.pos):
                # Open the tutorial
                pass
            elif options_button_rect.collidepoint(event.pos):
                # Open options menu
                pass
            elif credits_button_rect.collidepoint(event.pos):
                # Show credits
                pass
            elif exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()
    
    # Background color
    screen.fill((94,129,162))
    
    # Text display
    
    # Principal menu
    central_pos_x = WIDTH / 2
    
    # Game title
    display_text(central_pos_x, 50, "My game", "Exo2-Regular")
    
    # Menu options
    menu_options = ["Play", "Editor", "Tutorial", "Options", "Credits", "Exit"]
    
    for i in range(len(menu_options)):
        display_text(central_pos_x, 250 + 80*i, menu_options[i], "Lato-Regular")
    
    # Update screen
    pygame.display.update()
    clock.tick(60) # Frame ceiling
    
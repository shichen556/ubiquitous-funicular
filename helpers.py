import pygame

def load_font(x, y, text=None, font_type=None, font_size=50):
    if text is None and font_type is not None:
        font = pygame.font.Font(f"assets/font/{font_type}.ttf", font_size)
        font_surf = font.render(font_type, True, "Black")    
    
    elif text is not None and font_type is None:
        font = pygame.font.Font(font_type, font_size)
        font_surf = font.render("The quick brown fox jumps over the lazy dog", True, "Black")
    
    else:
        font = pygame.font.Font(f"assets/font/{font_type}.ttf", font_size)
        font_surf = font.render(text, True, "Black")
    font_rect = font_surf.get_rect(center = (x, y))
    
    return (font_surf, font_rect)
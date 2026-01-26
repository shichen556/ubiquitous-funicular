import pygame
pygame.init()
font = pygame.font.Font(None, 20)
    
def debug(info, display_surf, y = 20, x = 20):
    debug_surf = font.render(str(info), True, "white")
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    
    pygame.draw.rect(display_surf, "black", debug_rect)
    display_surf.blit(debug_surf, debug_rect)
    
import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x,y,width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont("Tahoma", 50)
        self.color = "#00BFFF"
        self.hover_color = "#2A3B7A"
        self.is_hovered = False

    def draw(self, screen):
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.color
        
        pygame.draw.rect(screen, color, self.rect)
        text_surf = self.font.render(self.text, True, "#FFFFFF")
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.action() # Ejecutar la accion asociada al boton
            elif event.type == pygame.MOUSEMOTION:
                self.is_hovered = self.rect.collidepoint(event.pos)
        
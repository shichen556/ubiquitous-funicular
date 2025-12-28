import pygame

class ElectricField:
    def __init__(self, rect, spacing=50):
        self.rect=rect
        self.spacing=spacing
        self.color="#FFD700"
    
    def draw(self, screen):
        area_subsurf = screen.subsurface(self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 1)
        
        width, height = area_subsurf.get_size()
    
        arrow_length = 20
        arrow_size = 6

        for y in range(self.spacing//2, height, self.spacing):
            # Horizontal lines
            pygame.draw.line(area_subsurf, self.color, (0,y), (width, y), 2)
            
            # Arrow after a interval
            for x in range(0, width, 100):
                pygame.draw.line(area_subsurf, self.color,
                                (x, y),
                                (x + arrow_length, y - arrow_size), 2)
                pygame.draw.line(area_subsurf, self.color,
                                (x, y),
                                (x + arrow_length, y + arrow_size), 2)

class MagneticField:
    def __init__(self, rect, field_type="out", spacing=60):
        self.rect=rect
        self.field_type=field_type
        if field_type == "out":
            self.color = "#00FFCC"
        else:
            self.color = "#9B30FF"
    
    def draw(self, screen):
        area_subsurf = screen.subsurface(self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 1)
        
        for y in range(self.rect.top + 20, self.rect.bottom, self.spacing):
            for x in range(self.rect.left + 20, self.rect.right, self.spacing):
                if self.field_type=="out":
                    # Campo saliente (·)
                    pygame.draw.circle(area_subsurf, self.color, (x, y), 12, 1)
                    pygame.draw.circle(area_subsurf, self.color, (x, y), 4)
                elif self.field_type=="in":
                    # Campo entrante (x)
                    pygame.draw.circle(screen, self.color, (x, y), 12, 1)
                    pygame.draw.line(screen, self.color, (x-4, y-4), (x+4, y+4), 2)
                    pygame.draw.line(screen, self.color, (x-4, y+4), (x+4, y-4), 2)
import pygame
import ctypes

def draw(self):
        self.color = "#FFD700"
        
        self.arrow_length = 10
        self.arrow_size = 6
        self.arrow_spacing = 50
        pygame.draw.rect(self.game.display1, self.edge_color4, self.square, 1)
        
        if self.type == "left" or self.type == "right":
            for y in range(self.square.top + 20, self.square.bottom, self.spacing):
                # Horizontal lines
                pygame.draw.line(self.game.display1, self.color, (self.square.left, y), (self.square.right, y), 2)
                
                # Arrow after a interval
                if self.type == "left":
                    for x in range(self.square.left + 20, self.square.right, self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_length, y - self.arrow_size), 2)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_length, y + self.arrow_size), 2)
                else:
                    for x in range(self.square.right - 20, self.square.left, -self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_length, y - self.arrow_size), 2)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_length, y + self.arrow_size), 2)
        elif self.type == "up" or self.type == "down":
            for x in range(self.square.left + 20, self.square.right, self.spacing):
                # Vertical lines
                pygame.draw.line(self.game.display1, self.color, (x, self.square.top), (x, self.square.bottom), 2)
                
                # Arrow after a interval
                if self.type == "up":
                    for y in range(self.square.top + 20, self.square.bottom, self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_size, y + self.arrow_length), 2)
                        pygame.draw.line(self.game.display, self.color, (x,y), (x + self.arrow_size, y + self.arrow_length), 2)
                else:
                    for y in range(self.square.bottom - 20, self.square.top, -self.arrow_spacing):
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x - self.arrow_size, y - self.arrow_length), 2)
                        pygame.draw.line(self.game.display1, self.color, (x,y), (x + self.arrow_size, y - self.arrow_length), 2)
                        
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

scalex, scaley = 0.6, 0.8
WIDTH, HEIGHT = user32.GetSystemMetrics(0) * scalex, user32.GetSystemMetrics(1) * scaley

mid_w = WIDTH / 2
mid_h = HEIGHT / 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")



pygame.image.save(screen, "proton.png")
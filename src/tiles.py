import pygame

class Tile:
    def __init__(self, game):
        self.game = game
        
        self.tile_size = 16
        self.offset = 2
        self.color = "#E3F2FD"
        
    def draw(self, x, y):
        pygame.draw.line(self.game.display1, self.color, (x,y), (x+self.offset, y))
        pygame.draw.line(self.game.display1, self.color, (x,y), (x+self.offset, y))
        
        pygame.draw.line(self.game.display1, self.color, (x,y), (x))

class TileMap(Tile):
    def __init__(self, game):
        super().__init__(game)
        
    def draw_map(self):
        for x in range(0, self.game.DISPLAY_W, self.tile_size):
            for y in range(0, self.game.DISPLAY_H2, self.tile_size):
                self.draw(x,y)
                
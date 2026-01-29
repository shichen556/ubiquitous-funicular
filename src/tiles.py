import pygame

class Tile:
    def __init__(self, game):
        self.game = game
        
        self.tile_size = 16
        self.length = 2
        self.color = "#E3F2FD"
        
    def draw(self, pos):
        pygame.draw.line(self.game.display1, self.color, (pos[0] - self.length, pos[1]), (pos[0] + self.length, pos[1]))
        pygame.draw.line(self.game.display1, self.color, (pos[0], pos[1] - self.length), (pos[0], pos[1] + self.length))

class TileMap(Tile):
    def __init__(self, game):
        super().__init__(game)
        
    def draw_map(self):
        for x in range(0, self.game.DISPLAY_W, self.tile_size):
            for y in range(0, self.game.DISPLAY_H2, self.tile_size):
                self.draw((x, y))
                
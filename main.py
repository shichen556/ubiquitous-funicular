"""
Chapuzada por ChatGPT y Copilot
"""

import pygame
from game import Game
from scenes import MenuScene

def main():
    pygame.init()
    game = Game()
    game.change_scene(MenuScene(game))
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
from game import Game
from scenes import MenuScene, PlayScene

def main():
    pygame.init()
    
    game=Game(900,700)
    
    game.change_scene(MenuScene(game))
    
    while game.running:
        game.run()
    
    pygame.quit()

if __name__ == "__main__":
    main()
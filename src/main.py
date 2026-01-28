import pygame
from game import Game

def main():
    g=Game()
    
    while g.running:
        if not g.playing:
            g.curr_menu.display_menu()
        else: 
            g.game_loop()
    
    pygame.image.save(g.window, "img.png")
    pygame.quit()
    
if __name__ == "__main__":
    main()
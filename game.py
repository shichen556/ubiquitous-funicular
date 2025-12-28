import pygame

class Game:
    def __init__(self, width, height):
        # Set up pygame screen
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Runner")
        
        # Framerate control
        self.running = True
        self.clock = pygame.time.Clock()
        self.scene = None
    
    def change_scene(self, new_scene):
        self.current_scene = new_scene
    
    def run(self):
        events = pygame.event.get()
        
        self.current_scene.handle_events(events)
        
        dt = pygame.time.get_ticks() / 1000
        self.current_scene.update(dt)
        
        self.current_scene.draw(self.screen)
        
        pygame.display.update()
        self.clock.tick(60)
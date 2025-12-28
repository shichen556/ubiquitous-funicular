import pygame

class Game:
    def __init__(self, width=900, height=700):
        # Set up pygame screen
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Runner")
        
        # Framerate control
        self.running = True
        self.clock = pygame.time.Clock()
        self.current_scene = None
    
    def change_scene(self, new_scene):
        self.current_scene = new_scene
    
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.current_scene.handle_events(events)
            self.current_scene.update(dt)
            self.current_scene.draw(self.screen)
            
            pygame.display.update()
        
        pygame.quit()
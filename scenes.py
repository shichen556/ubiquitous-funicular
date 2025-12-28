import pygame
from button import Button
from fields import ElectricField, MagneticField
from entities import Particle

class Scene:
    def __init__(self, game):
        self.game=game
        
    def handle_events(self, events):
        raise NotImplementedError
    
    def update(self, dt):
        raise NotImplementedError
    
    def draw(self, screen):
        raise NotImplementedError

# Game states
class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("Trebuchet MS", 80)
        
        self.buttons = [
            Button(350, 200, 200, 60, "Play", self.start_game),
            Button(350, 300, 200, 60, "Options", self.open_options),
            Button(350, 400, 200, 60, "Exit", self.quit_game)
        ]
    
    def start_game(self):
        print("Starting the game...")
        self.game.change_scene(PlayScene(self.game))
    
    def open_options(self):
        print("Opening options...")
        self.game.change_scene(OptionsScene(self.game))
    
    def quit_game(self):
        self.game.running = False
    
    def handle_events(self, events):
        for button in self.buttons:
            button.handle_events(events)
    
    def update(self, dt):
        pass
    
    def draw(self, screen):
        # Background color
        screen.fill("#0A0A23")
        title_surf = self.font.render("My Game", True, "#B0C4FF")
        title_rect = title_surf.get_rect(center = (self.game.WIDTH // 2, 80))
        
        # Game title
        screen.blit(title_surf, title_rect)
        
        for button in self.buttons:
            button.draw(screen)
        
class PlayScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("Arial", 30)
        
        self.electron = Particle(50, 200, "Negative")
        self.proton = Particle(200, 300, "Positive")
        
        self.electric_field = ElectricField(pygame.Rect(450 - 50, 350 - 50, 100, 100))
        self.magnetic_field = MagneticField(pygame.Rect(450 - 50, 350 - 50, 100, 100), field_type="in")
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.change_scene(MenuScene(self.game))
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Permitir cambiar la pos del campo con el clic del raton
                self.electric_field.rect.center=pygame.mouse.get_pos()
                self.magnetic_field.rect.center=pygame.mouse.get_pos()
    
    def update(self, dt):
        self.electron.update(self.electric_field, self.magnetic_field)
        self.proton.update(self.electric_field, self.magnetic_field)
    
    def draw(self, screen):
        # Background color
        screen.fill("#0A0A23")
        
        self.electric_field.draw(screen)
        self.magnetic_field.draw(screen)
        
        self.electron.draw(screen)
        self.proton.draw(screen)
        
        back_button = Button(50,50,200,50, "Back to Menu", self.go_back)
        back_button.draw(screen)

    def go_back(self):
        self.game.change_scene(MenuScene(self.game))
        
class PauseScene:
    pass

class OptionsScene:
    pass
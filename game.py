import pygame
import menu
import objects

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Framerate control
        self.running = True
        self.playing = False
        self.clock = pygame.time.Clock()
        
        # Keyboard control
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        
        # Pygame screen setup
        self.DISPLAY_W, self.DISPLAY_H = 900, 700
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H)) # Offscreen
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H)) # Screen
        pygame.display.set_caption("Runner")
        
        # Font
        self.font_name = "Tahoma"
        
        # Color palette
        self.BG_COLOR = "#0A0A23"
        self.TITLE_COLOR = "#00BFFF"
        self.MENU_COLOR = ["#00BFFF", "#2A3B7A"]
        self.TXT_COLOR = "#B0C4FF"
        
        # Load Menu options
        self.main_menu = menu.MainMenu(self)
        self.options = menu.OptionsMenu(self)
        self.credits = menu.CreditsMenu(self)
        self.curr_menu = self.main_menu
        
        # Load In-game
        self.E = 6
        self.B = 0.05
        
        self.eF = objects.ElectricField(self, (200, 100), (100, 300), "right", self.E)
        self.mgF = objects.MagneticField(self, (650, 100), (50, 220), "out", self.B)
        
        self.proton = objects.Particle(self, (100, 150), (5.0, 0.0), "+")
        self.electron = objects.Particle(self, (100, 250), (5.0, 0.0), "-")
        
        # Load HUD
        self.proton_stats = menu.GameMenu(self, (10, self.DISPLAY_H - 140-130), (350, 130), B=self.B, particle=self.proton)
        self.electron_stats = menu.GameMenu(self, (10, self.DISPLAY_H - 140), (350, 130), B=self.B, particle=self.electron)
        
        self.eF_stats = menu.GameMenu(self, (10 + 350, self.DISPLAY_H - 140-130), (175, 130), field=self.eF)
        self.mgF_stats = menu.GameMenu(self, (10 + 350, self.DISPLAY_H - 140), (175, 130), field=self.mgF)
    
    # Game loop
    def game_loop(self):
        self.electron.reset_pos()
        self.proton.reset_pos()
        
        while self.playing:
            self.check_events()
            if self.START_KEY or self.BACK_KEY:
                self.playing = False
                
            self.display.fill(self.BG_COLOR)
            
            # Draw field
            self.eF.draw()
            self.mgF.draw()
            
            # Draw particle
            self.proton.draw()
            self.electron.draw()
            
            # Draw HUD
            self.proton_stats.show()
            self.electron_stats.show()
            
            # self.eF_stats.show()
            # self.mgF_stats.show()
            
            # Update stats
            self.proton_stats.update(self.proton)
            self.electron_stats.update(self.electron)
            
            self.window.blit(self.display, (0,0))
            
            # Movement
            self.proton.move()
            self.electron.move()
            
            self.proton.check_eF_collision(self.eF)
            self.electron.check_eF_collision(self.eF)
            
            # self.proton.check_mgF_collision(self.mgF)
            # self.electron.check_mgF_collision(self.mgF)
            
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(60)
    
    # Check user keyboard input
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
        
    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False 
    
    def draw_text(self, text, size, x, y, color):
        font = pygame.font.SysFont(self.font_name, size)
        
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center = (x, y))
        
        self.display.blit(text_surf, text_rect)
    
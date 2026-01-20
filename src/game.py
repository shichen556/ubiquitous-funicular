import pygame
import menu as menu
import objects as objects

from debug.debug import debug

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Framerate control
        self.running = True
        self.playing = False
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
        # Pygame screen setup
        self.GAME_W, self.GAME_H = 450, 350
        self.DISPLAY_W, self.DISPLAY_H = 900, 700
        
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H)) # Offscreen
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H)) # Screen
        pygame.display.set_caption("Runner")
        
        # Keyboard control
        self.actions = {"up": False, "down": False, "left": False, "right": False, 
                        "start": False, "back": False}
        
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
        self.E = 2
        self.B = 0.05
        
        self.eF = objects.ElectricField(self, (200, 100), (100, 220), "right", self.E)
        self.mgF = objects.MagneticField(self, (400, 100), (50, 220), "out", self.B)
        
        self.proton = objects.Particle(self, (100, 150), (5.0, 0.0), "+")
        self.electron = objects.Particle(self, (100, 250), (5.0, 0.0), "-")
        
        # Load HUD
        self.proton_stats = menu.HUD(self, (10, self.DISPLAY_H - 140-130), (350, 130), B=self.B, particle=self.proton)
        self.electron_stats = menu.HUD(self, (10, self.DISPLAY_H - 140), (350, 130), B=self.B, particle=self.electron)
        
        self.eF_stats = menu.HUD(self, (10 + 350, self.DISPLAY_H - 140-130), (175, 130), field=self.eF)
        self.mgF_stats = menu.HUD(self, (10 + 350, self.DISPLAY_H - 140), (175, 130), field=self.mgF)
        
        self.is_draw = False
    
    # Game loop
    def game_loop(self):
        self.electron.reset_pos()
        self.proton.reset_pos()
        
        while self.playing:
            self.check_events()
            if self.actions["start"] or self.actions["back"]:
                self.playing = False
                
            self.display.fill(self.BG_COLOR)
            
            # Draw field
            self.eF.draw()
            self.mgF.draw()
            
            # Draw particle
            self.proton.draw()
            # self.electron.draw()
            
            # Draw HUD
            if not self.is_draw:
                # self.proton_stats.show()
                # self.electron_stats.show()
                
                # self.eF_stats.show()
                # self.mgF_stats.show()
                self.is_draw = True
            
            debug(f"{self.clock.get_fps():.2f}", self.display)
            
            # Update stats
            # self.proton_stats.update(self.proton)
            # self.electron_stats.update(self.electron)
            
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
            self.clock.tick(self.FPS)
    
    # Check user keyboard input
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_w]:
                    self.actions["up"] = True
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    self.actions["down"] = True
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.actions["left"] = True
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.actions["right"] = True
                if event.key == pygame.K_RETURN:
                    self.actions["start"] = True
                if event.key in [pygame.K_BACKSPACE, pygame.K_ESCAPE]:
                    self.actions["back"] = True
        
    def reset_keys(self):
        for key in self.actions:
            self.actions[key] = False
    
    def draw_text(self, text, size, x, y, color):
        font = pygame.font.SysFont(self.font_name, size)
        
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center = (x, y))
        
        self.display.blit(text_surf, text_rect)
    
import ctypes
import pygame
import time

from in_game import InGame

from debug.debug import debug

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Framerate control
        self.running = True
        self.playing = True
        
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.dt = 0
        self.t0 = time.time()
        self.t1 = 0
        
        # Pygame screen setup
        # Get monitor size
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()

        self.scalex, self.scaley = 0.8, 0.8
        self.WIDTH, self.HEIGHT = user32.GetSystemMetrics(0) * self.scalex, user32.GetSystemMetrics(1) * self.scaley

        self.DISPLAY_W, self.DISPLAY_H = int(self.WIDTH), int(self.HEIGHT)
        self.DISPLAY_H2 = self.DISPLAY_H-260
        
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H)) # Title Offscreen
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H)) # Screen
        pygame.display.set_caption("Runner")
        self.display1 = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H2))
        self.display2 = pygame.Surface((self.DISPLAY_W, 260))
        
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
        
        # Stack structure for states
        self.state_stack = []
        self.load_states()
        
        # Load In-game
        self.in_game = InGame()
        
        self.is_draw = False
        self.is_pause = False
        
    # Game loop
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.actions["start"] or self.actions["back"]:
                self.playing = False
            
            self.display1.fill(self.BG_COLOR)
            
            self.in_game.draw_objects()
            self.get_dt()
            
            if not self.is_pause:
                self.in_game.update()
            else:
                self.dt = 0
                
            debug(f"{self.clock.get_fps():.2f}", self.display1)
            
            pygame.draw.line(self.display2, "black", (0, 0), (self.DISPLAY_W, 0), 10)
            self.window.blit(self.display1, (0, 0))
            self.window.blit(self.display2, (0, self.DISPLAY_H2))
            
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(self.FPS)
    
    # Check user keyboard input
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
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
                if event.key == pygame.K_t:
                    if self.is_pause:
                        self.is_pause = False
                    else:
                        self.is_pause = True
            
    def reset_keys(self):
        for key in self.actions:
            self.actions[key] = False
    
    def draw_text(self, text, size, x, y, color):
        font = pygame.font.SysFont(self.font_name, size)
        
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center = (x, y))
        
        self.display.blit(text_surf, text_rect)
    
    def get_dt(self):
        self.t1 = time.time()
        self.dt = self.t1 - self.t0
        self.t0 = time.time()
    
    # State management
    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)
    
    def load_states(self):
        self.state_stack.append()
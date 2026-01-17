import pygame
import menu

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Framerate control
        self.running = True
        self.playing = False
        clock = pygame.time.Clock()
        
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
        self.MENU_COLOR = ["#00BFFF", "#2A3B7A"]
        self.TXT_COLOR = "#B0C4FF"
        
        # Menu options
        self.main_menu = menu.MainMenu(self)
        self.options = menu.OptionsMenu(self)
        self.credits = menu.CreditsMenu(self)
        self.curr_menu = self.main_menu
    
    # In-game loop
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
                
            self.display.fill(self.BG_COLOR)
            self.draw_text("Thanks for playing", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            
            pygame.display.update()
            self.reset_keys()
    
    # Check user keyboard input
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
                
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
        self.UP_KEY, 
        self.DOWN_KEY, 
        self.START_KEY, 
        self.BACK_KEY = False, False, False, False
    
    def draw_text(self, text, size, x, y):
        font = pygame.font.SysFont(self.font_name, size)
        
        text_surf = font.render(text, True, self.MENU_COLOR)
        text_rect = text_surf.get_rect(center = (x, y))
        
        self.display.blit(text_surf, text_rect)
    
import pygame
from math import sin, cos
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
        self.eF = objects.ElectricField(self, "right")
        self.mgF = objects.MagneticField(self, "out")
        
        self.proton = objects.Particle(self, (100, 200), (2, 0), "+")
        self.electron = objects.Particle(self, (100, 300), (2, 0), "-")
    
    # Game loop
    def game_loop(self):
        self.reset_pos()
        
        while self.playing:
            self.check_events()
            if self.START_KEY or self.BACK_KEY:
                self.playing = False
                
            self.display.fill(self.BG_COLOR)
            
            # Draw field
            self.mgF.draw()
            self.eF.draw()
            
            # Draw particle
            self.proton.draw()
            self.electron.draw()
            
            self.window.blit(self.display, (0,0))
            
            self.proton.move()
            self.electron.move()
            
            self.proton.check_eF_collision(self.eF.square)
            self.electron.check_eF_collision(self.eF.square)
            
            self.proton.check_mgF_collision(self.mgF.square)
            self.electron.check_mgF_collision(self.mgF.square)
            
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
    
    def reset_pos(self):
        # Set to initial position
        if self.proton.rect.x != 100:
            self.proton.rect.x = 100
        if self.proton.rect.y != 200:
            self.proton.rect.y = 200
            
        if self.electron.rect.x != 100:
            self.electron.rect.x = 100
        if self.electron.rect.y != 300:
            self.electron.rect.y = 300

# def rotate(x, y):
#     angulo += vel_ang
    
#     v_x = vel * cos(angulo)
#     v_y = vel * sin(angulo)
    
#     x += v_x
#     y += v_y

# # valores MCU
# radio = m*vel/(q*B)
# angulo = 0
# vel_ang = vel/radio
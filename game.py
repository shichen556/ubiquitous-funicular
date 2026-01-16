import pygame
from math import sin, cos
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
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
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



def draw_electric_field(rect, spacing = 50):
    color = "#FFD700"
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    arrow_length = 20
    arrow_size = 6
    
    for y in range(spacing//2, rect.bottom, spacing):
        # Horizontal lines
        pygame.draw.line(screen, color, (0,y), (rect.right, y), 2)
        
        # Arrow after a interval
        for x in range(0, rect.right, 100):
            pygame.draw.line(screen, color,
                             (x, y),
                             (x + arrow_length, y - arrow_size), 2)
            pygame.draw.line(screen, color,
                             (x, y),
                             (x + arrow_length, y + arrow_size), 2)
            
def draw_magnetic_field_out(rect, spacing=60):
    color = "#00FFCC"
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    for y in range(rect.top + 20, rect.bottom, spacing):
        for x in range(rect.left + 20, rect.right, spacing):
            # Campo saliente (·)
            pygame.draw.circle(screen, color, (x, y), 12, 1)
            pygame.draw.circle(screen, color, (x, y), 4)
                
def draw_magnetic_field_in(rect, spacing=60):
    color =  "#9B30FF"
    pygame.draw.rect(screen, (255,255,255), rect, 1)
    
    for y in range(rect.top + 20, rect.bottom, spacing):
        for x in range(rect.left + 20, rect.right, spacing):
            # Campo entrante (x)
            pygame.draw.circle(screen, color, (x, y), 12, 1)
            pygame.draw.line(screen, color, (x-4, y-4), (x+4, y+4), 2)
            pygame.draw.line(screen, color, (x-4, y+4), (x+4, y-4), 2)

def rotate(x, y):
    angulo += vel_ang
    
    v_x = vel * cos(angulo)
    v_y = vel * sin(angulo)
    
    x += v_x
    y += v_y

area_pos_x = 450
area_pos_y = 350

vel = 5
v_x = vel
v_y = 0

e_pos_x=50
e_pos_y=200

            
# p_pos_x=200
# p_pos_y=300

# Constantes
q = 1.602
m = 9.11
B = 0.5

# valores MCU
radio = m*vel/(q*B)
angulo = 0
vel_ang = vel/radio
    
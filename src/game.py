import pygame
import menu
import objects
import title

from debug.debug import debug
import time

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Framerate control
        self.running = True
        self.playing = False
        
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.dt = 0
        self.prev_time = 0
        
        # Pygame screen setup
        self.GAME_W, self.GAME_H = 450, 350
        self.DISPLAY_W, self.DISPLAY_H = 900, 700
        
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H)) # Title Offscreen
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
        self.main_menu = title.MainMenu(self)
        self.options = title.OptionsMenu(self)
        self.credits = title.CreditsMenu(self)
        self.curr_menu = self.main_menu
        
        # Load In-game
        self.E = 2
        self.B = 0.2
        
        self.eF = objects.ElectricField(self, (200, 100), (100, 220), "right", self.E)
        self.mgF = objects.MagneticField(self, (100, 100), (400, 400), "in", self.B)
        
        self.proton = objects.Particle(self, (250, 300), (3.0, 0.0), "+")
        self.electron = objects.Particle(self, (100, 250), (5.0, 0.0), "-")
        
        self.display1 = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H - 260))
        self.display2 = pygame.Surface((self.DISPLAY_W, 260))
           
        # Load HUD
        self.proton_stats = menu.ParticleHUD(self, (10, 140-130), (350, 130), self.B, self.proton)
        self.electron_stats = menu.ParticleHUD(self, (10, 140), (350, 130), self.B, self.electron)
        
        self.eF_stats = menu.FieldHUD(self, (10 + 350, 140-130), (175, 130), self.eF)
        self.mgF_stats = menu.FieldHUD(self, (10 + 350, 140), (175, 130), self.mgF)
        
        self.is_draw = False
        self.is_pause = True
        
    # Game loop
    def game_loop(self):
        self.electron.reset_pos()
        self.proton.reset_pos()
        
        while self.playing:
            self.check_events()
            if self.actions["start"] or self.actions["back"]:
                self.playing = False
                
            self.display1.fill(self.BG_COLOR)
            
            # Draw field
            # self.eF.draw()
            self.mgF.draw()
            
            # Draw particle
            self.proton.draw()
            # self.electron.draw()
            
            # Draw HUD    
            if not self.is_draw:
                self.display2.fill(self.BG_COLOR)
                self.proton_stats.show()
                # self.electron_stats.show()
                
                # self.eF_stats.show()
                # self.mgF_stats.show()
                
                self.is_draw = True
            
            if self.is_pause:
                if self.proton.vel != 0:
                    self.proton_stats.update_pos(self.proton)
                
                # if self.proton.eF_collision(self.eF) or self.proton.edge_collision():
                #     self.update_eF_collision(self.proton_stats, self.proton)
                if self.proton.mgF_collision(self.mgF) or self.proton.edge_collision():
                    self.update_mg_collision(self.proton_stats, self.proton)
                
                # if self.electron.eF_collision(self.eF):
                #     self.update_eF_collision(self.electron_stats, self.electron)
                # if self.electron.mgF_collision(self.mgF):
                #     self.mg_collision(self.electron_stats, self.electron)
                
                # Movement
                self.proton.move()
                # self.electron.move()
                
            self.proton.draw_circular_trajectory(self.mgF.type)
            
            debug(f"{self.clock.get_fps():.2f}", self.display1)
            debug(f"{self.proton.vel[0]:.2f}, {self.proton.vel[1]:.2f}", self.display1, 40)
            debug(f"w: {self.proton.ang_vel:.2f}", self.display1, 60)
            debug(f"alpha: {self.proton.angle:.2f}", self.display1, 80)
            debug(f"r: {self.proton.mod_vel:.2f}", self.display1, 100)
            debug(f"Pause: {self.is_pause}", self.display1, 120)
            
            pygame.draw.line(self.display2, "black", (0, 0), (self.DISPLAY_W, 0), 10)
            self.window.blit(self.display1, (0,0))
            self.window.blit(self.display2, (0,self.DISPLAY_H-260))
            
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
    
    def update_eF_collision(self, particle_hud, particle):
        # Update stats
        particle_hud.update1(particle)
        particle_hud.update2(particle)
        particle_hud.update_vel_comp(particle)
    
    def update_mg_collision(self, particle_hud, particle):
        # Update stats
        particle_hud.update2(particle)
        particle_hud.update_vel_comp(particle)
import ctypes
import os
import pygame
import time

import hud
import menu
import objects
import tiles

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
        self.MENU_COLOR = ["#00BFFF", "#2A3B7A"] # 2A 30 -85
        self.TXT_COLOR = "#B0C4FF"
        
        # Stack structure for states
        self.state_stack = []
        self.load_states()
        
        # Load Menu options
        self.main_menu = menu.MainMenu(self)
        self.options = menu.OptionsMenu(self)
        self.credits = menu.CreditsMenu(self)
        self.curr_menu = self.main_menu
        
        # Load In-game
        self.E = 2
        self.B = 15
        
        self.scale = 1
        
        self.eF_pos = [48, 48]
        self.mgF_pos = [288, 48]
        
        self.eF_size = [112, 112]
        self.mgF_size = [112, 112]
        
        self.eF = objects.ElectricField(self, self.eF_pos, self.eF_size, "up", self.E)
        self.mgF = objects.MagneticField(self, self.mgF_pos, self.mgF_size, "out", self.B)
        
        self.proton_pos = [288, 192]
        self.electron_pos = [192, 192]
        
        self.proton_vel = [100.0, 0.0]
        self.electron_vel = [100.0, 0.0]
        
        self.proton = objects.Particle(self, self.proton_pos, self.proton_vel, "+")
        self.electron = objects.Particle(self, self.electron_pos, self.electron_vel, "-")
        
        # Load HUD
        self.proton_stats = hud.ParticleHUD(self, (10, 140-130), (350, 130), self.B, self.proton)
        self.electron_stats = hud.ParticleHUD(self, (10, 140), (350, 130), self.B, self.electron)
        
        self.eF_stats = hud.FieldHUD(self, (10 + 350, 140-130), (175, 130), self.eF)
        self.mgF_stats = hud.FieldHUD(self, (10 + 350, 140), (175, 130), self.mgF)
        
        # Load Tiles
        self.tile = tiles.TileMap(self)
        
        self.is_draw = False
        self.is_pause = False
        
    # Game loop
    def game_loop(self):
        self.reset()
        while self.playing:
            self.check_events()
            if self.actions["start"] or self.actions["back"]:
                self.playing = False
            
            self.display1.fill(self.BG_COLOR)
            
            self.draw_objects()
            self.get_dt()
            
            if not self.is_pause:
                if self.proton.vel != 0:
                    self.proton_stats.update_pos(self.proton)
                if self.electron.vel != 0:
                    self.electron_stats.update_pos(self.proton)
                self.check_collision()
                
                # Movement
                # self.proton.move(self.dt)
                # self.electron.move(self.dt)
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
        
    def get_dt(self):
        self.t1 = time.time()
        self.dt = self.t1 - self.t0
        self.t0 = time.time()
    
    def reset(self):
        self.electron.reset_pos()
        self.proton.reset_pos()
    
    def draw_objects(self):
        self.tile.draw_map()
        
        # Draw field
        self.eF.draw()
        self.mgF.draw()
        
        # Draw particle
        self.proton.draw()
        self.electron.draw()

        # Draw HUD    
        if not self.is_draw:
            self.display2.fill(self.BG_COLOR)
            
            self.proton_stats.show()
            self.electron_stats.show()
            
            self.eF_stats.show()
            self.mgF_stats.show()
            
            self.is_draw = True
                
    def check_collision(self):
        if self.proton.eF_collision(self.eF) or self.proton.edge_collision():
            self.update_eF_collision(self.proton_stats, self.proton)
        if self.proton.mgF_collision(self.mgF, self.dt) or self.proton.edge_collision():
            self.proton.draw_circular_trajectory(self.mgF.type)
            self.update_mg_collision(self.proton_stats, self.proton)
        
        if self.electron.eF_collision(self.eF):
            self.update_eF_collision(self.electron_stats, self.electron)
        if self.electron.mgF_collision(self.mgF, self.dt) or self.electron.edge_collision():
            self.electron.draw_circular_trajectory(self.mgF.type)
            self.update_mg_collision(self.electron_stats, self.electron)
    
    # State management
    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)
    
    def load_states(self):
        self.state_stack.append()
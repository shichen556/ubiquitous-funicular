import UI.hud as hud
import objects
import tiles
import UI.input as input

class InGame:
    def __init__(self, game):
        self.game = game
        
        self.E = 2
        self.B = 15
        
        self.scale = 1
        
        self.eF_pos = [48, 48]
        self.mgF_pos = [288, 48]
        
        self.eF_size = [112, 112]
        self.mgF_size = [112, 112]
        
        self.eF = objects.ElectricField(self.game, self.eF_pos, self.eF_size, "up", self.E)
        self.mgF = objects.MagneticField(self.game, self.mgF_pos, self.mgF_size, "out", self.B)
        
        self.proton_pos = [288, 192]
        self.electron_pos = [192, 192]
        
        self.proton_vel = [100.0, 0.0]
        self.electron_vel = [100.0, 0.0]
        
        self.proton = objects.Particle(self.game, self.proton_pos, self.proton_vel, "+")
        self.electron = objects.Particle(self.game, self.electron_pos, self.electron_vel, "-")
        
        # Load HUD
        self.hud_particle_pos = (0, 5)
        
        self.hud_particle_size = (350, 130)
        self.hud_field_size = (175, 130)
        
        self.hud_posx_offsetx = self.hud_particle_size[0] - 5
        self.hud_posy_offsety = self.hud_particle_size[1] - 5
        
        self.hud_field_pos = (self.hud_posx_offsetx, self.hud_particle_pos[1])
        
        self.proton_stats = hud.ParticleHUD(self.game, self.hud_particle_pos, self.hud_particle_size, self.B, self.proton)
        self.electron_stats = hud.ParticleHUD(self.game, (self.hud_particle_pos[0], self.hud_particle_pos[1]+self.hud_posy_offsety), self.hud_particle_size, self.B, self.electron)
        
        self.eF_stats = hud.FieldHUD(self.game, self.hud_field_pos, self.hud_field_size, self.eF)
        self.mgF_stats = hud.FieldHUD(self.game, (self.hud_field_pos[0], self.hud_field_pos[1]+self.hud_posy_offsety), self.hud_field_size, self.mgF)
        
        # Load UI
        # self.label1 = input.Control(self.game.display1, (550, 50), (200, 50), "Test")
            
        # Load Tiles
        self.tile = tiles.TileMap(self.game)
    
    def draw_objects(self):
        # self.tile.draw_map()
        
        # Draw field
        self.eF.draw()
        self.mgF.draw()
        
        # Draw particle
        self.proton.draw()
        self.electron.draw()

        # Draw HUD    
        if not self.game.is_draw:
            # self.proton_stats.show()
            # self.electron_stats.show()
            
            # self.eF_stats.show()
            # self.mgF_stats.show()
            
            self.game.is_draw = True
        
        # input.pygame_widgets.update(input.pygame.event.get())
        
            
    def update_eF_collision(self, particle_hud, particle):
        # Update stats
        particle_hud.update1(particle)
        particle_hud.update2(particle)
        particle_hud.update_vel_comp(particle)
    
    def update_mg_collision(self, particle_hud, particle):
        # Update stats
        particle_hud.update2(particle)
        particle_hud.update_vel_comp(particle)
    
    def check_collision(self):
        if self.proton.eF_collision(self.eF) or self.proton.edge_collision():
            self.update_eF_collision(self.proton_stats, self.proton)
        if self.proton.mgF_collision(self.mgF, self.game.dt) or self.proton.edge_collision():
            self.proton.draw_circular_trajectory(self.mgF.type)
            self.update_mg_collision(self.proton_stats, self.proton)
        
        if self.electron.eF_collision(self.eF):
            self.update_eF_collision(self.electron_stats, self.electron)
        if self.electron.mgF_collision(self.mgF, self.game.dt) or self.electron.edge_collision():
            self.electron.draw_circular_trajectory(self.mgF.type)
            self.update_mg_collision(self.electron_stats, self.electron)
    
    def update(self):
        if self.proton.vel != 0:
            self.proton_stats.update_pos(self.proton)
        if self.electron.vel != 0:
            self.electron_stats.update_pos(self.proton)
        self.check_collision()
        
        # Movement
        # self.proton.move(self.dt)
        # self.electron.move(self.dt)
        
    def reset(self):
        self.electron.reset_pos()
        self.proton.reset_pos()
        
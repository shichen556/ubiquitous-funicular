from math import sin, cos
import pygame

class Scene:
    def handle_events(self, events):
        pass
    
    def update(self, dt):
        pass
    
    def draw(self, screen):
        pass

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Set up pygame screen
        self.WIDTH = 900
        self.HEIGHT = 700
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Runner")
        
        # Framerate control
        self.clock = pygame.time.Clock()
        self.running = True
    
    def change_scene(self, scene):
        self.current_scene = scene
    
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000 # Frame ceiling
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.current_scene.handle_events(events)
            self.current_scene.update(dt)
            self.current_scene.draw(self.screen)
            
            pygame.display.update()
        
        pygame.quit()

# Game states
class MenuScene(Scene):
    def __init__(self, game):
        self.game = game
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
        self.game = game
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
        self.electron.update(dt)
        self.proton.update(dt)
    
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

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x,y,width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont("Tahoma", 50)
        self.color = "#00BFFF"
        self.hover_color = "#2A3B7A"
        self.is_hovered = False

    def draw(self, screen):
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.color
        
        pygame.draw.rect(screen, color, self.rect)
        text_surf = self.font.render(self.text, True, "#FFFFFF")
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.action() # Ejecutar la accion asociada al boton
            elif event.type == pygame.MOUSEMOTION:
                self.is_hovered = self.rect.collidepoint(event.pos)
        
class Entity:
    pass

class Particle:
    def __init__(self, pos_x, pos_y, charge, mass = 9.11, q=1.602):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.charge=charge
        self.mass=mass
        self.q=q
        if charge == "Negative":
            self.color = "#1E90FF"
        else:
            self.color = "#FF4500"
        
        self.v_x = 0
        self.v_y = 0
        self.acc_x=0
        self.acc_y=0
        
        self.vel = 5
        self.angle = 0
    
    def apply_force(self, fx, fy):
        self.acc_x+=fx/self.mass
        self.acc_y+=fy/self.mass
    
    def update(self, electric_field, magnetic_field):
        ex,ey=self.calculate_electric_field_force(electric_field)
        self.apply_force(ex,ey)
        
        bx,by=self.calculate_magnetic_field(magnetic_field)
        self.apply_force(bx,by)
        
        self.v_x += self.acc_x
        self.v_y += self.acc_y
        
        self.pos_x += self.v_x
        self.pos_y += self.v_y
        
        self.acc_x=0
        self.acc_y=0
    
    def calculate_electric_force(self, electric_field):
        # Usar la carga y el campo eléctrico
        fx = self.q * electric_field.calculate_force(self.pos_x, self.pos_y, "x")
        fy = self.q * electric_field.calculate_force(self.pos_x, self.pos_y, "y")
        return fx, fy
    
    def calculate_magnetic_force(self, magnetic_field):
        bx, by = magnetic_field.calculate_force(self.pos_x, self.pos_y)
        # Usamos el producto cruzado (v x B) para calcular la fuerza magnética
        fx = self.vel_y * by - self.vel_x * bx
        fy = self.vel_x * bx - self.vel_y * by
        return fx, fy
    
    
    def reset_pos(self):
        self.pos_x = -100
        self.pos_y = 200
        self.v_x = self.vel
        self.v_y = 0
        self.angulo = 0
    
    def is_in_field(self):
        return self.field_rect.collidepoint(self.pos_x, self.pos_y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), 10)

class ElectricField:
    def __init__(self, rect, strength=1.0, spacing=50):
        self.rect=rect
        self.strength=strength
        self.spacing=spacing
        self.color="#FFD700"
    
    def calculate_foce(self, x,y,direction="x"):
        # Esto es simplificado: calculamos la fuerza como si el campo eléctrico es uniforme
        if direction == "x":
            return self.strength
        else:
            return self.strength  # Puede ser diferente si el campo no es uniforme
        
    def draw(self, screen):
        area_subsurf = screen.subsurface(self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 1)
        
        width, height = area_subsurf.get_size()
    
        arrow_length = 20
        arrow_size = 6

        for y in range(self.spacing//2, height, self.spacing):
            # Horizontal lines
            pygame.draw.line(area_subsurf, self.color, (0,y), (width, y), 2)
            
            # Arrow after a interval
            for x in range(0, width, 100):
                pygame.draw.line(area_subsurf, self.color,
                                (x, y),
                                (x + arrow_length, y - arrow_size), 2)
                pygame.draw.line(area_subsurf, self.color,
                                (x, y),
                                (x + arrow_length, y + arrow_size), 2)

class MagneticField:
    def __init__(self, rect, strength=1.0, field_type="out", spacing=60):
        self.rect=rect
        self.strength=strength
        self.field_type=field_type
        if field_type == "out":
            self.color = "#00FFCC"
        else:
            self.color = "#9B30FF"
    
    def calculate_force(self, x, y):
        # Simplificado: el campo es uniforme y radia hacia afuera
        # Devuelve las componentes del campo magnético en x y y
        return self.strength, self.strength  # Solo una aproximación para ilustrar
    
    def draw(self, screen):
        area_subsurf = screen.subsurface(self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 1)
        
        for y in range(self.rect.top + 20, self.rect.bottom, self.spacing):
            for x in range(self.rect.left + 20, self.rect.right, self.spacing):
                if self.field_type=="out":
                    # Campo saliente (·)
                    pygame.draw.circle(area_subsurf, self.color, (x, y), 12, 1)
                    pygame.draw.circle(area_subsurf, self.color, (x, y), 4)
                elif self.field_type=="in":
                    # Campo entrante (x)
                    pygame.draw.circle(screen, self.color, (x, y), 12, 1)
                    pygame.draw.line(screen, self.color, (x-4, y-4), (x+4, y+4), 2)
                    pygame.draw.line(screen, self.color, (x-4, y+4), (x+4, y-4), 2)

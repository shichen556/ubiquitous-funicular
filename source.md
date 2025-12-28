# Tutorial starting with Pygame
https://www.youtube.com/watch?v=AY9MnQ4x3zk

# Documentation
https://www.pygame.org/docs/

# AI generated
class Scene:
    def handle_events(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pass

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 900
        self.HEIGHT = 700
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Runner")

        self.clock = pygame.time.Clock()
        self.running = True

        self.current_scene = MenuScene(self)

    def change_scene(self, scene):
        self.current_scene = scene

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.current_scene.handle_events(events)
            self.current_scene.update(dt)
            self.current_scene.draw(self.screen)

            pygame.display.update()

        pygame.quit()

class MenuScene(Scene):
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("Trebuchet MS", 80)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Por ahora, clic = ir al juego
                self.game.change_scene(PlayScene(self.game))

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill("#0A0A23")
        title = self.font.render("My Game", True, "#B0C4FF")
        rect = title.get_rect(center=(self.game.WIDTH // 2, 80))
        screen.blit(title, rect)

class PlayScene(Scene):
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("Arial", 30)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.change_scene(MenuScene(self.game))

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill("#0A0A23")
        text = self.font.render("Playing...", True, "#FFFFFF")
        screen.blit(text, (50, 50))

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
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
                    self.action()  # Ejecutar la acción asociada al botón
            elif event.type == pygame.MOUSEMOTION:
                self.is_hovered = self.rect.collidepoint(event.pos)

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
        screen.fill("#0A0A23")
        title = self.font.render("My Game", True, "#B0C4FF")
        rect = title.get_rect(center=(self.game.WIDTH // 2, 80))
        screen.blit(title, rect)

        for button in self.buttons:
            button.draw(screen)

class PlayScene(Scene):
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("Arial", 30)
        self.electron = Particle(50, 200, "Negative")  # Partícula negativa (electrón)
        self.proton = Particle(200, 300, "Positive")  # Partícula positiva (protón)
        self.field_rect = pygame.Rect(450 - 50, 350 - 50, 100, 100)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Permitir cambiar la posición del campo con el clic del ratón
                self.field_rect.center = pygame.mouse.get_pos()

    def update(self, dt):
        self.electron.update(dt)
        self.proton.update(dt)

    def draw(self, screen):
        screen.fill("#0A0A23")

        # Dibuja el campo magnético
        draw_magnetic_field_in(self.field_rect)

        # Dibuja las partículas
        self.electron.draw(screen)
        self.proton.draw(screen)

        # Dibuja el botón de retroceso
        back_button = Button(50, 50, 200, 50, "Back to Menu", self.go_back)
        back_button.draw(screen)

    def go_back(self):
        self.game.change_scene(MenuScene(self.game))

class Particle:
    def __init__(self, pos_x, pos_y, charge):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.charge = charge
        self.vel = 5
        self.v_x = self.vel
        self.v_y = 0
        self.color = "#1E90FF" if charge == "Negative" else "#FF4500"

    def update(self, dt):
        # Movimiento en MCU (Movimiento Circular Uniforme) o MRU (Movimiento Rectilíneo Uniforme)
        if self.pos_x > 1000 or self.pos_x < -100 or self.pos_y > 800 or self.pos_y < -100:
            self.reset_position()

        if self.is_in_field():
            self.v_x = self.vel * cos(angulo)
            self.v_y = self.vel * sin(angulo)

        self.pos_x += self.v_x
        self.pos_y += self.v_y

    def reset_position(self):
        self.pos_x = -100
        self.pos_y = 200
        self.v_x = self.vel
        self.v_y = 0

    def is_in_field(self):
        return self.field_rect.collidepoint(self.pos_x, self.pos_y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), 10)

def draw_electric_field(surface, color, spacing=50):
    width, height = surface.get_size()
    arrow_length = 20
    arrow_size = 6

    for y in range(spacing // 2, height, spacing):
        # Línea horizontal
        pygame.draw.line(surface, color, (0, y), (width, y), 2)

        # Flechas cada cierto intervalo
        for x in range(0, width, 100):
            pygame.draw.line(surface, color,
                             (x, y),
                             (x + arrow_length, y - arrow_size), 2)
            pygame.draw.line(surface, color,
                             (x, y),
                             (x + arrow_length, y + arrow_size), 2)

def draw_magnetic_field(surface, color_out, color_in, spacing=60, phase=0):
    width, height = surface.get_size()

    for y in range(spacing // 2, height, spacing):
        for x in range(spacing // 2, width, spacing):
            if (x // spacing + y // spacing + phase) % 2 == 0:
                # Campo saliendo (•)
                pygame.draw.circle(surface, color_out, (x, y), 4)
            else:
                # Campo entrando (×)
                pygame.draw.line(surface, color_in, (x - 4, y - 4), (x + 4, y + 4), 2)
                pygame.draw.line(surface, color_in, (x - 4, y + 4), (x + 4, y - 4), 2)


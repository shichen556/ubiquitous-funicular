from math import sin, cos

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
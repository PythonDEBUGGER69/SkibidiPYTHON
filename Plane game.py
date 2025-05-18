import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Simulator/Roblox")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GOLDEN_SUN = (255, 223, 0)
ORANGE = (255, 165, 0)
DARK_GRAY = (64, 64, 64)
CLOUD_COLOR = (240, 240, 240)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Font
font = pygame.font.Font(None, 36)

# Plane properties
plane1_color = RED
plane2_color = GREEN
plane1_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2, 50, 30)
plane2_rect = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, 50, 30)

# Physics properties
gravity = 0.5
lift = -10
thrust = 5
velocity1 = [0, 0]
velocity2 = [0, 0]

# Ground
GROUND_LEVEL = HEIGHT - 50

# Player names
player1_name = "Player 1"
player2_name = "Player 2"

# Scoring
score1 = 0
score2 = 0

# Highscore persistence
highscore_file = "highscore.txt"
try:
    with open(highscore_file, "r") as file:
        highscore_data = file.read().strip().split(",")
        highscore = int(highscore_data[0])
        highscore_holder = highscore_data[1]
except (FileNotFoundError, ValueError, IndexError):
    highscore = 0
    highscore_holder = "None"

# Sunset cycle
sunset_active = False
sunset_duration = 30 * 1000  # 30 seconds
sunset_interval = 60 * 1000  # Every 60 seconds

# Clouds
clouds = []
cloud_speed = 1
num_clouds = 5

# Function to initialize clouds
def init_clouds():
    for _ in range(num_clouds):
        x = random.randint(0, WIDTH)
        y = random.randint(50, HEIGHT // 2)
        width = random.randint(50, 100)
        height = random.randint(20, 50)
        clouds.append(pygame.Rect(x, y, width, height))

# Function to update and draw clouds
def draw_clouds():
    for cloud in clouds:
        pygame.draw.ellipse(screen, CLOUD_COLOR, cloud)
        cloud.x -= cloud_speed  # Move the cloud left
        if cloud.right < 0:  # Reset the cloud when it goes off-screen
            cloud.x = WIDTH
            cloud.y = random.randint(50, HEIGHT // 2)
            cloud.width = random.randint(50, 100)
            cloud.height = random.randint(20, 50)

# Function to draw planes
def draw_plane(screen, x, y, color):
    pygame.draw.polygon(screen, color, [(x, y), (x - 20, y + 10), (x - 20, y - 10)])  # Body
    pygame.draw.rect(screen, color, (x - 30, y - 5, 10, 10))  # Tail

# Function to draw Twin Towers
def draw_twin_towers():
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH // 8, GROUND_LEVEL - 200, 100, 200))
    pygame.draw.rect(screen, BLACK, (WIDTH // 8 + 20, GROUND_LEVEL - 230, 60, 30))
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH // 8 + 120, GROUND_LEVEL - 250, 100, 250))
    pygame.draw.rect(screen, BLACK, (WIDTH // 8 + 140, GROUND_LEVEL - 280, 60, 30))

# Function to handle name input
def handle_name_input():
    global player1_name, player2_name
    input_box1_active = True
    input_box2_active = False
    input_box1_text = ""
    input_box2_text = ""
    
    player_names_done = False
    while not player_names_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if input_box1_active:
                    if event.key == pygame.K_RETURN:
                        input_box1_active = False
                        input_box2_active = True
                    elif event.key == pygame.K_BACKSPACE:
                        input_box1_text = input_box1_text[:-1]
                    else:
                        input_box1_text += event.unicode
                elif input_box2_active:
                    if event.key == pygame.K_RETURN:
                        input_box2_active = False
                        player_names_done = True
                    elif event.key == pygame.K_BACKSPACE:
                        input_box2_text = input_box2_text[:-1]
                    else:
                        input_box2_text += event.unicode

        screen.fill(WHITE)

        prompt_text1 = font.render("Enter Player 1 Name:", True, BLACK)
        prompt_text2 = font.render("Enter Player 2 Name:", True, BLACK)

        screen.blit(prompt_text1, (WIDTH // 4 - 100, HEIGHT // 3 - 50))
        screen.blit(prompt_text2, (3 * WIDTH // 4 - 100, HEIGHT // 3 - 50))

        pygame.display.flip()
        clock.tick(FPS)
    
    player1_name = input_box1_text or "Player 1"
    player2_name = input_box2_text or "Player 2"

# Main game loop
def main_game():
    global score1, score2, highscore, highscore_holder, sunset_active
    running = True
    init_clouds()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Game logic
        screen.fill(WHITE)

        # Draw elements
        draw_clouds()

        # Draw planes
        draw_plane(screen, plane1_rect.x, plane1_rect.y, plane1_color)
        draw_plane(screen, plane2_rect.x, plane2_rect.y, plane2_color)

        # Draw Twin Towers
        draw_twin_towers()

        # Draw score
        score_text1 = font.render(f"{player1_name}: {score1}", True, BLACK)
        score_text2 = font.render(f"{player2_name}: {score2}", True, BLACK)
        screen.blit(score_text1, (10, 10))
        screen.blit(score_text2, (WIDTH - score_text2.get_width() - 10, 10))

        pygame.display.flip()
        clock.tick(FPS)

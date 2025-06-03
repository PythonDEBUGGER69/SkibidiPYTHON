try:
    import pygame
except ImportError:
    import subprocess
    import sys
    print("Pygame not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

# Now, Pygame should be imported normally
import pygame
import sys
import random  # Import random module

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("qwertyuioasdfghjk")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 10)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Plane properties
plane1_color = RED
plane2_color = BLUE
plane1_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2, 50, 30)
plane2_rect = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, 50, 30)

# Physics properties
gravity = 0.5
lift = -10
thrust = 5
velocity1 = [0, 0]  # [velocity_x, velocity_y] for plane 1
velocity2 = [0, 0]  # [velocity_x, velocity_y] for plane 2

# Boundaries
GROUND_LEVEL = HEIGHT - 50

# Get player names
player1_name = input("Enter Player 1 name: ") or "Player 1"
player2_name = input("Enter Player 2 name: ") or "Player 2"

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

font = pygame.font.Font(None, 36)

# Obstacles
obstacle_color = (0, 0, 0)
obstacle_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 100)
obstacle_velocity = -5

# Function to draw a plane as a shape
def draw_plane(screen, x, y, color):
    pygame.draw.polygon(screen, color, [(x, y), (x - 20, y + 10), (x - 20, y - 10)])  # Body
    pygame.draw.rect(screen, color, (x - 30, y - 5, 10, 10))  # Tail

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses for player 1 and player 2
    keys = pygame.key.get_pressed()

    # Player 1 controls (Arrow keys)
    if keys[pygame.K_UP]:
        velocity1[1] += lift
    if keys[pygame.K_DOWN]:
        velocity1[1] += gravity
    if keys[pygame.K_LEFT]:
        velocity1[0] -= thrust
    if keys[pygame.K_RIGHT]:
        velocity1[0] += thrust

    # Player 2 controls (WASD keys)
    if keys[pygame.K_w]:
        velocity2[1] += lift
    if keys[pygame.K_s]:
        velocity2[1] += gravity
    if keys[pygame.K_a]:
        velocity2[0] -= thrust
    if keys[pygame.K_d]:
        velocity2[0] += thrust

    # Apply gravity
    velocity1[1] += gravity
    velocity2[1] += gravity

    # Update plane positions
    plane1_rect.x += velocity1[0]
    plane1_rect.y += velocity1[1]
    plane2_rect.x += velocity2[0]
    plane2_rect.y += velocity2[1]

    # Prevent the planes from going off-screen
    for plane_rect, velocity in [(plane1_rect, velocity1), (plane2_rect, velocity2)]:
        if plane_rect.right > WIDTH:
            plane_rect.right = WIDTH
            velocity[0] = 0
        if plane_rect.left < 0:
            plane_rect.left = 0
            velocity[0] = 0
        if plane_rect.bottom > GROUND_LEVEL:
            plane_rect.bottom = GROUND_LEVEL
            velocity[1] = 0
        if plane_rect.top < 0:
            plane_rect.top = 0
            velocity[1] = 0

    # Move obstacle
    obstacle_rect.x += obstacle_velocity
    if obstacle_rect.right < 0:
        obstacle_rect.left = WIDTH
        obstacle_rect.y = random.randint(50, HEIGHT - 150)  # Use random.randint

        # Award points for avoiding the obstacle
        score1 += 1
        score2 += 1

    # Check for collisions with the obstacle
    if plane1_rect.colliderect(obstacle_rect):
        score1 -= 1  # Deduct a point on collision
        obstacle_rect.left = WIDTH  # Reset obstacle
    if plane2_rect.colliderect(obstacle_rect):
        score2 -= 1  # Deduct a point on collision
        obstacle_rect.left = WIDTH  # Reset obstacle

    # Update highscore and highscore holder
    if score1 > highscore:
        highscore = score1
        highscore_holder = player1_name
    if score2 > highscore:
        highscore = score2
        highscore_holder = player2_name

    # Draw background
    screen.fill(BLUE)

    # Draw ground
    pygame.draw.rect(screen, GRAY, (0, GROUND_LEVEL, WIDTH, HEIGHT - GROUND_LEVEL))

    # Draw planes
    draw_plane(screen, plane1_rect.centerx, plane1_rect.centery, plane1_color)
    draw_plane(screen, plane2_rect.centerx, plane2_rect.centery, plane2_color)

    # Draw obstacle
    pygame.draw.rect(screen, obstacle_color, obstacle_rect)

    # Display scores and highscore
    score_text1 = font.render(f"{player1_name} Score: {score1}", True, WHITE)
    score_text2 = font.render(f"{player2_name} Score: {score2}", True, WHITE)
    highscore_text = font.render(f"Highscore: {highscore} by {highscore_holder}", True, WHITE)
    screen.blit(score_text1, (10, 10))
    screen.blit(score_text2, (10, 50))
    screen.blit(highscore_text, (WIDTH // 2 - 150, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Save highscore and holder to file
with open(highscore_file, "w") as file:
    file.write(f"{highscore},{highscore_holder}")

# Quit Pygame
pygame.quit()
sys.exit()

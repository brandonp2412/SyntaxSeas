import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Syntax Seas")

# Colors
OCEAN_BLUE = (0, 105, 148)
LIGHT_BLUE = (173, 216, 230)
SAND_COLOR = (238, 214, 175)
LOG_COLOR = (160, 82, 45)
TEXT_COLOR = (255, 69, 0)

# Player
player_width = 60
player_height = 60
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 60, player_width, player_height)
player_speed = 10

# Load and scale the sailboat sprite
sailboat_sprite = pygame.image.load('sail.png')
sailboat_sprite = pygame.transform.scale(sailboat_sprite, (player_width, player_height))

# Logs
log_width = 100
log_height = 40
log_speed = 3
logs = []

# Game variables
clock = pygame.time.Clock()
game_over = False
win = False

def create_log():
    y = random.randint(100, HEIGHT - 150)
    log = pygame.Rect(WIDTH, y, log_width, log_height)
    logs.append(log)

def move_logs():
    for log in logs:
        log.x -= log_speed
        if log.right < 0:
            logs.remove(log)

def draw_gradient_background():
    for y in range(HEIGHT):
        r = int(OCEAN_BLUE[0] * (1 - y/HEIGHT) + LIGHT_BLUE[0] * (y/HEIGHT))
        g = int(OCEAN_BLUE[1] * (1 - y/HEIGHT) + LIGHT_BLUE[1] * (y/HEIGHT))
        b = int(OCEAN_BLUE[2] * (1 - y/HEIGHT) + LIGHT_BLUE[2] * (y/HEIGHT))
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

def draw_objects():
    draw_gradient_background()
    pygame.draw.rect(screen, SAND_COLOR, (0, 0, WIDTH, 50))  # Start area
    pygame.draw.rect(screen, SAND_COLOR, (0, HEIGHT - 50, WIDTH, 50))  # End area
    screen.blit(sailboat_sprite, (player.x, player.y))
    for log in logs:
        pygame.draw.rect(screen, LOG_COLOR, log)

def check_collision():
    player_hitbox = pygame.Rect(player.x + player_width//4, player.y + player_height//2, player_width//2, player_height//2)
    for log in logs:
        if player_hitbox.colliderect(log):
            return True
    return False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over and not win:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
            player.y += player_speed
        if keys[pygame.K_q]:
            running = False

        # Create new logs
        if random.randint(1, 60) == 1:
            create_log()

        move_logs()

        # Check for collision
        if check_collision():
            game_over = True

        # Check for win condition
        if player.top <= 50:
            win = True

    draw_objects()

    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over!", True, TEXT_COLOR)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    if win:
        font = pygame.font.Font(None, 74)
        text = font.render("You Win!", True, TEXT_COLOR)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ocean Crossing")

# Colors
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Player
player_width = 40
player_height = 60
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10, player_width, player_height)
player_speed = 5

# Logs
log_width = 100
log_height = 40
log_speed = 3
logs = []

# Game variables
clock = pygame.time.Clock()
game_over = False
win = False

def draw_sailboat(screen, x, y, width, height):
    # Draw the hull
    pygame.draw.polygon(screen, (139, 69, 19), [(x, y + height), (x + width, y + height), (x + width//2, y + height//2)])
    
    # Draw the sail
    pygame.draw.polygon(screen, WHITE, [(x + width//2, y + height//2), (x + width//2, y), (x + width, y + height//2)])
    
    # Draw the mast
    pygame.draw.line(screen, (101, 67, 33), (x + width//2, y + height//2), (x + width//2, y), 2)

def create_log():
    y = random.randint(100, HEIGHT - 150)
    log = pygame.Rect(WIDTH, y, log_width, log_height)
    logs.append(log)

def move_logs():
    for log in logs:
        log.x -= log_speed
        if log.right < 0:
            logs.remove(log)

def draw_objects():
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, 50))  # Start area
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 50, WIDTH, 50))  # End area
    draw_sailboat(screen, player.x, player.y, player_width, player_height)
    for log in logs:
        pygame.draw.rect(screen, BROWN, log)

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
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    if win:
        font = pygame.font.Font(None, 74)
        text = font.render("You Win!", True, GREEN)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
import random
import math

# Constants
WIDTH = 800
HEIGHT = 600
OCEAN_BLUE = (0, 105, 148)
LIGHT_BLUE = (173, 216, 230)
SAND_COLOR = (238, 214, 175)
TEXT_COLOR = (255, 69, 0)

# Game state
player_width = 60
player_height = 60
log_width = 120
log_height = 30

def init_game(caption='Syntax seas'):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(caption)
    
    player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 60, player_width, player_height)
    sailboat_sprite = pygame.image.load('sail.png')
    sailboat_sprite = pygame.transform.scale(sailboat_sprite, (player_width, player_height))
    
    logs = []
    clock = pygame.time.Clock()
    game_over = False
    win = False
    
    return screen, player, sailboat_sprite, logs, clock, game_over, win

def create_log(logs):
    y = random.randint(100, HEIGHT - 150)
    log = {
        'rect': pygame.Rect(WIDTH, y, log_width, log_height),
        'color': (random.randint(100, 160), random.randint(50, 82), random.randint(20, 45)),
        'rings': random.randint(3, 6)
    }
    logs.append(log)

def move_logs(logs, speed):
    for log in logs:
        log['rect'].x -= speed
        if log['rect'].right < 0:
            logs.remove(log)

def draw_gradient_background(screen):
    for y in range(HEIGHT):
        r = int(OCEAN_BLUE[0] * (1 - y/HEIGHT) + LIGHT_BLUE[0] * (y/HEIGHT))
        g = int(OCEAN_BLUE[1] * (1 - y/HEIGHT) + LIGHT_BLUE[1] * (y/HEIGHT))
        b = int(OCEAN_BLUE[2] * (1 - y/HEIGHT) + LIGHT_BLUE[2] * (y/HEIGHT))
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

def draw_log(screen, log):
    pygame.draw.ellipse(screen, log['color'], log['rect'])
    
    end_color = tuple(max(0, c-20) for c in log['color'])
    pygame.draw.ellipse(screen, end_color,
                        (log['rect'].left, log['rect'].top, log['rect'].height, log['rect'].height))
    pygame.draw.ellipse(screen, end_color,
                        (log['rect'].right-log['rect'].height, log['rect'].top, log['rect'].height, log['rect'].height))
    
    ring_color = tuple(max(0, c-40) for c in log['color'])
    for i in range(log['rings']):
        ring_pos = log['rect'].width * (i + 1) / (log['rings'] + 1)
        pygame.draw.arc(screen, ring_color,
                        (log['rect'].left + ring_pos - 5, log['rect'].top, 10, log['rect'].height),
                        math.pi/2, 3*math.pi/2, 2)

def draw_objects(screen, player, sailboat_sprite, logs):
    draw_gradient_background(screen)
    pygame.draw.rect(screen, SAND_COLOR, (0, 0, WIDTH, 50))
    pygame.draw.rect(screen, SAND_COLOR, (0, HEIGHT - 50, WIDTH, 50))
    screen.blit(sailboat_sprite, (player.x, player.y))
    for log in logs:
        draw_log(screen, log)

def check_collision(player, logs):
    player_hitbox = pygame.Rect(player.x + player_width//4, player.y + player_height//2, player_width//2, player_height//2)
    for log in logs:
        log_hitbox = pygame.Rect(log['rect'].left + log['rect'].height//2, log['rect'].top,
                                 log['rect'].width - log['rect'].height, log['rect'].height)
        if player_hitbox.colliderect(log_hitbox):
            return True
    return False

def run_game(player_speed=10, log_speed=3, caption='Syntax seas'):
    screen, player, sailboat_sprite, logs, clock, game_over, win = init_game(caption)
    
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

            if random.randint(1, 60) == 1:
                create_log(logs)

            move_logs(logs, log_speed)

            if check_collision(player, logs):
                game_over = True

            if player.top <= 50:
                win = True

        draw_objects(screen, player, sailboat_sprite, logs)

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
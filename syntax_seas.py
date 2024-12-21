import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
OCEAN_BLUE = (0, 105, 148)
LIGHT_BLUE = (173, 216, 230)
SAND_COLOR = (238, 214, 175)
TEXT_COLOR = (255, 105, 50)

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
    sailboat_sprite = pygame.image.load('sailboat.png')
    sailboat_sprite = pygame.transform.scale(sailboat_sprite, (player_width, player_height))
    
    log_sprite = pygame.image.load('log.png')
    log_sprite = pygame.transform.scale(log_sprite, (log_width, log_height))
    
    logs = []
    clock = pygame.time.Clock()
    game_over = False
    win = False
    
    return screen, player, sailboat_sprite, log_sprite, logs, clock, game_over, win

def create_log(logs):
    y = random.randint(100, HEIGHT - 150)
    log = {
        'rect': pygame.Rect(WIDTH, y, log_width, log_height),
    }
    logs.append(log)

def move_logs(logs, speed):
    for log in logs:
        log['rect'].x -= speed
        if log['rect'].right < 0:
            logs.remove(log)

def draw_objects(screen, player, sailboat_sprite, log_sprite, logs):
    ocean = pygame.image.load('ocean.png')
    ocean = pygame.transform.scale(ocean, (WIDTH, HEIGHT))
    screen.blit(ocean, (0, 0))
    screen.blit(sailboat_sprite, (player.x, player.y))
    for log in logs:
        screen.blit(log_sprite, log['rect'])

def check_collision(player, logs):
    player_hitbox = pygame.Rect(player.x + player_width//4, player.y + player_height//2, player_width//2, player_height//2)
    for log in logs:
        log_hitbox = pygame.Rect(log['rect'].left + log['rect'].height//2, log['rect'].top,
                                 log['rect'].width - log['rect'].height, log['rect'].height)
        if player_hitbox.colliderect(log_hitbox):
            return True
    return False

def run_game(player_speed=10, log_speed=3, caption='Syntax seas'):
    screen, player, sailboat_sprite, log_sprite, logs, clock, game_over, win = init_game(caption)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            running = False
            
        if keys[pygame.K_r]:
            game_over = False
            win = False
            player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 60, player_width, player_height)

        if not game_over and not win:
            if keys[pygame.K_LEFT] and player.left > 0:
                player.x -= player_speed
            if keys[pygame.K_RIGHT] and player.right < WIDTH:
                player.x += player_speed
            if keys[pygame.K_UP] and player.top > 0:
                player.y -= player_speed
            if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
                player.y += player_speed

            if random.randint(1, 30) == 1:
                create_log(logs)

            move_logs(logs, log_speed)

            if check_collision(player, logs):
                game_over = True

            if player.top <= 0:
                win = True

        draw_objects(screen, player, sailboat_sprite, log_sprite, logs)

        if game_over:
            font = pygame.font.Font(None, 74)
            font_small = pygame.font.Font(None, 36)
            text = font.render("Game Over!", True, TEXT_COLOR)
            quit_text = font_small.render("Press 'q' to quit, 'r' to restart", True, TEXT_COLOR)
            quit_text_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
            screen.blit(quit_text, quit_text_rect)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        if win:
            font_large = pygame.font.Font(None, 74)
            font_small = pygame.font.Font(None, 36)

            win_text = font_large.render("You Win!", True, TEXT_COLOR)
            quit_text = font_small.render("Press 'q' to quit, 'r' to restart", True, TEXT_COLOR)

            win_text_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
            quit_text_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))

            screen.blit(win_text, win_text_rect)
            screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    
if __name__ == '__main__':
    run_game()
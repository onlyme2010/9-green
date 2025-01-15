import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player settings
player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Bullet settings
bullet_width, bullet_height = 5, 10
bullets = []
bullet_speed = 7

# Enemy settings
enemy_width, enemy_height = 50, 50
enemies = []
enemy_speed = 3
enemy_spawn_time = 1000  # milliseconds
pygame.time.set_timer(pygame.USEREVENT, enemy_spawn_time)

# Game loop control
running = True
clock = pygame.time.Clock()

# Main game loop
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            # Spawn an enemy
            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemies.append([enemy_x, 0])  # Start at the top of the screen

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        # Shoot bullet
        if len(bullets) < 10:  # Limit number of bullets on screen
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # Update bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Update enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], enemy_width, enemy_height))

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()



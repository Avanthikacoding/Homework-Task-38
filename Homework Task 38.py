import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Add More Sprites - Space Invader Project Part 1")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

player = pygame.Rect(400, 300, 40, 40)

enemies = []
for i in range(7):
    x = random.randint(0, 760)
    y = random.randint(0, 560)
    enemies.append(pygame.Rect(x, y, 40, 40))

score = 0
font = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    player.x = max(0, min(760, player.x))
    player.y = max(0, min(560, player.y))

    for enemy in enemies:
        if player.colliderect(enemy):
            score = score + 1
            enemy.x = random.randint(0, 760)
            enemy.y = random.randint(0, 560)

    pygame.draw.rect(screen, GREEN, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

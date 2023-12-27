import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy
from constants import S_WIDTH, S_HEIGHT, TITLE, B_INIT_COOLDOWN, E_INIT_COOLDOWN
import random

pygame.init()

if __name__ == '__main__':
    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    pygame.display.set_caption(f'{TITLE: ^{S_WIDTH / 3.5}}')
    clock = pygame.time.Clock()
    player = Player(400, 300)

    bullets = []
    enemies = []

    b_sTime = pygame.time.get_ticks()
    e_sTime = b_sTime
    b_cD = B_INIT_COOLDOWN
    e_cD = E_INIT_COOLDOWN
    while True:
        keys = pygame.key.get_pressed()
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit

        cTime = pygame.time.get_ticks()

        player.move(keys)

        m_x, m_y = pygame.mouse.get_pos()

        if cTime - b_sTime >= b_cD:
            b_sTime = pygame.time.get_ticks()
            new_bullet = Bullet(player.posX + player.size / 2, player.posY + player.size / 2, m_x, m_y)
            bullets.append(new_bullet)

        if cTime - e_sTime >= e_cD:
            e_sTime = pygame.time.get_ticks()

            tX = random.randint(1, S_WIDTH - 1)
            tY = random.randint(1, S_HEIGHT - 1)
            new_enemy = Enemy(tX, tY)
            enemies.append(new_enemy)

        for bullet in bullets:
            bullet.move()

        for enemy in enemies:
            enemy.move(player.posX, player.posY, enemies)

        # ===================================================================================== #

        bullets_to_remove = []
        for i, bullet in enumerate(bullets):
            if bullet.posX < 0 or bullet.posX > S_WIDTH:
                bullets_to_remove.append(i)

            if bullet.posY < 0 or bullet.posY > S_HEIGHT:
                bullets_to_remove.append(i)

        for i in bullets_to_remove:
            try:
                bullets.pop(i)
            except IndexError:
                continue
        # ===================================================================================== #

        screen.fill((0, 0, 0))  # Fill the display with a solid color

        for bullet in bullets:
            bullet.draw(screen)

        player.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        # Render the graphics here.

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)  # wait until next frame (at 60 FPS)

import time
from utils import *
from constants import *
import math

pygame.init()

if __name__ == '__main__':
    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    pygame.display.set_caption(f'{TITLE: ^{S_WIDTH / 3.5}}')
    clock = pygame.time.Clock()
    font = pygame.font.Font('Black Hulk.otf', 64)

    player = Player(400, 300)

    pause_game = False

    bullets = []
    enemies = []
    gems = []

    b_sTime = pygame.time.get_ticks()
    e_sTime = b_sTime
    b_cD = B_INIT_COOLDOWN
    e_cD = E_INIT_COOLDOWN

    while True:
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_p]:
            pause_game = not pause_game
            time.sleep(0.1)
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit

        if is_game_over(player):

            msg = font.render('game over', True, FONT_COLOR, BACKGROUND_COLOR)
            msg_rect = msg.get_rect()
            msg_rect.center = (S_WIDTH // 2, S_HEIGHT // 2 - 50)
            screen.blit(msg, msg_rect)

            msg = font.render('press R to restart', True, FONT_COLOR, BACKGROUND_COLOR)
            msg_rect = msg.get_rect()
            msg_rect.center = (S_WIDTH // 2, S_HEIGHT // 2 + 50)
            screen.blit(msg, msg_rect)

            pygame.display.flip()

            if keys_pressed[pygame.K_r]:
                player = Player(400, 300)
                pause_game = False
                bullets = []
                enemies = []
                gems = []

            continue

        if not pause_game:

            if is_lvl_up(player):
                player.curr_exp = player.curr_exp - player.exp_needed
                player.lvl += 1 if player.lvl < 100 else 0
                player.exp_needed = math.ceil(LVL_SCALING * player.exp_needed)

            cTime = pygame.time.get_ticks()

            player.move(keys_pressed)

            m_x, m_y = pygame.mouse.get_pos()

            if cTime - b_sTime >= b_cD:
                b_sTime = pygame.time.get_ticks()
                new_bullet = Bullet(player.posX + player.size / 2, player.posY + player.size / 2, m_x, m_y)
                bullets.append(new_bullet)

            if len(enemies) < SPAWN_CAP:
                e_sTime = spawn_constant_enemy(enemies, e_sTime, cTime, e_cD, player)

            for bullet in bullets:
                bullet.move()

            for gem in gems:
                gem.move(player.posX, player.posY)

            for enemy in enemies:
                enemy.move(player.posX, player.posY)

            # ===================================================================================== #

            enemies = enemy_enemy_collision(enemies)
            enemies, bullets = normal_bullet_enemy_collision(enemies, bullets, gems)
            enemy_player_collision(enemies, player)
            gems = gem_player_collision(gems, player)

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

        screen.fill(BACKGROUND_COLOR)  # Fill the display with a solid color
        for bullet in bullets:
            bullet.draw(screen)

        for gem in gems:
            gem.draw(screen)

        player.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        if pause_game:
            msg = font.render('game paused', True, FONT_COLOR, BACKGROUND_COLOR)
            msg_rect = msg.get_rect()
            msg_rect.center = (S_WIDTH // 2, S_HEIGHT // 2)
            screen.blit(msg, msg_rect)
        # Render the graphics here.

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)  # wait until next frame (at 60 FPS)

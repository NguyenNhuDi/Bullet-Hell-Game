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

    dmg = add_dmg(0)
    collect_dist = COLLECT_DIST

    player = Player(400, 300)

    pause_game = False

    bullets = []
    enemies = []
    gems = []
    m_stars = spawn_m_star(400, 300, 0)

    b_sTime = pygame.time.get_ticks()
    e_sTime = b_sTime
    b_cD = B_INIT_COOLDOWN
    e_cD = E_INIT_COOLDOWN

    # test_box_1 = Button(50, 100, 'hello world', ADD_HP)
    # test_box_2 = Button(300, 100, 'hello world', ADD_DMG)
    # test_box_3 = Button(550, 100, 'hello world', ADD_SPEED)

    buttons = []
    pos = 0
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
                test_box_1 = Button(50, 100, 'hello world', ADD_HP)
                test_box_2 = Button(300, 100, 'hello world', ADD_DMG)
                test_box_3 = Button(550, 100, 'hello world', ADD_SPEED)

                buttons.append(test_box_1)
                buttons.append(test_box_2)
                buttons.append(test_box_3)
                left_button_pressed = False
                while True:
                    keys_pressed = pygame.key.get_pressed()

                    display_game(screen, bullets, gems, m_stars, player, enemies, buttons, pause_game, font)

                    if len(buttons) == 1:
                        ...
                    elif len(buttons) == 2:
                        ...
                    else:

                        buttons[pos].color = (255, 0, 0)
                        if keys_pressed[pygame.K_LEFT] and not left_button_pressed:
                            left_button_pressed = True
                            buttons[pos].color = (168, 227, 197)

                            if pos == 0:
                                pos = 2
                            else:
                                pos -= 1

                        if not keys_pressed[pygame.K_LEFT]:
                            left_button_pressed = False
                    pygame.event.pump()

                player.curr_exp = player.curr_exp - player.exp_needed
                player.lvl += 1 if player.lvl < 50 else 0
                player.exp_needed = math.ceil(LVL_SCALING * player.exp_needed)

            cTime = pygame.time.get_ticks()

            player.move(keys_pressed)

            m_x, m_y = pygame.mouse.get_pos()

            b_sTime = spawn_bullet(bullets, m_x, m_y, b_sTime, cTime, b_cD, player, 1, 5, 5, dmg)

            regen_hp(player, cTime)

            if len(enemies) < SPAWN_CAP:
                e_sTime = spawn_constant_enemy(enemies, e_sTime, cTime, e_cD, player)

            for bullet in bullets:
                bullet.move()

            for gem in gems:
                gem.move(player.posX, player.posY)

            for enemy in enemies:
                enemy.move(player.posX, player.posY)

            for m_star in m_stars:
                m_star.move(player.posX, player.posY)

            # ===================================================================================== #

            enemies = enemy_enemy_collision(enemies)
            enemies = morning_star_enemy_collision(enemies, m_stars, gems)
            enemies, bullets = bullet_enemy_collision(enemies, bullets, gems)
            enemy_player_collision(enemies, player)
            gems = gem_player_collision(gems, player, collect_dist)

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

        display_game(screen, bullets, gems, m_stars, player, enemies, buttons, pause_game, font)

        clock.tick(60)

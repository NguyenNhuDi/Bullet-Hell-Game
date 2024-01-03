import math
from typing import List, Tuple
import random
from enemy import Enemy
from player import Player
from bullet import Bullet
from gem import Gem
from mStar import MorningStar
from constants import S_WIDTH, S_HEIGHT, SPAWN_DISTANCE, E_DMG, E_VEL, COLLECT_DIST, SIZE_FACTOR, B_CD, B_SIZE_0, \
    B_SIZE_1, B_SIZE_2, B_SIZE_3, B_SIZE_4, B_SIZE_5
import pygame


def spawn_bullet(bullets: List[Bullet], m_x: int, m_y: int, b_sTime: int, c_time: int, b_cD: int, player: Player,
                 bullet_num: int = 1, bullet_hp: int = 1, split_lvl: int = 0) -> int:
    if c_time - b_sTime >= b_cD:

        angle_diff = 2 * math.pi / bullet_num

        b_size = B_SIZE_0

        if split_lvl == 1:
            b_size = B_SIZE_1
        elif split_lvl == 2:
            b_size = B_SIZE_2
        elif split_lvl == 3:
            b_size = B_SIZE_3
        elif split_lvl == 4:
            b_size = B_SIZE_2
        elif split_lvl == 5:
            b_size = B_SIZE_5

        for i in range(bullet_num):
            curr_bullet = Bullet(player.posX + player.size / 2, player.posY + player.size / 2, m_x, m_y, hp=bullet_hp,
                                 split=True if split_lvl > 0 else False, split_amount=split_lvl, size=b_size)
            curr_bullet.angle = curr_bullet.angle + i * angle_diff

            bullets.append(curr_bullet)

        b_sTime = pygame.time.get_ticks()

    return b_sTime


# spawn the enemy for constant intervals
def spawn_constant_enemy(enemies: List[Enemy], e_sTime: int, c_time: int, e_cD: int, player: Player) -> int:
    if c_time - e_sTime >= e_cD:
        e_sTime = pygame.time.get_ticks()

        tX = random.randint(1, S_WIDTH - 1)
        tY = random.randint(1, S_HEIGHT - 1)

        distance = ((tX - player.posX) ** 2 + (tY - player.posY) ** 2) ** 0.5

        while distance < SPAWN_DISTANCE:
            tX = random.randint(1, S_WIDTH - 1)
            tY = random.randint(1, S_HEIGHT - 1)
            distance = ((tX - player.posX) ** 2 + (tY - player.posY) ** 2) ** 0.5

        new_enemy = Enemy(tX, tY)
        enemies.append(new_enemy)

    return e_sTime


# spawn a gem
def spawn_gem(gems: List[Gem], x, y) -> None:
    new_gem = Gem(x, y)
    gems.append(new_gem)


def spawn_m_star(pX: int, pY: int, nums: int) -> List[MorningStar]:
    if nums == 0:
        return []

    out_m_stars = []
    angle_diff = math.pi * 2 / nums

    for i in range(nums):
        curr_star = MorningStar(pX, pY, angle_diff * i)
        out_m_stars.append(curr_star)

    return out_m_stars


# enemy on enemy collision
def enemy_enemy_collision(enemies: List) -> List[Enemy]:
    new_enemies = []

    for i, enemy_1 in enumerate(enemies):
        if enemy_1 == -1:
            continue

        for j, enemy_2 in enumerate(enemies):
            if i == j or enemy_2 == -1:
                continue

            x_offset = enemy_1.posX - enemy_2.posX
            y_offset = enemy_1.posY - enemy_2.posY

            if enemy_2.mask.overlap(enemy_1.mask, (x_offset, y_offset)):

                if enemy_1.size >= enemy_2.size:
                    max_size = enemy_1.size
                    min_size = enemy_2.size

                    new_x = enemy_1.posX
                    new_y = enemy_1.posY
                else:
                    max_size = enemy_2.size
                    min_size = enemy_1.size

                    new_x = enemy_2.posX
                    new_y = enemy_2.posY

                new_enemy = Enemy(new_x, new_y)
                new_enemy.size = (min_size * SIZE_FACTOR) + max_size
                new_enemy.vel = new_enemy.size / E_VEL
                new_enemy.hp = enemy_1.hp + enemy_2.hp
                new_enemy.max_hp = enemy_1.max_hp + enemy_2.max_hp

                new_enemies.append(new_enemy)

                enemies[i] = -1
                enemies[j] = -1

    enemies += new_enemies
    enemies = set(enemies)
    enemies = list(enemies)

    return enemies


def morning_star_enemy_collision(enemies: List, m_stars: List[MorningStar], gems: List[Gem]) -> List[Enemy]:
    for i, m_star in enumerate(m_stars):

        for j, enemy in enumerate(enemies):
            if enemy == -1:
                continue

            x_offset = enemy.posX - m_star.posX
            y_offset = enemy.posY - m_star.posY

            # m_star collided with this enemy
            if m_star.mask.overlap(enemy.mask, (x_offset, y_offset)):
                enemy.hp -= 1
                if enemy.hp <= 0:
                    spawn_gem(gems, enemy.posX, enemy.posY)
                    enemies[j] = -1

    out_enemies = []

    for i in enemies:
        if i == -1:
            continue
        out_enemies.append(i)

    return out_enemies


def split_bullet(bullets: List[Bullet], bullet: Bullet, curr_lvl: int):
    angle_diff = 2 * math.pi / (curr_lvl + 1)

    b_size = B_SIZE_5

    if curr_lvl == 1:
        b_size = B_SIZE_1
    elif curr_lvl == 2:
        b_size = B_SIZE_2
    elif curr_lvl == 3:
        b_size = B_SIZE_3
    elif curr_lvl == 4:
        b_size = B_SIZE_2

    for k in range(1, curr_lvl + 2):
        c_bullet = Bullet(bullet.posX, bullet.posY, -1, -1, True, split_amount=curr_lvl - 1, hp=bullet.hp, size=b_size)
        c_bullet.angle = bullet.angle + k * angle_diff

        bullets.append(c_bullet)


# normal bullet on enemy collision
def bullet_enemy_collision(enemies: List, bullets: List, gems: List[Gem]) -> Tuple[List[Enemy], List[Bullet]]:
    for i, bullet in enumerate(bullets):

        if bullet == -1:
            continue

        for j, enemy in enumerate(enemies):
            if enemy == -1:
                continue

            x_offset = enemy.posX - bullet.posX
            y_offset = enemy.posY - bullet.posY

            # bullet collided with this enemy
            if bullet.mask.overlap(enemy.mask, (x_offset, y_offset)):
                c_time = pygame.time.get_ticks()
                if c_time - bullet.sTime >= B_CD:
                    bullet.sTime = pygame.time.get_ticks()
                    enemy.hp -= 1

                    if bullet.split:
                        if bullet.split_amount == 1:
                            b1 = Bullet(bullet.posX, bullet.posY, -1, -1, False, hp=bullet.hp)
                            b2 = Bullet(bullet.posX, bullet.posY, -1, -1, False, hp=bullet.hp)

                            b1.angle = bullet.angle - math.pi / 3
                            b2.angle = bullet.angle + math.pi / 3

                            bullets.append(b1)
                            bullets.append(b2)
                        else:
                            split_bullet(bullets, bullet, bullet.split_amount)
                    bullet.hp -= 1

            if enemy.hp <= 0:
                spawn_gem(gems, enemy.posX, enemy.posY)
                enemies[j] = -1

            if bullet.hp <= 0:
                bullets[i] = -1

    out_enemies = []
    out_bullets = []

    for i in enemies:
        if i == -1:
            continue
        out_enemies.append(i)

    for j in bullets:
        if j == -1:
            continue
        out_bullets.append(j)

    return out_enemies, out_bullets


# enemy player collision
def enemy_player_collision(enemies: List[Enemy], player: Player) -> None:
    c_time = pygame.time.get_ticks()

    for i, enemy in enumerate(enemies):
        x_offset = enemy.posX - player.posX
        y_offset = enemy.posY - player.posY

        x_offset *= x_offset
        y_offset *= y_offset

        dist = (x_offset + y_offset) ** 0.5

        max_dist = (enemy.size ** 2 + player.size ** 2) ** 0.5

        if dist <= max_dist:
            enemy.vel = 0
            if c_time - player.sTime >= player.iframe:
                player.sTime = pygame.time.get_ticks()
                player.hp -= E_DMG
        else:
            enemy.vel = enemy.size / E_VEL

        if player.hp <= 0:
            return


# gem plyer collision
def gem_player_collision(gems: List, player: Player) -> List[Gem]:
    r_index = set()

    for i, gem in enumerate(gems):
        if gem == -1:
            continue

        x_offset = gem.posX - player.posX
        y_offset = gem.posY - player.posY

        if player.mask.overlap(gem.mask, (x_offset, y_offset)):
            r_index.add(i)
            player.curr_exp += 1

        # distance management
        x_offset *= x_offset
        y_offset *= y_offset

        dist = (x_offset + y_offset) ** 0.5

        if dist <= COLLECT_DIST:
            gem.vel = player.velX * 2

    out_gems = [gems[i] for i in range(len(gems)) if i not in r_index]
    return out_gems


# ==============================================================================

def is_game_over(player: Player) -> bool:
    return player.hp <= 0


def is_lvl_up(player: Player) -> bool:
    return player.curr_exp >= player.exp_needed

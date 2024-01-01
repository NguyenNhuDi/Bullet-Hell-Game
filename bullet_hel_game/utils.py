from typing import List, Tuple
import random
from enemy import Enemy
from player import Player
from bullet import Bullet
from gem import Gem
from constants import S_WIDTH, S_HEIGHT, SPAWN_DISTANCE, E_DMG, E_VEL, SPEED_FACTOR, SIZE_FACTOR
import pygame


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

                new_enemies.append(new_enemy)

                enemies[i] = -1
                enemies[j] = -1

    enemies += new_enemies
    enemies = set(enemies)
    enemies = list(enemies)

    return enemies


# normal bullet on enemy collision
def normal_bullet_enemy_collision(enemies: List, bullets: List, gems: List[Gem]) -> Tuple[List[Enemy], List[Bullet]]:
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
                bullets[i] = -1

                enemy.hp -= 1
                if enemy.hp <= 0:
                    spawn_gem(gems, enemy.posX, enemy.posY)
                    enemies[j] = -1

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

    out_gems = [gems[i] for i in range(len(gems)) if i not in r_index]
    return out_gems

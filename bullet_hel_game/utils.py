from typing import List, Tuple
import random
from enemy import Enemy
from player import Player
from bullet import Bullet
from gem import Gem
from constants import S_WIDTH, S_HEIGHT, SPAWN_DISTANCE
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


# If the bullet has hit the enemy
def normal_bullet_collision(enemies: List, bullets: List, gems: List[Gem]) -> Tuple[List[Enemy], List[Bullet]]:
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

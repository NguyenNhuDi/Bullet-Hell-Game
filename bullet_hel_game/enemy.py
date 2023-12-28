from entity import Entity
from constants import E_SIZE, SPEED_FACTOR, SIZE_FACTOR, COLOR_FACTOR
import pygame
import math


class Enemy(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

        self.vel = E_VEL

        self.color = [100, 100, 100]  # Red ish
        self.size = E_SIZE

        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color=tuple(self.color))

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # print(mask_offset(self.mask, self.mask))

    def draw(self, screen):
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color=tuple(self.color))
        self.mask = pygame.mask.from_surface(self.image)
        screen.blit(self.image, (self.posX, self.posY))

    def move(self, pX: int, pY: int, enemies):
        n_x = pX - self.posX
        n_y = pY - self.posY

        angle = math.atan2(n_y, n_x)

        vel_x = self.vel * math.cos(angle)
        vel_y = self.vel * math.sin(angle)

        for i, enemy in enumerate(enemies):
            if enemy is self:
                continue
            else:
                x_offset = enemy.posX - self.posX
                y_offset = enemy.posY - self.posY
                if self.mask.overlap(enemy.mask, (x_offset, y_offset)):
                    # they merged :D

                    new_vel = self.vel if self.vel < enemy.vel else enemy.vel
                    new_vel *= SPEED_FACTOR

                    new_size = self.size if self.size > enemy.size else enemy.size
                    new_size *= SIZE_FACTOR

                    self.vel += new_vel
                    self.size += new_size
                    self.color[0] = enemy.color[0] if enemy.color[0] > self.color[0] else self.color[0]
                    self.color[0] += COLOR_FACTOR

                    if self.color[0] >= 255:
                        self.color[0] = 100

                    enemies.pop(i)
                    break

        self.posX += vel_x
        self.posY += vel_y

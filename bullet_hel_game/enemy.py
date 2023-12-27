from entity import Entity
from constants import E_VEL, E_SIZE
import pygame
import math


class Enemy(Entity):
    def __init__(self, x: int, y: int, s_width: int = 800, s_height: int = 600):
        super().__init__(x, y, s_width, s_height)

        self.vel = E_VEL

        self.color = (240, 10, 10)  # Red ish
        self.size = E_SIZE

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.size, self.size))

    def move(self, pX: int, pY: int):
        n_x = pX - self.posX
        n_y = pY - self.posY

        angle = math.atan2(n_y, n_x)

        vel_x = self.vel * math.cos(angle)
        vel_y = self.vel * math.sin(angle)

        self.posX += vel_x
        self.posY += vel_y

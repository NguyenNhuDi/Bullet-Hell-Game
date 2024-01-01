from entity import Entity
from constants import G_SIZE
import pygame
import math


class Gem(Entity):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

        self.color = (26, 219, 55)  # green
        self.size = G_SIZE

        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color=self.color)

        self.mask = pygame.mask.from_surface(self.image)

        self.vel = 0

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, (self.posX, self.posY))

    def move(self, pX: int, pY: int):
        n_x = pX - self.posX
        n_y = pY - self.posY

        angle = math.atan2(n_y, n_x)

        vel_x = self.vel * math.cos(angle)
        vel_y = self.vel * math.sin(angle)

        self.posX += vel_x
        self.posY += vel_y

from entity import Entity
from constants import MSTAR_VEL, MSTAR_SIZE, MSTAR_RADIUS
import pygame
import math


class MorningStar(Entity):
    def __init__(self, pX: int, pY: int, angle: float) -> None:
        x = MSTAR_RADIUS * math.cos(angle) + pX
        y = MSTAR_RADIUS * math.sin(angle) + pY

        super().__init__(x, y)

        self.vel = MSTAR_VEL
        self.angle = angle

        self.color = (38, 43, 128)
        self.size = MSTAR_SIZE

        # Visual things
        self.image = pygame.Surface((self.size, self.size))  # TODO update to image
        self.image.fill(color=self.color)

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, (self.posX, self.posY))

    def move(self, pX: int, pY: int) -> None:
        self.angle += self.vel
        self.posX = MSTAR_RADIUS * math.cos(self.angle) + pX
        self.posY = MSTAR_RADIUS * math.sin(self.angle) + pY

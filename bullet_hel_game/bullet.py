import sys
from constants import B_VEL, B_SIZE_0
import math
import pygame
from entity import Entity


class Bullet(Entity):
    def __init__(self, x: int, y: int, m_x: int, m_y: int, split: bool = False, split_amount: int = 0,
                 hp: int = 1, size: int = B_SIZE_0, dmg: int = 1) -> None:
        if split and split_amount <= 0:
            sys.exit('Split amount is 0 or less when split is true')

        super().__init__(x, y)

        self.split = split
        self.split_amount = split_amount

        # angle and speed calculations
        self.vel = B_VEL

        n_x = m_x - x
        n_y = m_y - y

        self.angle = math.atan2(n_y, n_x)

        self.size = size

        # collision settings
        self.hp = hp

        self.sTime = pygame.time.get_ticks()
        self.fHit = False

        # damage
        self.damage = dmg

        # Visual things
        self.color = (0, 0, 0)  # black
        self.image = pygame.Surface((self.size, self.size))  # TODO update to image
        self.image.fill(color=self.color)

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, (self.posX, self.posY))

    def move(self) -> None:
        velX = self.vel * math.cos(self.angle)
        velY = self.vel * math.sin(self.angle)

        self.posX += velX
        self.posY += velY

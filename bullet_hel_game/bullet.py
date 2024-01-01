from constants import BASIC, SPLIT, HONING, B_VEL, B_SIZE
import math
import pygame
from entity import Entity


class Bullet(Entity):
    def __init__(self, x: int, y: int, m_x: int, m_y: int, b_type=BASIC) -> None:
        super().__init__(x, y)
        self.b_type = b_type

        # angle and speed calculations
        self.vel = B_VEL

        n_x = m_x - x
        n_y = m_y - y

        self.angle = math.atan2(n_y, n_x)

        self.color = (0, 0, 0)  # black
        self.size = B_SIZE

        # Visual things
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

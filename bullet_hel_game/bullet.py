from constants import BASIC, SPLIT, HONING, B_VEL, B_SIZE
import math
import pygame
from entity import Entity


class Bullet(Entity):
    def __init__(self, x: int, y: int, m_x: int, m_y: int, b_type=BASIC) -> None:
        super().__init__(x, y)
        self.b_type = b_type

        # angle and speed calculations
        vel = B_VEL

        n_x = m_x - x
        n_y = m_y - y

        angle = math.atan2(n_y, n_x)

        self.velX = vel * math.cos(angle)
        self.velY = vel * math.sin(angle)

        self.color = (0, 0, 0)  # black
        self.size = B_SIZE

        # Visual things
        self.image = pygame.Surface((self.size, self.size))  # TODO update to image
        self.image.fill(color=self.color)

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, (self.posX, self.posY))

    def move(self) -> None:
        self.posX += self.velX
        self.posY += self.velY

from constants import BASIC, SPLIT, HONING, B_VEL, B_RADIUS
import math
import pygame
from entity import Entity


class Bullet(Entity):
    def __init__(self, x: int, y: int, m_x: int, m_y: int, s_width: int = 800, s_height=600, b_type=BASIC):
        super().__init__(x, y, s_width, s_height)
        self.b_type = b_type

        # angle and speed calculations
        vel = B_VEL

        n_x = m_x - x
        n_y = m_y - y

        angle = math.atan2(n_y, n_x)

        self.velX = vel * math.cos(angle)
        self.velY = vel * math.sin(angle)

        self.color = (50, 168, 82)  # lime green ish
        self.radius = B_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.posX), int(self.posY)), self.radius)

    def move(self):
        self.posX += self.velX
        self.posY += self.velY

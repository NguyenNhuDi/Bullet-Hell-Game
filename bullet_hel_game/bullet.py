from constants import BASIC, SPLIT, HONING
import math
import pygame


class Bullet:
    def __init__(self, x: float, y: float, m_x: float, m_y: float, s_width: int = 800, s_height=600, b_type=BASIC):
        self.posX = x
        self.posY = y

        self.s_width = s_width
        self.s_height = s_height

        self.b_type = b_type

        # angle and speed calculations
        vel = 2

        n_x = m_x - x
        n_y = m_y - y

        angle = math.atan2(n_y, n_x)

        self.velX = vel * math.cos(angle)
        self.velY = vel * math.sin(angle)

        self.color = (50, 168, 82)  # lime green ish
        self.radius = 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.posX), int(self.posY)), self.radius)

    def move(self):
        self.posX += self.velX
        self.posY += self.velY

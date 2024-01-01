from entity import Entity
from constants import E_VEL, E_SIZE, E_HEALTH
import pygame
import math


class Enemy(Entity):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

        self.vel = E_VEL

        self.color = [100, 100, 100]  # Red ish
        self.size = E_SIZE

        self.max_hp = E_HEALTH
        self.hp = E_HEALTH

        # Visual things
        self.image = pygame.Surface((self.size, self.size))  # TODO update to image
        self.image.fill(color=tuple(self.color))

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.surface.Surface) -> None:
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color=tuple(self.color))

        self.mask = pygame.mask.from_surface(self.image)

        red = (255, 0, 0)

        p_hp = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.posX, self.posY - 6, self.size * p_hp, 4))

        screen.blit(self.image, (self.posX, self.posY))

    def move(self, pX: int, pY: int) -> None:
        n_x = pX - self.posX
        n_y = pY - self.posY

        angle = math.atan2(n_y, n_x)

        vel_x = self.vel * math.cos(angle)
        vel_y = self.vel * math.sin(angle)

        self.posX += vel_x
        self.posY += vel_y

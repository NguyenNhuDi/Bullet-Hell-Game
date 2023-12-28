from entity import Entity
from constants import G_SIZE
import pygame


class Gem(Entity):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

        self.color = (26, 219, 55)  # green
        self.size = G_SIZE

        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color=self.color)

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, (self.posX, self.posY))

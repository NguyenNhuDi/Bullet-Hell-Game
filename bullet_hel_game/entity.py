import pygame
from constants import S_WIDTH, S_HEIGHT


class Entity(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.posX = x
        self.posY = y

        self.sWidth = S_WIDTH
        self.sHeight = S_HEIGHT



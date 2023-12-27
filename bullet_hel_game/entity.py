import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, s_width: int = 800, s_height: int = 600):
        super().__init__()

        self.posX = x
        self.posY = y

        self.sWidth = s_width
        self.sHeight = s_height


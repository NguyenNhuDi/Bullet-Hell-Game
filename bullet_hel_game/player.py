import pygame.draw
from entity import Entity
from constants import P_VEL, P_SIZE


class Player(Entity):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

        self.velX = P_VEL
        self.velY = P_VEL

        self.color = (128, 29, 106)  # Purple Pink ish
        self.size = P_SIZE

        self.keys = pygame.key.get_pressed()

        # Visual things
        self.image = pygame.Surface((self.size, self.size))  # TODO update to image
        self.image.fill(color=self.color)

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, (self.posX, self.posY))

    def move(self, keys: pygame.key.ScancodeWrapper) -> None:
        # move left
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.posX >= self.size:
            self.posX -= self.velX
        # move right
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.posX <= self.sWidth - self.size * 2:
            self.posX += self.velX
        # move up
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.posY >= self.size:
            self.posY -= self.velY
        # move down
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.posY <= self.sHeight - self.size * 2:
            self.posY += self.velY

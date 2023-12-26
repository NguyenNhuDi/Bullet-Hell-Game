import pygame.draw


class Player:
    def __init__(self, x: float, y: float, s_width: int = 800, s_height: int = 600):
        self.posX = x
        self.posY = y

        self.sWidth = s_width
        self.sHeight = s_height

        self.velX = 5
        self.velY = 5

        self.color = (128, 29, 106)  # Purple Pink ish
        self.size = 10

        self.keys = pygame.key.get_pressed()

    def draw(self, screen: pygame.surface.Surface):
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.size, self.size))

    def move(self, keys: pygame.key.ScancodeWrapper):
        # move left
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.posX -= self.velX
        # move right
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.posX += self.velX

        # move up
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.posY -= self.velY
        # move down
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.posY += self.velY

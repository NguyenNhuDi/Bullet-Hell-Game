import pygame.draw
from entity import Entity
from constants import P_VEL, P_SIZE, PLAYER_INIT_HP


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

        self.max_hp = PLAYER_INIT_HP
        self.hp = PLAYER_INIT_HP

    def draw(self, screen: pygame.surface.Surface) -> None:

        # Draw health bar
        hb_len = 250
        hb_height = 10
        green = (0, 255, 0)
        red = (255, 0, 0)

        pygame.draw.rect(screen, red, (5, 5, hb_len, hb_height))

        p_hp = self.hp // self.max_hp

        pygame.draw.rect(screen, green, (5, 5, hb_len * p_hp, hb_height))

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

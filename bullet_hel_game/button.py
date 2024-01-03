from entity import Entity
import pygame


class Button(Entity):
    def __init__(self, x: int, y: int, msg: str, p_type: int) -> None:
        super().__init__(x, y)

        self.color = (168, 227, 197)  # light green
        self.msg = msg
        self.p_type = p_type

        # Visual things
        self.image = pygame.Surface((200, 200))  # TODO update to image
        self.image.fill(color=self.color)

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.surface.Surface) -> None:
        self.image.fill(color=self.color)
        screen.blit(self.image, (self.posX, self.posY))

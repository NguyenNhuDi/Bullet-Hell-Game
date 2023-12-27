from entity import Entity


class Enemy(Entity):
    def __init__(self, x: int, y: int, s_width: int = 800, s_height: int = 600):
        super().__init__(x, y, s_width, s_height)

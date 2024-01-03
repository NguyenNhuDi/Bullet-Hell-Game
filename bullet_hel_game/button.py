from entity import Entity


class Button(Entity):
    def __init__(self, x: int, y: int, msg: str) -> None:
        super().__init__(x, y)

        self.color = ()

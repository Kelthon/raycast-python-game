from pygame import Vector2

class Spacing():
    def __init__(self, topleft: Vector2(0, 0), bottomright: Vector2(0, 0)) -> None:
        self.top = topleft.x
        self.left = topleft.y
        self.bottom = bottomright.x
        self.right = bottomright.y
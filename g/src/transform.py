from pygame import Vector2

class Transform():
    def __init__(self, position: Vector2 = Vector2(0, 0), rotate: Vector2 = Vector2(0, 0), scale: Vector2 = Vector2(1, 1)) -> None:
        self.scale = scale
        self.rotate = rotate
        self.position = position
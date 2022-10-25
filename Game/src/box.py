from pygame import Vector2
from game.src.spacing import Spacing

class Box():
    def __init__(self, position: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(0, 0),
            padding: Vector2 = Vector2(0, 0), margin: Vector2 = Vector2(0, 0)) -> None:
        
        self.position = position
        self.width = size.x
        self.height = size.y
        self.margin = Spacing(margin, margin)
        self.padding = Spacing(padding, padding)

    def get_position(self) -> Vector2:
        return self.position

    def update_size(self, size: Vector2):
        self.width = size.x
        self.height = size.y
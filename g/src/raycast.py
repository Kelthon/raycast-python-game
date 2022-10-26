from pygame import Vector2, Color, draw
from game.src.constants import global_window

class Raycast():
    def __init__(self, origin: Vector2, direction: Vector2, color:Color=Color(0, 0, 0)) -> None:
        self.origin = origin
        self.direction = direction
        self.color = color
        self.shape = draw.aaline(global_window.surface, self.color, self.origin, self.raycast())

    def raycast(self):
        # Calc raycast line
        ray = Vector2(0, 0)
        line_slope = 0

        # Case line slope is zero
        if self.direction.x == self.origin.x:
            ray.x = self.direction.x
            if self.direction.y > self.origin.y:
                ray.y = global_window.height
            else:
                ray.y = 0
        elif self.direction.y == self.origin.y:
            ray.y = self.direction.y
            if self.direction.x > self.origin.x:
                ray.x = global_window.width
            else:
                ray.x = 0
        # Case line slope is no-zero
        else:
            if self.direction.y < self.origin.y:

                ray.y = 0
                line_slope = (self.origin.y - self.direction.y) / (self.direction.x - self.origin.x)
                ray.x = self.direction.x + ((self.direction.y - ray.y) / line_slope)

            else:
                ray.y = global_window.height
                line_slope = (self.direction.y - self.origin.y) / (self.direction.x - self.origin.x)
                ray.x = self.direction.x + ((ray.y - self.direction.y) / line_slope)
        return ray
from pygame import Vector2, Color, draw
from game.src.constants import global_window

class Raycast():
    def __init__(self, origin: Vector2, direction: Vector2, color:Color=Color(0, 0, 0)) -> None:
        self.origin = origin
        self.direction = direction
        self.color = color
        self.shape = draw.aaline(global_window.surface, self.color, self.origin, self.raycast())

    def line_slope(self) -> float:
        slope = 0

        if self.direction.x != self.origin.x and self.direction.y != self.origin.y:
            slope_direction = self.origin.y - self.direction.y if self.direction.y < self.origin.y else self.direction.y - self.origin.y
            slope = slope_direction / (self.direction.x - self.origin.x)

        return slope

    def raycast(self, max_length: Vector2 = Vector2(global_window.width, global_window.height)):
        # Calc raycast line
        ray = Vector2(0, 0)
        line_slope = self.line_slope()

        # Case line slope is zero and raycast is a horizontal line
        if self.direction.x == self.origin.x:
            ray.x = self.direction.x
            ray.y = max_length.y if self.direction.y > self.origin.y else 0
        
        # Case line slope is zero and raycast is a vertical line
        elif self.direction.y == self.origin.y:
            ray.y = self.direction.y
            ray.x = max_length.x if self.direction.x > self.origin.x else 0
        
        # Case line slope is no-zero and raycast is a sloped line
        else:
            ray.y = 0 if self.direction.y < self.origin.y else max_length.y
            slope_direction = (self.direction.y - ray.y) if self.direction.y < self.origin.y else (ray.y - self.direction.y)
            ray.x = self.direction.x + (slope_direction / line_slope)

        return ray

    
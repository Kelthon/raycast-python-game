from typing import List, Tuple
from pygame import Vector2, Color, Rect, draw
from game.src.constants import global_window

class Raycast():
    def __init__(self, origin: Vector2, direction: Vector2, color:Color=Color(0, 0, 0), max_length = Vector2(global_window.width, global_window.height), collision_list: List[Rect] | None = None) -> None:
        self.__color = color
        self.__origin = origin
        self.__direction = direction
        self.__max_length = max_length
        self.__collision_list: List[Rect] = collision_list
        self.update()

    def set_color(self, color: Vector2) -> None:
        self.__color = color
        self.update()

    def set_origin(self, origin: Vector2) -> None:
        self.__origin = origin
        self.update()

    def set_direction(self, direction: Vector2) -> None:
        self.__direction = direction
        self.update()

    def set_max_length(self, max_length: Vector2) -> None:
        self.__max_length = max_length
        self.update()

    def set_collision_list(self, obj_list: List[Rect] | None):
        self.__collision_list = obj_list
        self.update()

    def update(self):
        ray = self.raycast()

        if self.__collision_list is not None:
            for i in self.__collision_list:
                try:
                    limit_start, limit_end = i.clipline(self.__origin, ray)
                    if self.__origin.distance_squared_to(Vector2(limit_start)) < self.__origin.distance_squared_to(ray):
                        ray = Vector2(limit_start)
                except:
                    continue

        self.shape = draw.aaline(global_window.surface, self.__color, self.__origin, ray)

    def line_slope(self) -> float:
        slope = 0

        if self.__direction.x != self.__origin.x and self.__direction.y != self.__origin.y:
            slope_direction = self.__origin.y - self.__direction.y if self.__direction.y < self.__origin.y else self.__direction.y - self.__origin.y
            slope = slope_direction / (self.__direction.x - self.__origin.x)

        return slope

    def raycast(self):
        # Calc raycast line
        ray = Vector2(0, 0)
        line_slope = self.line_slope()

        # Case line slope is zero and raycast is a horizontal line
        if self.__direction.x == self.__origin.x:
            ray.x = self.__direction.x
            ray.y = self.__max_length.y if self.__direction.y > self.__origin.y else 0
        
        # Case line slope is zero and raycast is a vertical line
        elif self.__direction.y == self.__origin.y:
            ray.y = self.__direction.y
            ray.x = self.__max_length.x if self.__direction.x > self.__origin.x else 0
        
        # Case line slope is no-zero and raycast is a sloped line
        else:
            ray.y = 0 if self.__direction.y < self.__origin.y else self.__max_length.y
            slope_direction = (self.__direction.y - ray.y) if self.__direction.y < self.__origin.y else (ray.y - self.__direction.y)
            ray.x = self.__direction.x + (slope_direction / line_slope)

        return ray
        
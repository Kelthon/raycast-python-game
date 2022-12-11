from game.src.facade import *
from typing import List

def get_line_slope(origin: Vector2, direction: Vector2) -> float:
    """Calculates the line slope of a line into two vectors
    
    :param origin: points that represents the origin line
    :type origin: pygame.math.Vector2
    :param direction: points that represents the end line
    :type direction: pygame.math.Vector2

    :returns: returns a number that represents line slope
    :rtype: float
    """
    
    slope = -100

    if direction.x != origin.x and direction.y != origin.y:
        slope_direction = origin.y - direction.y if direction.y < origin.y else direction.y - origin.y
        slope = slope_direction / (direction.x - origin.x)

    return slope

class Raycaster:
    def __init__(self, origin: Vector2, direction: Vector2, max_length:Vector2) -> None:
        self.origin = origin
        self.direction = direction
        self.max_length = max_length


    def raycast(self) -> Vector2:
        """Calculates a vector called raycast, from the a origin into a direction

        :param origin: points that represents the origin line
        :type origin: pygame.math.Vector2
        :param direction: points that represents the end line
        :type direction: pygame.math.Vector2
        :param max_length:  points that represents the max length line
        :type max_length: pygame.math.Vector2

        :returns: a vector that represents a raycast projection
        :rtype: pygame.math.Vector2
        """

        # Calc raycast line
        ray = Vector2(0, 0)
        ray_line_slope = get_line_slope(self.origin, self.direction)

        # Case line slope is zero and raycast is a horizontal line
        if self.direction.x == self.origin.x:
            ray.x = self.direction.x
            ray.y = self.max_length.y if self.direction.y > self.origin.y else 0
        
        # Case line slope is zero and raycast is a vertical line
        elif self.direction.y == self.origin.y:
            ray.y = self.direction.y
            ray.x = self.max_length.x if self.direction.x > self.origin.x else 0
        
        # Case line slope is no-zero and raycast is a sloped line
        else:
            ray.y = 0 if self.direction.y < self.origin.y else self.max_length.y
            slope_direction = (self.direction.y - ray.y) if self.direction.y < self.origin.y else (ray.y - self.direction.y)
            ray.x = self.direction.x + (slope_direction / ray_line_slope)

        return ray

    def raycast_with_collision(self, collision_list: List[Rect]) -> Vector2:
        """Simulates a collision in raycast vector
        
        :param origin: points that represents the origin line
        :type origin: pygame.math.Vector2
        :param direction: points that represents the end line
        :type direction: pygame.math.Vector2
        :param max_length:  points that represents the max length line
        :type max_length: pygame.math.Vector2
        :param collision_list: represents the obtacles list
        :type collision_list: List[pygame.Rect]

        :returns: a vector that represents the collision point
        :rtype: pygame.math.Vector2
        """

        ray = self.raycast()

        if collision_list is not None:
            for i in collision_list:
                try:
                    limit_start, limit_end = i.clipline(self.origin, ray)
                    if self.origin.distance_squared_to(Vector2(limit_start)) < self.origin.distance_squared_to(ray):
                        ray = Vector2(limit_start)
                except:
                    continue

        return ray
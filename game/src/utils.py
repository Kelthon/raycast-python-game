from random import randint
from typing import List, Tuple
from game.src.facade import *


def mouse_position() -> Vector2:
    """Gets de mouse position as a pygame.math.Vector2
    
    :returns: a vector tha represents the mouse position
    :rtype: pygame.math.Vector2
    """

    return Vector2(pygame.mouse.get_pos())

def center(vector: Vector2) -> Vector2:
    """Gets a Vector2 centered at other Vector2
    
    :param vector: vector to calculates center
    :type vector: pygame.math.Vector2

    :returns: Vector2 thats represent a center
    :rtype vector: pygame.math.Vector2
    """
    return Vector2(vector.x / 2, vector.y / 2)


def get_random_items(items) -> List[Tuple[Surface, int]]:
    rand = []

    for i in range(0, 4):
        rand.append((items[randint(0, len(items) - 1)], i))

    return rand
    

def suffle_items(items) -> List[Tuple[Surface, int]]:
    suffle = []

    for i in range(0, 4):
        suffle.append((items[randint(0, len(items) - 1)], i))
    
    return suffle


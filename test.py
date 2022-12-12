import pytest
from game.src.facade import Vector2
from game.src.raycast import get_line_slope

def get_line_slope(origin: Vector2, direction: Vector2) -> float:
    
    slope = -100

    if direction.x != origin.x and direction.y != origin.y:
        slope_direction = origin.y - direction.y if direction.y < origin.y else direction.y - origin.y
        slope = slope_direction / (direction.x - origin.x)

    return slope


# black_box test
def black_box_test_line_slope():
    assert get_line_slope(Vector2(0, 0), Vector2(0, 0)) == -100
    assert get_line_slope(Vector2(0, 0), Vector2(-50, -50)) == 1.0
    assert get_line_slope(Vector2(0, 0), Vector2(100, -50)) == 0.5
    assert get_line_slope(Vector2(0, 0), Vector2(-100, 50)) == -0.5
    assert get_line_slope(Vector2(0, 0), Vector2(50, 50)) == 1.05

# white_box test

def white_box_test_line_slope():
    assert get_line_slope(Vector2(0, 0), Vector2(0, 50))
    assert get_line_slope(Vector2(20, 0), Vector2(10, 10))
    assert get_line_slope(Vector2(20, 10), Vector2(0, 10))
    assert get_line_slope(Vector2(20, 10), Vector2(20, 10))
    assert get_line_slope(Vector2(20, 10), Vector2(-20, 10.5))

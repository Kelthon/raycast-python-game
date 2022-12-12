import pytest
from game.src.facade import Vector2, Rect
from game.src.raycast import get_line_slope
from game.src.config import tela
from game.app import projectile_collided

# black_box test
def black_box_test_line_slope():
    assert get_line_slope(Vector2(0, 0), Vector2(0, 0)) == 0
    assert get_line_slope(Vector2(0, 0), Vector2(0, 50)) == 0
    assert get_line_slope(Vector2(0, 0), Vector2(100, 0)) == 0
    assert get_line_slope(Vector2(10, 50), Vector2(30, 0)) == 2.5
    assert get_line_slope(Vector2(10, 40), Vector2(40, 45)) == 0.16666666666666666

# white_box test

def white_box_test_projectile_collided():
    rects_1 = []
    rects_2 = [Rect(0, 0, 10, 10)]
    size = Vector2(10, 10)
    assert projectile_collided(Vector2(0, 0), size, rects_1)
    assert projectile_collided(Vector2(tela.size.x + 1, tela.size.y + 1), Vector2(0, 0), rects_2)
    assert projectile_collided(Vector2(tela.size.x, tela.size.y), size, rects_2)
    assert projectile_collided(Vector2(0, 0), size, rects_2)
    assert projectile_collided(Vector2(50, 50), size, rects_2)
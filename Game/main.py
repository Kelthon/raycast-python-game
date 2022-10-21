import pygame
from sys import exit
from typing import Tuple
from pygame import Vector2, Color
from pygame.locals import *

posx = 200
posy = 200
main_window_width = 640
main_window_height = 640

pygame.init()
window = pygame.display.set_mode((main_window_width, main_window_height), RESIZABLE)

def raycast(origin: Vector2, direction: Vector2, color:Color=Color(0, 0, 0)) -> Rect:
    # Calc raycast line
    ray = Vector2(0, 0)
    line_slope = 0

    # Case line slope is zero
    if direction.x == origin.x:
        ray.x = direction.x
        if direction.y > origin.y:
            ray.y = main_window_height
        else:
            ray.y = 0
    elif direction.y == origin.y:
        ray.y = direction.y
        if direction.x > origin.x:
            ray.x = main_window_width
        else:
            ray.x = 0
    # Case line slope is no-zero
    else:
        if direction.y < origin.y:

            ray.y = 0
            line_slope = (origin.y - direction.y) / (direction.x - origin.x)
            ray.x = direction.x + ((direction.y - ray.y) / line_slope)

        else:
            ray.y = main_window_height
            line_slope = (direction.y - origin.y) / (direction.x - origin.x)
            ray.x = direction.x + ((ray.y - direction.y) / line_slope) 

    return pygame.draw.aaline(window, color, origin, ray)


def grid(base_color: Color = Color(0, 0, 0), axis_x_color: Color = Color(255, 0, 0), axis_y_color: Color = Color(0, 255, 127)) -> Tuple[Rect]:

    for i in range(0, main_window_width + 1, 64):
        if main_window_width / 2  == i:
            axis_x = i
        else:
            pygame.draw.line(window, base_color, (i, 0), (i, main_window_height))

    for i in range(0, main_window_height + 1, 64):
        if main_window_width / 2  == i:
            pygame.draw.line(window, axis_y_color, (0, i), (main_window_width, i))
        else:
            pygame.draw.line(window, base_color, (0, i), (main_window_width, i))

    pygame.draw.line(window, axis_x_color, (axis_x, 0), (axis_x, main_window_height))
 

player_north = pygame.draw.line(window, [0, 0, 255], ((main_window_width / 2) -1, 0), ((main_window_width / 2) -1, main_window_height))
player_left = pygame.draw.line(window, [255, 0, 0], (0, (main_window_height / 2) -1), (main_window_width, (main_window_height / 2) -1))

while True:
    for event in pygame.event.get():
        if event.type == WINDOWCLOSE:
            pygame.quit()
            exit()
    
    window.fill([0]*3)
    mousex, mousey = pygame.mouse.get_pos()
    keys_pressed = pygame.key.get_pressed()

    # draw player and raycast
    grid(Color(80, 80, 80), Color(160, 160, 160), Color(160, 160, 160))
    player = pygame.draw.circle(window, [255]*3, (posx, posy), 10)
    raycast(Vector2(posx, posy), Vector2(mousex, mousey), Color(0, 255, 0))

    # player movement
    if keys_pressed[K_a] or keys_pressed[K_LEFT]:
        posx -= 0.1
    elif keys_pressed[K_d] or keys_pressed[K_RIGHT]:
        posx += 0.1
    if keys_pressed[K_w] or keys_pressed[K_UP]:
        posy -= 0.1
    elif keys_pressed[K_s] or keys_pressed[K_DOWN]:
        posy += 0.1

    pygame.display.flip()

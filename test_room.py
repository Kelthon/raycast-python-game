import sys
import pygame
from pygame.locals import *
from typing import Sequence, List, Tuple
from pygame import Vector2, Rect
import math

'''
    Exit the game
'''
def exit() -> None:
    pygame.quit()
    sys.exit()

'''
    Update screen surface
'''
def update_screen() -> None:
    pygame.display.flip()
    tela.fill([0]*3)

'''
    Calc the line slope of a line
'''
def line_slope(origin: Vector2, direction: Vector2) -> float:
        slope = -100

        if direction.x != origin.x and direction.y != origin.y:
            slope_direction = origin.y - direction.y if direction.y < origin.y else direction.y - origin.y
            slope = slope_direction / (direction.x - origin.x)

        return slope

'''
    Calculates a raycast from the a origin into a direction
'''
def raycast(origin: Vector2, direction: Vector2, max_length: Vector2) -> Vector2:
     # Calc raycast line
        ray = Vector2(0, 0)
        ray_line_slope = line_slope(origin, direction)

        # Case line slope is zero and raycast is a horizontal line
        if direction.x == origin.x:
            ray.x = direction.x
            ray.y = max_length.y if direction.y > origin.y else 0
        
        # Case line slope is zero and raycast is a vertical line
        elif direction.y == origin.y:
            ray.y = direction.y
            ray.x = max_length.x if direction.x > origin.x else 0
        
        # Case line slope is no-zero and raycast is a sloped line
        else:
            ray.y = 0 if direction.y < origin.y else max_length.y
            slope_direction = (direction.y - ray.y) if direction.y < origin.y else (ray.y - direction.y)
            ray.x = direction.x + (slope_direction / ray_line_slope)

        return ray

# raycast enemy
def straight_raycast() -> Vector2:
    return (enemy_position.x,enemy_position.y+200);


def raycast_with_collision(origin: Vector2, direction: Vector2, max_length: Vector2, collision_list) -> Vector2:
    ray = raycast(origin, direction, max_length)

    if collision_list is not None:
            for i in collision_list:
                try:
                    limit_start, limit_end = i.clipline(origin, ray)
                    if origin.distance_squared_to(Vector2(limit_start)) < origin.distance_squared_to(ray):
                        ray = Vector2(limit_start)
                except:
                    continue

    return ray
    

'''
    Gets de mouse position as a pygame.math.Vector2
'''
def mouse_position() -> Vector2:
    return Vector2(pygame.mouse.get_pos())

'''
    Returns a string where has the collision with player
'''
def get_collision_direction(rects: List[Rect]):
    collide_list = []
    
    for rect in rects:
        if player.colliderect(rect):
            if player.top <= rect.bottom and player.bottom > rect.bottom:
                collide_list.append("top")

            if player.bottom >= rect.top and player.top < rect.top:
                collide_list.append("bottom")
            
            if player.right >= rect.left and player.left < rect.left:
                collide_list.append("right")
            
            if player.left <= rect.right and player.right > rect.right:
                collide_list.append("left")

    return collide_list

'''
    Updates the variable player_position
'''
def player_move() -> None:
    key = pygame.key.get_pressed()
    collision = get_collision_direction(walls)

    if not "top" in collision:
        if key[K_w]:
            player_position.y -= 0.2
    
    if not "bottom" in collision:
        if key[K_s]:
            player_position.y += 0.2

    if not "left" in collision:
        if key[K_a]:
            player_position.x -= 0.2
    
    if not "right" in collision:
        if key[K_d]:
            player_position.x += 0.2

'''
    Call functions to update the game loop
'''

# movement of enemy horizontally
direction_move = 1;
def enemy_move() -> None:

    global direction_move;

    if (math.floor(enemy_position.x) == 120):

        direction_move = 1;

    elif (math.floor(enemy_position.x) == 660):

        direction_move = -1;

    enemy_position.x+=0.2*direction_move;

def update() -> None:
    
    update_screen()
    player_move()
    enemy_move();

    for event in pygame.event.get():
        if event.type == WINDOWCLOSE:
            exit()
            return False
    
    return True

'''
    Constants and variables for the game to works
'''
inGame = True
walls: List[Rect] = []
tela_size = Vector2((800, 600))
tela_center = Vector2(tela_size.x / 2, tela_size.y / 2)
tela = pygame.display.set_mode(tela_size)
player_position = Vector2(tela_center)
enemy_position = Vector2(120,0)

'''
    main loop responsible for drawing things on the screen
'''
while inGame:
    inGame = update()
    
    walls = [
        pygame.draw.rect(tela, [160]*3, (0, 0, 40, 120)),
        pygame.draw.rect(tela, [150]*3, (40, 0, 80, 40)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 40, 0, 40, 120)),
        pygame.draw.rect(tela, [150]*3, (tela_size.x - 120, 0, 80, 40)),
        pygame.draw.rect(tela, [160]*3, (0, tela_size.y - 120, 40, 120)),
        pygame.draw.rect(tela, [150]*3, (40, tela_size.y - 40, 80, 40)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 40, tela_size.y - 120, 40, 120)),
        pygame.draw.rect(tela, [150]*3, (tela_size.x - 120, tela_size.y - 40, 80, 40)),

        pygame.draw.rect(tela, [150]*3, (tela_center.x - 150, tela_center.y - 100, 300, 5)),
        pygame.draw.rect(tela, [140]*3, (tela_center.x - 155, tela_center.y - 100, 5, 200)),
        pygame.draw.rect(tela, [130]*3, (tela_center.x + 150, tela_center.y - 100, 5, 200)),
    ]

    enemy = pygame.draw.rect(tela, (240,42,42), Rect(enemy_position.x, enemy_position.y, 20, 20),2);

    player = pygame.draw.circle(tela, [255]*3, player_position, 20);
    raycast_line = pygame.draw.aaline(tela, [0, 255, 0], player_position, raycast_with_collision(player_position, mouse_position(), tela_size, walls))
    raycast_line_e = pygame.draw.aaline(tela, [0, 255, 0], (enemy_position.x+10,enemy_position.y+10), straight_raycast())
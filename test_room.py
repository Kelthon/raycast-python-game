import sys
import pygame
from pygame.locals import *
from typing import Sequence, List, Tuple
from pygame import Vector2, Rect

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
        slope = 0

        if direction.x != origin.x and direction.y != origin.y:
            slope_direction = origin.y - direction.y if direction.y < origin.y else direction.y - origin.y
            slope = slope_direction / (direction.x - origin.x)

        return slope

'''
    Calculates a vector from the a origin into a direction
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

'''
    Simulates a collision in raycast
'''
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
def get_collision_direction(rects: List[Rect]) -> List[str]:
    collide_list: List[str] = []
    
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
    Returns a Vector2 with a montion sense: 1 for fowards or -1 for backwards 
'''
def get_motion_sense(origin: Vector2, direction: Vector2) -> Vector2:
    sense = Vector2(1, 1)

    if origin.x > direction.x:
        sense.x = -1
    
    if origin.y > direction.y:
        sense.y = -1

    return sense

'''
    Returns boolean that represents if bulltes to collide
'''
def projectile_collided(projectile_origin: Vector2, projectile_direction: Vector2, rects: List[Rect]) -> bool:
    collision = False

    if projectile_origin.x > projectile_direction.x and projectile_origin.y > projectile_direction.y:
        if projectile_origin.x <= projectile_direction.x and projectile_origin.y <= projectile_direction.y:
            collision = True
    elif projectile_origin.x > projectile_direction.x and projectile_origin.y < projectile_direction.y:
        if projectile_origin.x <= projectile_direction.x and projectile_origin.y >= projectile_direction.y:
            collision = True
    elif projectile_origin.x < projectile_direction.x and projectile_origin.y < projectile_direction.y:
        if projectile_origin.x >= projectile_direction.x and projectile_origin.y >= projectile_direction.y:
            collision = True
    elif projectile_origin.x < projectile_direction.x and projectile_origin.y < projectile_direction.y:
         if projectile_origin.x >= projectile_direction.x and projectile_origin.y <= projectile_direction.y:
            collision = True

    return collision
'''
    Updates the variable player_position
'''
def player_move() -> None:
    key = pygame.key.get_pressed()
    collision = get_collision_direction(walls)

    if not "top" in collision:
        if key[K_w]:
            player_position.y -= 0.1
    
    if not "bottom" in collision:
        if key[K_s]:
            player_position.y += 0.1

    if not "left" in collision:
        if key[K_a]:
            player_position.x -= 0.1
    
    if not "right" in collision:
        if key[K_d]:
            player_position.x += 0.1

'''
    Call functions to update the game loop
'''
def update() -> None:
    
    update_screen()
    player_move()

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
player_size = 10
bullets: List[Tuple[bool, Vector2, Vector2, Vector2, Vector2]] = []
clock = pygame.time.Clock()
fire_rate = 10
waiting_time = fire_rate
bullet_speed = 1

'''
    main loop responsible for drawing things on the screen
'''
while inGame:
    inGame = update()
    delta_time = pygame.time.get_ticks()

    walls = [
        pygame.draw.rect(tela, [160]*3, (0, 0, 5, 120)),
        pygame.draw.rect(tela, [160]*3, (5, 0, 115, 5)),
        pygame.draw.rect(tela, [160]*3, (0, 120, 70, 5)),
        pygame.draw.rect(tela, [160]*3, (120, 0, 5, 70)),
        pygame.draw.rect(tela, [160]*3, (120, 0, 5, 70)),
        pygame.draw.rect(tela, [160]*3, (120, 0, 5, 70)),

        pygame.draw.rect(tela, [160]*3, (tela_size.x - 5, 0, 5, 120)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 120, 0, 115, 5)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 125, 0, 5, 70)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 70, 120, 70, 5)),

        pygame.draw.rect(tela, [160]*3, (0, tela_size.y - 120, 5, 120)),
        pygame.draw.rect(tela, [160]*3, (5, tela_size.y - 5, 115, 5)),
        pygame.draw.rect(tela, [160]*3, (120, tela_size.y - 70, 5, 70)),
        pygame.draw.rect(tela, [160]*3, (5, tela_size.y - 120, 70, 5)),

        pygame.draw.rect(tela, [160]*3, (tela_size.x - 5, tela_size.y - 120, 5, 120)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 120, tela_size.y - 5, 115, 5)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 120, tela_size.y - 70, 5, 70)),
        pygame.draw.rect(tela, [160]*3, (tela_size.x - 70, tela_size.y - 120, 70, 5)),

        pygame.draw.rect(tela, [160]*3, (tela_center.x - 150, tela_center.y - 100, 70, 5)),
        pygame.draw.rect(tela, [160]*3, (tela_center.x - 35, tela_center.y - 100, 70, 5)),
        pygame.draw.rect(tela, [160]*3, (tela_center.x + 80, tela_center.y - 100, 70, 5)),

        pygame.draw.rect(tela, [160]*3, (tela_center.x - 155, tela_center.y - 100, 5, 200)),
        pygame.draw.rect(tela, [160]*3, (tela_center.x + 150, tela_center.y - 100, 5, 200)),
        pygame.draw.rect(tela, [160]*3, (tela_center.x - 155, tela_center.y + 100, 100, 5)),
        pygame.draw.rect(tela, [160]*3, (tela_center.x + 55, tela_center.y + 100, 100, 5)),
    ]

    ray = raycast_with_collision(player_position, mouse_position(), tela_size, walls)
    player = pygame.draw.circle(tela, [255]*3, player_position, player_size)
    raycast_line = pygame.draw.aaline(tela, [0, 255, 0], player_position, ray)

    left_click, scroll_click, right_click = pygame.mouse.get_pressed()
    
    if left_click:
        if waiting_time == fire_rate:
            start_position = Vector2(player_position.x - 2.5, player_position.y - 2.5)
            sense = get_motion_sense(start_position, ray)
            bullets.append((False, sense, start_position, ray, Vector2(5, 5)))
            waiting_time = 0
        else:
            waiting_time += abs(pygame.time.get_ticks() - delta_time)

    for bullet in bullets:
        bullet_collide, bullet_sense, bullet_origin, bullet_direction, bullet_size = bullet
        
        if bullet_collide:
            bullets.remove(bullet)
        else:
            collide_x = False
            collide_y = False
            delta = Vector2(abs(bullet_origin.x - bullet_direction.x), abs(bullet_origin.y - bullet_direction.y))
            position = Vector2(bullet_origin.x, bullet_origin.y)
            
            if bullet_direction.y < bullet_origin.y:
                if bullet_sense.y < 0:
                    position.y = bullet_origin.y - bullet_speed
                else:
                    collide_y = True
            else:
                if bullet_sense.y > 0:
                    position.y = bullet_origin.y + bullet_speed
                else:
                    collide_y = True

            if bullet_direction.x < bullet_origin.x:
                if bullet_sense.x < 0:
                    position.x = bullet_origin.x - bullet_speed
                else:
                    collide_x = True

            else:
                if bullet_sense.x > 0:
                    position.x = bullet_origin.x +bullet_speed
                else:
                    collide_x = True

            if collide_x and collide_y:
                bullet_collide = True
            
            bullet_origin = position
            bullet_collide = projectile_collided(bullet_origin, bullet_direction, walls) | bullet_collide
            bullets[bullets.index(bullet)] = (bullet_collide, bullet_sense, bullet_origin, bullet_direction, bullet_size)

            pygame.draw.rect(tela, [255, 127, 0], (bullet_origin, bullet_size))
        
import sys
import math
import numpy
import pygame
from pygame.locals import *
from pygame.font import Font
from typing import Sequence, List, Tuple, Callable
from pygame import Vector2, Rect, Color, mixer

pygame.init()
mixer.init()
pygame.font.init()

def exit() -> None:
    """Exit the game"""

    pygame.quit()
    sys.exit()

def update_tela() -> None:
    """Update tela surface"""
    
    pygame.display.flip()
    tela.fill([0]*3)

def line_slope(origin: Vector2, direction: Vector2) -> float:
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

def raycast(origin: Vector2, direction: Vector2, max_length: Vector2) -> Vector2:
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

def straight_raycast() -> Vector2:
    """raycast enemy"""
    return (enemy_position.x,enemy_position.y+200);

def raycast_with_collision(origin: Vector2, direction: Vector2, max_length: Vector2, collision_list: List[Rect]) -> Vector2:
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
    
def mouse_position() -> Vector2:
    """Gets de mouse position as a pygame.math.Vector2
    
    :returns: a vector tha represents the mouse position
    :rtype: pygame.math.Vector2
    """

    return Vector2(pygame.mouse.get_pos())

def get_collision_direction(rects: List[Rect]) -> List[str]:
    """Returns a string where has the collision with player

    :params rects: represents a obstacles list
    :type rects: List[Rect]

    :returns: a list with all collisions in str format: "top", "down", "left" and/or "right"
    :rtype: List[str]
    """
    
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

def get_motion_sense(origin: Vector2, direction: Vector2) -> Vector2:
    """Returns a Vector2 with a montion sense
    
    :param origin: points that represents the origin motion
    :type origin: pygame.math.Vector2
    :param direction: points that represents the end motion
    :type direction: pygame.math.Vector2

    :returns: returns a Vector2 with a montion sense
    :rtype: pygame.math.Vector2
    """
    
    sense = Vector2(1, 1)

    if origin.x > direction.x:
        sense.x = -1
    
    if origin.y > direction.y:
        sense.y = -1

    return sense

def projectile_collided(projectile_origin: Vector2, projectile_direction: Vector2, rects: List[Rect]) -> bool:
    """Returns boolean that represents if bulltes to collide
    
    :param projectile_origin: 
    :type projectile_origin: Vector2
    :param projectile_direction: 
    :type projectile_direction: Vector2
    :param rects:
    :type rects: List[Rect]

    :returns: a boolean representing whether it was a collision
    :rtype: boolean
    """
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

def player_move() -> None:
    """Updates the variable player_position"""

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

direction_move = 1;
def enemy_move() -> None:
    """movement of enemy horizontally"""
    height = 0;
    width = 0;
    tan = 0;
    res = 0
    state = 1;
    
    if player_position.x >= enemy_position.x+10-radius:
        if player_position.x <= enemy_position.x+10+radius:
            if player_position.y >= enemy_position.y+10-radius:
                if player_position.y <= enemy_position.y+10+radius:
                    width = player_position.x - enemy_position.x-10
                    height = player_position.y - enemy_position.y-10
                    tan = height/0.001 if width == 0 else height/width
                    
                    res = 1
                    sen = (numpy.sin(numpy.arctan(tan))*res)
                    cos = (numpy.cos(numpy.arctan(tan))*res)
                    if (width < 0):
                        sen = -sen;
                        cos = -cos

                    enemy_position.y += sen*0.1;
                    enemy_position.x += cos*0.1;
                    state = 0
                    
    global direction_move;

    if (math.floor(enemy_position.x) == 120):

        direction_move = 1;

    elif (math.floor(enemy_position.x) == 660):

        direction_move = -1; 

    enemy_position.x+=0.1*direction_move*state;

def close_tela() -> bool:
    for event in pygame.event.get():
        if event.type == WINDOWCLOSE:
            exit()
            return False
    return True

def center(vector: Vector2):
    """Gets a Vector2 centered at other Vector2
    
    :param vector: vector to calculates center
    :type vector: pygame.math.Vector2

    :returns: Vector2 thats represent a center
    :rtype vector: pygame.math.Vector2
    """
    return Vector2(vector.x / 2, vector.y / 2)

def get_font(font_name: str = pygame.font.get_default_font(), size: float = 25, bold: bool = False, italic: bool = False) -> Font:
    """Returns a system font"""
    font  = pygame.font.SysFont(font_name, size, bold, italic)
    return font

def write(text: str, color: Color = Color(255, 255, 255), position: Vector2 = Vector2(0, 0), bg_color = None, font: Font = get_font()) -> Rect:
    """blit a text in screen"""
    render = font.render(text, True, color, bg_color)
    return pygame.display.get_surface().blit(render, position)

def update() -> None:
    """Call functions to update the game loop"""

    update_tela()
    player_move()
    enemy_move();

def update_menu(play_enable: bool) -> bool:
    close_tela()
   
    menu = True
    if play_enable:
        menu = False
    
    return menu

def update() -> None:
    """Call functions to update the game loop"""

    update_tela()
    player_move()
    enemy_move();
    
    return close_tela()

def creat_button(text: str, size: Vector2, position: Vector2, function: Callable):
    button: List[Vector2, Vector2]
    if button_jogar_position.x <= mouse_pos.x <= button_jogar_position.x + button_size.x and button_jogar_position.y <= mouse_pos.y <= button_jogar_position.y + button_size.y:
        #Aqui será o botão cinza
        button = pygame.draw.rect(tela,color_light,(button_jogar_position, button_size))  
          
    else: 
        #Aqui será o botão preto
        button = pygame.draw.rect(tela,color_dark,(button_jogar_position, button_size))    
    return button

"""Declaration constants and variables for the game to works"""
inMenu = True
inGame = False
walls: List[Rect] = []
tela_size = Vector2((800, 600))
tela_center = center(tela_size)
tela = pygame.display.set_mode(tela_size)
player_position = Vector2(tela_center)
player_size = 10
bullets: List[Tuple[bool, Vector2, Vector2, Vector2, Vector2]] = []
clock = pygame.time.Clock()
fire_rate = 100
waiting_time = fire_rate
bullet_speed = 1
enemy_position = Vector2(200,80)
radius = 100


'''*** Informações para inserir no meu incial do programa ***'''
color_white = (255, 255, 255)
color_light = (128, 128, 128) #Cor do botão mudará para cinza quando passar o mouse por cima
color_dark = (0, 0, 0) #Cor do butão antes de clicar
impact_font = pygame.font.SysFont('Impact', 30) #Fonte que sserá usado para o butão
text_1 = impact_font.render('JOGAR', True, color_white)
text_2 = impact_font.render('QUIT', True, color_white)
text_3 = impact_font.render('HELP',True, color_white)
button_size = Vector2(140, 40)
button_jogar_position = Vector2(tela_size.x/2 - button_size.x/2, tela_size.y/2 + 150)
button_quit_position = Vector2(tela_size.x/2 - button_size.x/2, tela_size.y/2 + 150)
button_help_position = Vector2(tela_size.x/2 - button_size.x/2, tela_size.y/2 + 150 + button_size.y + button_size.y/2)
'''Aqui é a tela de fundo'''


tela_background_image = pygame.image.load("game/public/textures/background.jpg") #olhar o caminho disso aqui
#Colocando som
mixer.music.load("game/public/sound effects/ShotGun-Cocking_background.wav")#Olhar o caminho disso aqui
mixer.music.set_volume(0.7)

while inMenu:
    inMenu = update_menu(inGame)
    
    left_click, scroll_click, right_click = pygame.mouse.get_pressed()
    mouse_pos = mouse_position()

    if left_click:
        #Criando cada um dos botões...
        if button_jogar_position.x <= mouse_pos.x and mouse_pos.x <= button_jogar_position.x + button_size.x and button_jogar_position.y <= mouse_pos.y and mouse_pos.y <= button_jogar_position.y + button_size.y:
            mixer.music.play()
            inGame = True 
        
        if button_quit_position.x <= mouse_pos.x <= button_quit_position.x + button_size.x and button_quit_position.y + 2 * tela_size.y <= mouse_pos.y <= button_quit_position.y + 2 * tela_size.y:
            mixer.music.play()
            pygame.quit() 
        
        if button_help_position.x <= mouse_pos.x <= button_help_position.x + button_size.x and button_help_position.y + 2 * tela_size.y <= mouse_pos.y <= button_help_position.y + 2 * tela_size.y:
            print('aqui vai as intruções')        
    
    
    tela.blit(tela_background_image, (0, 0))
    #pegando a posição do mouse
    # creat_button("Jogar", button_size, button_jogar_position)
    # #botão iniciar
    if button_jogar_position.x <= mouse_pos.x <= button_jogar_position.x + button_size.x and button_jogar_position.y <= mouse_pos.y <= button_jogar_position.y + button_size.y:
        #Aqui será o botão cinza
        pygame.draw.rect(tela,color_light,(button_jogar_position, button_size))  
          
    else: 
         #Aqui será o botão preto
        pygame.draw.rect(tela,color_dark,(button_jogar_position, button_size))    

    #Botão quit

    # if button_quit_position.x <= mouse_pos.x <= button_quit_position.x + button_size.x and button_quit_position.y + button_size.y + button_size.y/2 <= mouse_pos.y <= button_quit_position.y + (button_size.y * 2) + button_size.y/2 :
    #     #Aqui será o botão cinza
    #     pygame.draw.rect(tela,color_light,(Vector2(button_quit_position.x, button_quit_position.y + button_size.y + button_size.y/2), button_size))
    # else: 
    #      #Aqui será o botão preto
    #     pygame.draw.rect(tela,color_dark,(Vector2(button_quit_position.x, button_quit_position.y + button_size.y + button_size.y/2), button_size)) 

    # #Aqui será os texto que representarão Jogar e Quit
        
    # if button_help_position.x <= mouse_pos.x <= button_help_position.x + button_size.x and button_help_position.y + button_size.y + button_size.y/2 <= mouse_pos.y <= button_help_position.y + (button_size.y * 2) + button_size.y/2 :
    #     #Aqui será o botão cinza
    #     pygame.draw.rect(tela,color_light,(Vector2(button_help_position.x, button_help_position.y + button_size.y + button_size.y/2), button_size))
    # else: 
    #      #Aqui será o botão preto
    #     pygame.draw.rect(tela,color_dark,(Vector2(button_help_position.x, button_help_position.y + button_size.y + button_size.y/2), button_size)) 

    #Aqui será os texto que representarão Jogar e Quit
    
     
    tela.blit(text_1, (tela_size.x/2 - 30,tela_size.y/2.5 + 210))  #texto 
    # tela.blit(text_2, (tela_size.x/2 - 20, tela_size.y/2.5 + 240))
    # tela.blit(text_3, (tela_size.x/2 - 30, tela_size.y/2.5 + 320))
    pygame.display.update()

while inGame:
    """main loop responsible for drawing things on the tela"""
    inGame = update()
    delta_time = pygame.time.get_ticks()
    left_click, scroll_click, right_click = pygame.mouse.get_pressed()

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
            del bullets[bullets.index(bullet)]
        else:
            collide_x = False
            collide_y = False
            
            b_width = bullet_origin.x - bullet_direction.x
            b_heigth = bullet_direction.y - bullet_origin.y
            
            b_angle = numpy.degrees(numpy.arctan(b_heigth / b_width))

            b_cos = numpy.cos(b_angle)
            b_sin = numpy.sin(b_angle) 
            if b_width<0:
                b_sin = -b_sin
                b_cos = -b_cos
                
            bullet_origin.y += b_cos * 0.1
            bullet_origin.x += b_sin * 0.1
            
            bullet_collide = projectile_collided(bullet_origin, bullet_direction, walls) | bullet_collide
            bullets[bullets.index(bullet)] = (bullet_collide, bullet_sense, bullet_origin, bullet_direction, bullet_size)
            pygame.draw.rect(tela, [255, 127, 0], (bullet_origin, bullet_size))

    # range_enemy = pygame.draw.circle(tela, (95,83,83), (enemy_position.x+10,enemy_position.y+10), radius);
    # raycast_line_e = pygame.draw.aaline(tela, [0, 255, 0], (enemy_position.x+10,enemy_position.y+10), player_position)
    
    enemy = pygame.draw.rect(tela, (240,42,42), Rect(enemy_position.x, enemy_position.y, 20, 20),2);
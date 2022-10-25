import pygame
from sys import exit
from typing import Tuple
from pygame import Color
from pygame.locals import *
from pygame import Vector2
from game.src.player import Player
from game.src.scene import Scene
from game.src.game import Game

game = Game()
phase_1 = Scene()
game.scenes.append(phase_1)
game.change_scene(game.scenes[0])
game.run()
# from Raycast import Raycast

# def coordinate(x: float, y: float) -> Vector2:
#     cx =  window.width / 2 
#     cy =  window.height / 2

#     return Vector2(cx + x, cy + y)

# def grid(base_color: Color = Color(255, 255, 255), axis_x_color: Color = Color(255, 0, 127), axis_y_color: Color = Color(0, 255, 127)) -> Tuple[Rect]:
#     axis_x = window.width / 2
#     axis_y = window.height / 2

#     pygame.draw.line(window.surface, axis_x_color, (0, axis_y), (window.width, axis_y))
#     pygame.draw.line(window.surface, axis_y_color, (axis_x, 0), (axis_x, window.height))

# pygame.init()
# pygame.font.init()
# font = pygame.font.SysFont("consolas", 12)

# skybox_sprite = pygame.image.load(".\\Game\\public\\skybox.png")
# player_icon_sprite = pygame.image.load(".\\Game\\public\\map_icon_1.png")
# texture_wall_sprite = pygame.image.load(".\\Game\\public\\texture_1.png")

# window = Window(size=Vector2(720, 480))
# player = Entity(player_icon_sprite, coordinate(0, 0))
# grid_on = True
# walls = []
# origin = Vector2(0, 0)

# while True:
#     for event in pygame.event.get():
#         if event.type == WINDOWCLOSE:
#             pygame.quit()
#             exit()

#     window.update_size(Vector2(window.surface.get_size()))
#     window.surface.fill([0]*3)

#     mouse = Vector2(pygame.mouse.get_pos())
#     # aim = Raycast(player.position, mouse, Color(0, 255, 0))
#     keys_pressed = pygame.key.get_pressed()
#     left, wheel, right = pygame.mouse.get_pressed()

#     # draw player and raycast
#     if grid_on:
#         grid()

#     player.update()
#     # aim.raycast()

#     # if player.shape in  wall.collidelist():
#     #     window.surface.blit(font.render(True, True, Color(100, 255, 100)), (Vector2(50, 10), Vector2(50, 10)))

#     if keys_pressed[K_a]:
#         player.position.x -= 0.1
#     elif keys_pressed[K_d]:
#         player.position.x += 0.1
#     if keys_pressed[K_w]:
#         player.position.y -= 0.1
#     elif keys_pressed[K_s]:
#         player.position.y += 0.1
#     if keys_pressed[K_TAB]:
#         grid_on = True if grid_on else False
#     if keys_pressed[K_SPACE]:
#         player.shape = pygame.transform.rotate(player.shape, 45)
#         angle = angle + 45 if angle < 360 else 0

#     pygame.display.flip()

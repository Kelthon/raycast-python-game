from ast import main
import pygame
import numpy as np
from sys import exit
from pygame.locals import *

posx = 200
posy = 200
main_window_width = 640
main_window_height = 640

pygame.init()

window = pygame.display.set_mode(size=(main_window_width, main_window_height))

    
while True:
    for event in pygame.event.get():
        if event.type == WINDOWCLOSE:
            pygame.quit()
            exit()
    window.fill([0]*3)
    mousex, mousey = pygame.mouse.get_pos()
    keys_pressed = pygame.key.get_pressed()
    
    for i in range(0, main_window_width+1, 64):
        pygame.draw.aaline(window, [80, 80, 80], (i, 0), (i, main_window_height))
    for i in range(0, main_window_height+1, 64):
        pygame.draw.aaline(window, [80, 80, 80], (0, i), (main_window_width, i))

    # Calc raycast line
    xc = main_window_width
    yc = main_window_height
    inclinacao = 1
    
    if mousex == posx:
        xc = mousex
        if mousey > posy:
            yc = main_window_height
        else:
            yc = 0
    elif mousey == posy:
        yc = mousey
        if mousex > posx:
            xc = main_window_width
        else:
            xc = 0
    else:
        if mousey < posy:

            yc = 0
            inclinacao = -(mousey - posy) / (mousex - posx)
            xc = mousex + ((mousey - yc) / inclinacao)

        else:
            yc = main_window_height
            inclinacao = (mousey - posy) / (mousex - posx)
            xc = mousex + ((yc - mousey) / inclinacao)   


    # draw player and raycast
    player = pygame.draw.circle(window, [255]*3, (posx, posy), 10)
    raycast = pygame.draw.aaline(window, [0, 255, 0], (posx, posy), (xc, yc))


    # player movement
    if keys_pressed[K_a] or keys_pressed[K_LEFT]:
        posx -= 0.1
    elif keys_pressed[K_d] or keys_pressed[K_RIGHT]:
        posx += 0.1
    if keys_pressed[K_w] or keys_pressed[K_UP]:
        posy -= 0.1
    elif keys_pressed[K_s] or keys_pressed[K_DOWN]:
        posy += 0.1
    else:
        pass

    pygame.display.flip()

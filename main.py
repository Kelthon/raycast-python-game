import pygame
import numpy as np
from sys import exit
from pygame.locals import *

posx = 200
posy = 200
main_window_width = 400
main_window_height = 400

pygame.init()

window = pygame.display.set_mode(size=(main_window_width, main_window_height))


while True:

    window.fill([0]*3)
    mousex, mousey = pygame.mouse.get_pos()
    keys_pressed = pygame.key.get_pressed()
    
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
            inclinacao = -(mousey - posy) / (mousex - posx)
            xc = mousex + ((yc - mousey) / inclinacao)
            yc = 0
        else:
            inclinacao = (mousey - posy) / (mousex - posx)
            xc = mousex + ((yc - mousey) / inclinacao)   

    circle = pygame.draw.circle(window, [255]*3, (posx, posy), 10)
    raycast = pygame.draw.aaline(window, [0, 255, 0], (posx, posy), (xc, yc))

    for event in pygame.event.get():
        if event.type == WINDOWCLOSE:
            pygame.quit()
            exit()

    if keys_pressed[K_a] or keys_pressed[K_LEFT]:
        posx -= 1
    elif keys_pressed[K_d] or keys_pressed[K_RIGHT]:
        posx += 1
    if keys_pressed[K_w] or keys_pressed[K_UP]:
        posy -= 1
    elif keys_pressed[K_s] or keys_pressed[K_DOWN]:
        posy += 1
    else:
        pass

    pygame.display.flip()

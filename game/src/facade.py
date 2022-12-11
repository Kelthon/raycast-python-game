import pygame
import pygame.locals as locals_namespace

"""Importing pygame modules with alias"""
key = pygame.key
draw = pygame.draw
font = pygame.font
time = pygame.time
mouse = pygame.mouse
mixer = pygame.mixer
event = pygame.event
image = pygame.image
local = locals_namespace
display = pygame.display
transform = pygame.transform

"""Importing pygame Classes with alias"""
Rect = pygame.Rect
Color = pygame.Color
Font = pygame.font.Font
Vector2 = pygame.Vector2
Surface = pygame.Surface

"""Initialize pygame"""
pygame.init()
mixer.init()
pygame.font.init()

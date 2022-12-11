import math
import numpy
from random import randint
from game.src.facade import *
from game.src.player import Player

class Enemy:
    def __init__(self, position: Vector2, player: Player, radius: float = 100) -> None:
        self.position = position
        self.radius = radius
        self.direction_move = 1
        self.player = player
        self.shape = None
    
    def update(self, surface=display.get_surface()):
        if surface is not None:
            self.shape = draw.rect(surface, (240,42,42), Rect(self.position.x, self.position.y, 20, 20),2)

    def move(self) -> None:
        """movement of enemy horizontally"""
        height = 0
        width = 0
        state = 1
        tan = 0
        res = 0
    
        if self.player.position.x >= self.position.x + 10 - self.radius:
            if self.player.position.x <= self.position.x + 10 + self.radius:
                if self.player.position.y >= self.position.y + 10 - self.radius:
                    if self.player.position.y <= self.position.y + 10 + self.radius:
                        width = self.player.position.x - self.position.x - 10
                        height = self.player.position.y - self.position.y - 10
                        tan = height/0.001 if width == 0 else height/width
                        
                        res = 1
                        sen = (numpy.sin(numpy.arctan(tan)) * res)
                        cos = (numpy.cos(numpy.arctan(tan)) * res)
                        if (width < 0):
                            sen = -sen
                            cos = -cos

                        self.position.y += sen * 0.2
                        self.position.x += cos * 0.2
                        state = 0

        if (math.floor(self.position.x) == 120):

            self.direction_move = 1;

        elif (math.floor(self.position.x) == 660):

            self.direction_move  = -1; 

        self.position.x += 0.2 * self.direction_move * state
    
    def respawn(self, position: Vector2) -> None:
        new_pos = Vector2(randint(50, position.x - 50), randint(50, position.y - 50))
        self.position = new_pos

    
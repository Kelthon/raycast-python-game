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
    
    def move(self) -> None:
        """movement of enemy horizontally"""
        height = 0
        width = 0
        state = 1
        tan = 0
        res = 0
        
        for position in self.position:
            if self.player.position.x >= position.x + 10 - self.radius:
                if self.player.position.x <= position.x + 10 + self.radius:
                    if self.player.position.y >= position.y + 10 - self.radius:
                        if self.player.position.y <= position.y + 10 + self.radius:
                            width = self.player.position.x - position.x - 10
                            height = self.player.position.y - position.y - 10
                            tan = height/0.001 if width == 0 else height/width
                            
                            res = 1
                            sen = (numpy.sin(numpy.arctan(tan)) * res)
                            cos = (numpy.cos(numpy.arctan(tan)) * res)
                            if (width < 0):
                                sen = -sen
                                cos = -cos

                            position.y += sen * 0.2
                            position.x += cos * 0.2
                            state = 0

            if (math.floor(position.x) == 120):

                self.direction_move = 1;

            elif (math.floor(position.x) == 660):

                self.direction_move  = -1; 
   
            position.x += 0.2 * self.direction_move * state
    
    def respawn(self, position: Vector2) -> None:
        new_pos = Vector2(randint(50, position.x - 50), randint(50, position.y - 50))
        self.position = new_pos

    
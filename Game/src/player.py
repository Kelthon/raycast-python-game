import pygame
from typing import List
from pygame.locals import *
from pygame import Rect, Vector2
from game.src.entity import Entity
from game.src.behavior import Behavior
from game.src.transform import Transform
from pygame.sprite import Sprite, collide_rect

class Player(Entity):
    def __init__(self, shape: Rect | None = None, transform: Transform = Transform(), behavior: Behavior = None) -> None:
        super().__init__(shape, transform, behavior)
        
    def start(self):
        w, h = pygame.display.get_surface().get_size()
        self.shape = pygame.transform.scale(self.shape, self.transform.scale)
        self.transform.position = Vector2((w - self.transform.scale.x) / 2, (h - self.transform.scale.y) / 2)
    
    def collide(self, rects: List[Rect]):
        collide_list = []
        self_rect = self.shape.get_rect()
        self_rect.update(self.transform.position, self.transform.scale)
        
        for rect in rects:
            if self_rect.colliderect(rect):
                if self_rect.top <= rect.bottom and self_rect.bottom > rect.bottom:
                    collide_list.append("top")

                if self_rect.bottom >= rect.top and self_rect.top < rect.top:
                    collide_list.append("bottom")
                
                if self_rect.right >= rect.left and self_rect.left < rect.left:
                    collide_list.append("right")
                
                if self_rect.left <= rect.right and self_rect.right > rect.right:
                    collide_list.append("left")

        return collide_list

    def update(self, map: List[Rect]):
        key = pygame.key.get_pressed()
        collision = self.collide(map)
        
        if not "top" in collision:
            if key[K_w]:
                self.transform.position.y -= 0.1
        
        if not "bottom" in collision:
            if key[K_s]:
                self.transform.position.y += 0.1

        if not "left" in collision:
            if key[K_a]:
                self.transform.position.x -= 0.1
        
        if not "right" in collision:
            if key[K_d]:
                self.transform.position.x += 0.1
            
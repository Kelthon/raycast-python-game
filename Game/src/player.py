import pygame
from pygame.locals import *
from pygame import Rect, Vector2, Color
from game.src.entity import Entity
from game.src.transform import Transform
from game.src.behavior import Behavior

class Player(Entity):
    def __init__(self, shape: Rect | None = None, transform: Transform = Transform(), behavior: Behavior = None) -> None:
        super().__init__(shape, transform, behavior)
        
    def start(self):
        w, h = pygame.display.get_surface().get_size()
        self.shape = pygame.transform.scale(self.shape, self.transform.scale)
        self.transform.position = Vector2((w - self.transform.scale.x) / 2, (h - self.transform.scale.y) / 2)

    def collide(self):
        print(self.shape.get_rect())

    def update(self):
        
        key = pygame.key.get_pressed()
        
        if key[K_w]:
            self.transform.position.y -= 0.1
        
        if key[K_s]:
            self.transform.position.y += 0.1

        if key[K_a]:
            self.transform.position.x -= 0.1
        
        if key[K_d]:
            self.transform.position.x += 0.1
        
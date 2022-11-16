import pygame
from typing import List
from pygame.locals import *
from pygame import Rect, Vector2
from game.src.entity import Entity
from game.src.behavior import Behavior
from game.src.transform import Transform

class enemy(Entity):
  def __init__(self, shape: Rect | None = None, transform: Transform = ..., behavior: Behavior = None) -> None:
    super().__init__(shape, transform, behavior)

  def start(self):
    w, h = pygame.display.get_surface().get_size();
    self.shape = pygame.transform.scale(self.shape, self.transform.scale)
    self.transform.position = Vector2((w - self.transform.scale.x), (h - self.transform.scale.y))

from pygame import Rect
from abc import ABC, abstractmethod
from game.src.behavior import Behavior
from game.src.transform import Transform

class Entity(ABC):
    def __init__(self, shape: Rect | None = None, transform: Transform = Transform(), behavior: Behavior = None) -> None:
        self.shape = shape
        self.behavior = behavior
        self.transform = transform

    def copy(self):
        return self.shape.copy()
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass
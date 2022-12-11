from game.src.facade import *

class Item:
    def __init__(self, filepath:str, size=Vector2(100, 100)) -> None:
        self.size = size
        self.surface = self.set_surface(filepath)

    def set_surface(self, filepath:str) -> None:
        self.surface = transform.scale(image.load(filepath), self.size)

    def get_surface(self) -> Surface:
        return self.surface

    @classmethod
    def get_surface_by_filepath(cls, filepath:str, size=Vector2(100, 100)) -> Surface:
        return transform.scale(image.load(filepath), size)




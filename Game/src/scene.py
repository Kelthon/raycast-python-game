from pygame import Color, Rect, draw
from typing import List
from game.src.entity import Entity
from game.src.constants import global_window

class Scene():
    def __init__(self) -> None:
        self.childrens: List[Entity] = []
        self.map = List[Rect]
        self.enemies = []
        self.items = []
        self.skybox = None

    def load_map(self):
        draw.rect(global_window.surface, Color(255, 255, 255), (0, 0, 50, 50))
        
        # for i in map:
        #     self.map.add(i)

    def add_children(self, children):
        self.childrens.append(children)
    
    def remove_children(self, children):
        self.childrens.remove(children)

    def init(self):
        for i in self.childrens:
            i.start()

    def draw_scene(self):
        self.load_map()

        for i in self.childrens:
            i.update()
            global_window.surface.blit(i.shape, i.transform.position)
    
    def change_scene(self, scene) -> None:
        pass
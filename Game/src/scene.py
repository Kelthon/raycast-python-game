from typing import List
from game.src.entity import Entity
from game.src.raycast import Raycast
from pygame import Color, Rect, Vector2, draw
from game.src.constants import global_window, player, Mouse

class Scene():
    def __init__(self) -> None:
        self.enemies: List[Entity] = []
        self.map: List[Rect] = []
        self.player = player 
        self.skybox = None
        self.items = []

    def load_map(self):
        self.map = [
            draw.rect(global_window.surface, Color(255, 255, 255), (50, 0, 50, 100)),
            draw.rect(global_window.surface, Color(255, 255, 255), (600, 50, 50, 300)),
            draw.rect(global_window.surface, Color(255, 255, 255), (500, 200, 100, 50)),
            draw.rect(global_window.surface, Color(255, 255, 255), (100, 199, 50, 50)),
            draw.rect(global_window.surface, Color(255, 255, 255), (200, 300, 50, 500)),
            draw.rect(global_window.surface, Color(255, 255, 255), (300, 350, 100, 50)),
            draw.rect(global_window.surface, Color(255, 255, 255), (50, 300, 25, 25)),
            draw.rect(global_window.surface, Color(255, 255, 255), (100, 300, 25, 25)),
            draw.rect(global_window.surface, Color(255, 255, 255), (50, 350, 25, 25)),
            draw.rect(global_window.surface, Color(255, 255, 255), (100, 350, 25, 25)),
            draw.rect(global_window.surface, Color(255, 255, 255), (50, 400, 25, 25)),
            draw.rect(global_window.surface, Color(255, 255, 255), (100, 400, 25, 25)),
            draw.circle(global_window.surface, Color(255, 255, 255), Vector2(400, 80), 50),
            draw.rect(global_window.surface, Color(255, 255, 255), (245, 180, 100, 40)),
            draw.rect(global_window.surface, Color(255, 255, 255), (375, 250, 40, 40)),
            draw.rect(global_window.surface, Color(255, 255, 255), (305, 250, 40, 40))
        ]

    def add_enemy(self, enemy):
        self.enemies.append(enemy)
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def init(self):
        if len(self.enemies):
            for i in self.enemies:
                i.start()

        self.player.start()

    def draw_scene(self):
        self.load_map()
        
        raycast = Raycast(Vector2(self.player.transform.position.x + self.player.transform.scale.x / 2, self.player.transform.position.y + self.player.transform.scale.y / 2), Vector2(Mouse.get_pos()), Color(0, 255, 0))
        raycast.shape

        self.player.update(self.map)
        global_window.surface.blit(self.player.shape, self.player.transform.position)

        for i in self.enemies:
            i.update()
            global_window.surface.blit(i.shape, i.transform.position)

    def change_scene(self, scene) -> None:
        pass
from typing import List, Tuple
from game.src.facade import *
from game.src.item import Item
from game.src.enemy import Enemy
from game.src.player import Player


class Level:
    def __init__(self, game_map: List[Rect], player: Player, enemy_list: List[Enemy], items_list: List[Item]) -> None:
        self.game_map: List[Rect] = game_map
        self.player: Player = player
        self.enemy_list: List[Enemy] = enemy_list
        self.items_list: List[Item] = items_list
        self.score = 0
        self.items_taken:List[Tuple(Surface, int)]  = []
        self.backup = {}
        self.save()

    def update(self):
        self.player.move_and_update()

        for enemy in self.enemy_list:
            enemy.move()

    def restart(self):
        self.score = self.backup["score"]
        self.player = self.backup["player"]
        self.game_map = self.backup["game_map"]
        self.emeny_list = self.backup["emeny_list"]
        self.items_list = self.backup["items_list"]
        self.items_taken = self.backup["items_taken"]

    def save(self):
        self.backup["score"] = self.score
        self.backup["player"] = self.player
        self.backup["game_map"] = self.game_map
        self.backup["emeny_list"] = self.enemy_list
        self.backup["items_list"] = self.items_list
        self.backup["items_taken"] = self.items_taken


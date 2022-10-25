import pygame

pygame.init()
pygame.font.init()

from game.src.window import Window
from game.src.scene import Scene
from game.src.game import Game

game = Game(True)
phase_1 = Scene()
game.scenes.append(phase_1)
game.change_scene(game.scenes[0])
game.run()

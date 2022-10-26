
import pygame

pygame.init()
pygame.font.init()

from game.src.scene import Scene
from game.src.game import Game

phase_1 = Scene()

game = Game()
game.scenes.append(phase_1)
game.change_scene(game.scenes[0])
game.run()

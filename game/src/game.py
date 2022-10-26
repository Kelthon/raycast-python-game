import pygame
from typing import List
from game.src.scene import Scene
from game.src.saver import Saver
from pygame import Vector2, Color, WINDOWCLOSE 
from game.src.constants import global_window

class Game():
    def __init__(self, debug: bool = False) -> None:
        self.scenes: List[Scene] = []
        self.window = global_window
        self.mouse = pygame.mouse
        self.isNotGameOver = True
        self.current_scene = None
        self.isNotClosed = True
        self.isNotPaused = True
        self.isDebug = debug
        self.saver = Saver()
        self.state = ""
        

    def save(self):
        self.saver.save("game.save", self.state)

    def load(self):
        self.state = self.saver.load("game.save", self.state)

    def change_scene(self, scene: Scene):
        self.current_scene = scene

    def run(self):

        self.current_scene.init()

        while self.isNotClosed:
            self.window.surface.fill(Color(0, 0, 0))
            
            if self.isDebug:
                pygame.draw.line(self.window.surface, Color(0, 255, 127), Vector2(self.window.width / 2, self.window.position.y), Vector2(self.window.width / 2, self.window.height))
                pygame.draw.line(self.window.surface, Color(255, 0, 127), Vector2(self.window.position.x , self.window.height / 2), Vector2(self.window.width, self.window.height / 2))
            
            self.current_scene.draw_scene()
            
            self.window.flip()
            
            for event in pygame.event.get():
                if event.type == WINDOWCLOSE:
                    self.isNotClosed = False
                    pygame.quit()

import pygame
from pygame import Vector2
from game.src.player import Player
from game.src.window import Window
from game.src.behavior import Behavior
from game.src.gamelogger import GameLogger
from game.src.transform import Transform

Mouse = pygame.mouse
Input = pygame.key
Image = pygame.image
Font = pygame.font

system_fonts = Font.get_fonts()
default_font = Font.SysFont(system_fonts[0], 15)
console_font = Font.SysFont("Consolas", 15) if "Consolas" in system_fonts else default_font

def from_origin(x: float, y: float):
    cx = global_window.width / 2 
    cy = global_window.height / 2

    return Vector2(cx + x, cy + y)

def isfont(name: str) -> bool:
    return name in system_fonts


global_window = Window (
    Vector2(0, 0), 
    Vector2(720, 480)
)

logger = GameLogger()

player = Player (
    Image.load(".\\Game\\public\\player_icon.png"),
    Transform  (
        global_window.center(),
        Vector2(0, 0),
        Vector2(16, 16)
    )
)


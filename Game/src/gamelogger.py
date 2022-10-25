from typing import Tuple
from pygame import Vector2, Surface, Color
from pygame.font import get_fonts, SysFont, Font
from os.path import exists
from datetime import datetime

class GameLogger():
    def __init__(self, filename: str = "game.log", position: Vector2 = Vector2(0, 0)) -> None:
        self.__default_style = self.style()
        self.__filename = filename
        self.position = position
        self.__number_lines = 0
        
        if not exists(filename):
            with open(file=self.__filename, mode="wt", encoding="utf-8") as logfile:
                logfile.close()

    def __get_default_style(self):
        return self.__default_style

    def get_format_date(self, format: str = "%m-%d-%Y %H:%M:%S") -> str:
        return datetime.now().strftime(format)

    def __write_logfile(self, string: str, mode: str):
        text = f"{self.get_format_date()} {mode} {string}\n"
        
        with open(file=self.__filename, mode="at", encoding="utf-8") as logfile:
            logfile.write(text)
            logfile.close()

    def style(self, position: Vector2 = Vector2(0, 0), text_color: Color = Color(255, 255, 255), bg_color: Color | None = None, font_family: Font = SysFont(get_fonts()[0], 15)) -> Tuple[Vector2, Color, Color | None, Font]:
        return (position, text_color, bg_color, font_family)

    def print(self, text: str, style: Tuple[Vector2, Color, Color | None, Font] | None = None):
        if style is None:
            style = self.__get_default_style()

        position, color, bgcolor, font = style
        text_surface = font.render(text, True, color, bgcolor)
        self.surface.blit(text_surface, position)
        self.__number_lines += 1

        

    def log(self, string):        
        self.__write_logfile(string, "log")

    def error(self, error):
        self.__write_logfile(error, "error")

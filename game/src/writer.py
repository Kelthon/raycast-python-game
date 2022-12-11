from game.src.facade import *


def get_font(font_name: str = font.get_default_font(), size: float = 25, bold: bool = False, italic: bool = False) -> Font:
    """Returns a system font"""
    sfont = font.SysFont(font_name, size, bold, italic)
    return sfont


def write(text: str, color: Color = Color(255, 255, 255), position: Vector2 = Vector2(0, 0), bg_color = None, font: Font = get_font()) -> Rect:
        """blit a text in screen"""
        render = font.render(text, True, color, bg_color)
        return pygame.display.get_surface().blit(render, position)


class Writer():
    def __init__(self, font: Font = font.get_default_font(), color: Color = Color(255, 255, 255), background_color: Color | None = None, is_bold: bool = False, is_italic: bool = False) -> None:
        self.font = self.set_font(font)
        self.font_size = self.set_font_size(25)
        self.font_color = self.set_font_color(color)
        self.font_background_color = self.set_font_background_color(background_color)
        self.font_bold = self.set_font_bold(is_bold)
        self.font_italic = self.set_font_italic(is_italic)

    def set_font(self, font: Font) -> None:
        self.font = font
        
    def get_font(self) -> Font:
        return self.font

    def set_font_size(self, size: float) -> None:
        self.font_size = size

    def get_font_size(self) -> float:
        return self.font_size

    def set_font_color(self, color: Color) -> None:
        self.font_color = color

    def get_font_color(self) -> Color:
        return self.font_color

    def set_font_background_color(self, background_color: Color) -> None:
        self.font_background_color = background_color

    def get_font_background_color(self) -> Color:
        return self.font_background_color

    def set_font_bold(self, is_bold: bool) -> None:
        self.font_bold = is_bold

    def get_font_bold(self) -> bool:
        return self.font_bold

    def set_font_italic(self, is_italic: bool) -> None:
        self.font_italic = is_italic

    def get_font_italic(self) -> bool:
        return self.font_italic

    def write(self, text: str, position: Vector2 = Vector2(0, 0)) -> Rect:
        """blit a text in screen"""
        render = font.render(text, True, self.font_color, self.font_background_color)
        return display.get_surface().blit(render, position)
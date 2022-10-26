from pygame import Surface, Vector2, display, init
from pygame.locals import *
from game.src.box import Box

class Window(Box):
    def __init__(self, position: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(0, 0), padding: Vector2 = Vector2(0, 0), 
        margin: Vector2 = Vector2(0, 0), background_color: Color = Color(0, 0, 0), caption: str = "Untitled Project", 
        icontitle: str | None = None, icon: Surface | None = None) -> None:

        super().__init__(position, size, padding, margin)
        self.background_color = background_color
        self.text_color = Color(255, 255, 255)
        self.surface = display.set_mode((self.width, self.height), RESIZABLE)
        self.surface = display.set_mode(size=(self.width, self.height))
        self.caption = caption
        self.icontitle = icontitle
        self.icon = icon

        if self.icontitle is None:
            display.set_caption(self.caption) 
        else:
            display.set_caption(self.caption, self.icontitle) 
        
        if self.icontitle is not None:
            display.set_icon(self.icon)

        init()

    def center(self):
        return Vector2(self.width / 2, self.height / 2)

    def set_mode(self, size = Vector2(0, 0), flags=0, depth=0, displays=0, vsync=0):
        self.surface = display.set_mode(size, flags, depth, displays, vsync)

    def toggle_fullscreen(self):
        display.toggle_fullscreen()

    def flip(self):
        display.flip()

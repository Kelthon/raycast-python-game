from game.src.utils import *
from game.src.facade import *

class Window:

    def __init__(self, size, background_color: Color = Color(0, 0, 0), background_image: Surface | None = None) -> None:
        self.size = size
        self.background_image = background_image
        self.background_color = background_color
        self.surface = display.set_mode(self.size, local.RESIZABLE)
    
    def center(self) -> Vector2:
        return center(self.size)

    def update(self) -> None:
        """Update tela surface"""
    
        display.flip()
        self.surface.fill(self.background_color)
        self.surface.blit(self.background_image, (0, 0))

    def close(self) -> None:
        for e in event.get():
            if e.type == local.WINDOWCLOSE:
                exit()
    
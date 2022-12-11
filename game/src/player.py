# from game.src.facade import *
from game.src.facade import *
from typing import List, Dict, overload

class Walker():
    def __init__(self, position, speed, size) -> None:
        self.position: Vector2 = position
        self.speed: float = speed
        self.size: Vector2 = size

    def move(self, direction: Vector2):
        self.position.x += self.speed * direction.x 
        self.position.y += self.speed * direction.y
    

class Collider():
    top = 1
    down = 2
    left = 3
    right = 4

    def __init__(self) -> None:
        self.colliders = []

    def get_colliders(self):
        return self.colliders

    @overload
    def add(self, rect: Rect):
        ...

    @overload
    def add(self, rectlist: List[Rect]):
        ...

    def add(self, obj: Rect | List[Rect]):
        if isinstance(obj, Rect):
            self.colliders.append(obj)
        elif isinstance(obj, list):
            for rect in obj:
                if isinstance(rect, Rect):
                    self.colliders.append(rect)
                else:
                    raise TypeError("Insertion Failure: List with disallowed types in " + rect + " of type " + type(rect))
        else:
            raise TypeError("Invalid types: rectlist argument must be of type Rect or List[Rect]")

    @overload
    def remove(self, rect: Rect):
        ...

    @overload
    def remove(self, index: int):
        ...

    @overload
    def remove(self, rectlist: List[Rect]):
        ...

    def remove(self, obj: Rect | int | List[Rect]) -> None:
        if isinstance(obj, Rect):
            self.colliders.remove(obj)
        elif isinstance(obj, int):
            del self.colliders[obj]
        elif  isinstance(obj, list):
            for rect in obj:
                if isinstance(rect, Rect):
                    self.colliders.remove(rect)
                else:
                    raise TypeError("Remotion Failure: List with disallowed types in " + rect + " of type " + type(rect))
        else:
            raise TypeError("arg rectlist should be a int, Rect or List[Rect]")

    def get_collision_direction(self, rect: Rect):
        """Returns a string where has the collision with something

        :params rect: represents something
        :type rect: Rect

        :returns: a int list with all collisions
        :rtype: List[int]
        """

        collide_list = []

        for collider in self.colliders:
            if rect.colliderect(collider):
                if rect.top <= collider.bottom and rect.bottom > collider.bottom:
                    collide_list.append(Collider.top)

                if rect.bottom >= collider.top and rect.top < collider.top:
                    collide_list.append(Collider.down)
                
                if rect.right >= collider.left and rect.left < collider.left:
                    collide_list.append(Collider.right)
                
                if rect.left <= collider.right and rect.right > collider.right:
                    collide_list.append(Collider.left)

        return collide_list


class Player(Walker):
    def __init__(self, position: Vector2, speed: float, size: Vector2, collider: Collider, binds) -> None:
        super().__init__(position, speed, size)
        self.collider = collider
        self.shape = None
        self.set_binds(binds)
        self.update()

    def set_binds(self, binds):
        self.binds = binds

    def update(self, surface=display.get_surface()) -> None:
        if surface is None:
            return
        else:
            self.shape = draw.circle(surface, [255]*3, self.position, self.size)

    def move(self) -> None:
        if self.shape is not None:
            pressed_keys = key.get_pressed()
            collisions = self.collider.get_collision_direction(self.shape)

            for bind in self.binds:

                pkey = bind["key"]
                pcol = bind["col"]
                pdir = bind["dir"]

                if pressed_keys[pkey] and not pcol in collisions:
                    super().move(pdir)

    def move_and_update(self) -> None:
        self.move()
        self.update()


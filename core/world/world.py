from .tile import Tile
from ..entity.unit import Unit

import random
from ..constant import move_cmd, FOOD

"""
2D Grid map. And includes other information.
actually has pseudo-depth
"""


class World:
    width:2
    height:2
    map:list[list[Tile]]
    unit:list[Unit]

    @property
    def width(self):
        return len(self.map)
    @property
    def height(self):
        return len(self.map[0])

    def __init__(self) -> None:
        self.map = [[Tile(), Tile()], [Tile(), Tile()]]
        pass
    @staticmethod
    def new_size(width,height):
        res=World()
        res.map=[[Tile() for _ in range(width)] for _ in range(height)]

        return res

    def add_unit(self, u: Unit):
        u.pos_x = random.randint(1, self.width - 1)
        u.pos_y = random.randint(1, self.height - 1)
        if (not hasattr(self, "unit")): self.unit: list[Unit] = []
        self.unit.append(u)
        try:
            self.map[u.pos_x][u.pos_y].append(u)
        except:
            pass
    def __getitem__(self, key):
        if not isinstance(key, tuple) or len(key) != 2:
            raise IndexError("Index must be a tuple of length 2")

        posx, posy = key
        if posx < 0 or posx >= self.width or posy < 0 or posy >= self.height:
            return None
    def __setitem__(self, key, value):
        if not isinstance(key, tuple) or len(key) != 2:
            raise IndexError("Index must be a tuple of length 2")

        posx, posy = key
        if posx < 0 or posx >= self.width or posy < 0 or posy >= self.height:
            raise IndexError("Index out of range")

        self.map[posy][posx] = value

        return self.map[posy][posx]
    #other status

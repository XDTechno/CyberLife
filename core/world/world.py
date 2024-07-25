from .tile import Tile
from ..entity.unit import Unit

import random
from ..constant import move_cmd, FOOD

"""
2D Grid map. And includes other information.
actually has pseudo-depth
"""


class World:
    width: 2
    height: 2
    map: list[list[Tile]]
    unit: list[Unit]

    def __init__(self) -> None:
        self.map = [[Tile(), Tile()], [Tile(), Tile()]]
        pass

    def new_size(width, height):
        res = World()
        res.width, res.height = width, height
        res.map = [[Tile() for _ in range(width)] for _ in range(height)]

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
    #other status

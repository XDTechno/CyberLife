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

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)
    
    map:list[list[Tile]]
    #y lines ,each line contains x elements
    # [
    #   [x1y1,x2y1,x3y1],
    #   [x1y2,x2y2,x3y2],
    #   [x1y3,x2y3,x3y3]
    # ]
    unit:list[Unit]

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
        if not hasattr(self, "unit"):
            self.unit: list[Unit] = []
        self.unit.append(u)
        try:
            self[u.pos_x,u.pos_y].append(u)
        except:
            pass
    def __getitem__(self, key):
        if not isinstance(key, tuple) or len(key) != 2:
            raise IndexError("Index must be a tuple of length 2")
        posx, posy = key
        if posx < 0 or posx >= self.width or posy < 0 or posy >= self.height:
            return None
        else: return self.map[posy][posx]
    def __setitem__(self, key, value):
        if not isinstance(key, tuple) or len(key) != 2:
            raise IndexError("Index must be a tuple of length 2")

        posx, posy = key
        if posx < 0 or posx >= self.width or posy < 0 or posy >= self.height:
            raise IndexError("Setting items out of range")

        self.map[posy][posx] = value

        return self
    def closest_map(self,_from:tuple,item,**args):
        px,py=_from
        collectee=[]
        filter=item if callable(item) else lambda i:item in i
        distance=lambda dx,dy:abs(dx**2+dy**2) if "distance" not in args else args['distance']
        for ir, row in enumerate(self.map):
            for ic, cell in enumerate(row):
                if filter(cell) :
                    collectee.append((ic, ir, distance(ir - px,ic - py)))
        if len(collectee)>0:
            return min(collectee,lambda n:n[2])
        return None
    def closest_unit(self,_from:tuple,item,**args):
        px,py=_from
        collectee=[]
        filter=item if callable(item) else lambda i:item in i
        distance=lambda dx,dy:abs(dx**2+dy**2) if "distance" not in args else args['distance']
        for idx,u in enumerate(self.unit):
            if(filter (u)):
                collectee.append((idx,distance(u.pos_x-px,u.pos_y-py)))
        if len(collectee)>0:
            return min(collectee,lambda n:n[2])
        return None
    #other status

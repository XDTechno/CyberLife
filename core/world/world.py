from .tile import Tile
from ..entity.unit import Unit
"""
2D Grid map. And includes other information.
actually has pseudo-depth
"""
class World:
    map:list[list[Tile]]
    unit:list[Unit]

    def __init__(self) -> None:
        self.map=[[Tile()]]
        self.unit=[Unit(),Unit(),Unit(),Unit(),Unit()]
        pass
    def new_size(width,height):
        res=World()
        res.map=[[Tile() for _ in range(width)] for _ in range(height)]
        return res
    #other status
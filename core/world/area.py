from typing import Tuple,Callable
from core.world.world import World
type Point=Tuple[int,int]
class AreaNode:
    start:Point
    end:Point
    def each(self):
        for y_index in range(self.start[1],self.end[1]+1):
            for x_index in range(self.start[0],self.end[0]+1):
                yield (x_index,y_index)
        pass

class AreaBranch:
    #and areabranch
    sub=[]#:list[AreaNode|any]
    def each(self):
        all_res=set()
        for n in self.sub:
            for d in n.each():
                if not d in all_res:
                    all_res.add(d)
                    yield d
        self.cached_res=all_res
class MountedBranch:
    target:World
    origin:Point
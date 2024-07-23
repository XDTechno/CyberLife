from .tile import Tile
from ..entity.unit import Unit
import random
from ..constant import move_cmd,FOOD
"""
2D Grid map. And includes other information.
actually has pseudo-depth
"""
def test_findfood(self:Unit,wld):
    foods=[]
    (px,py)=(self.pos_x,self.pos_y)
    for (ir,row) in enumerate(wld.map):
        for (ic,cell) in enumerate(row):
            if FOOD in cell:
                foods.append((
                    ir,ic,abs((ir-px)**2+(ic-py)**2)))
    if(len(foods)>0):
        target =min(foods, key=lambda x: x[2])
        print(f"[{self.id}@{self.pos_x}:{self.pos_y}] going for food@{target[0]}:{target[1]}")
        dx,dy=px-target[0],py-target[1]
        if abs(dx) > abs(dy):
            if dx>0 :return 'left'
            else :return "right"
        else :
            if dy>0:return 'up'
            else :return 'down'
    else:
        pass
    return "shish"
class World:
    map:list[list[Tile]]
    unit:list[Unit]

    def __init__(self) -> None:
        self.map=[[Tile()]]
        self.unit=[]
        for _ in range(3):self.add_unit(Unit())
        self.add_unit(Unit.new_act(lambda _,_1:random.sample(sorted(move_cmd),1)[0]))
        self.add_unit(Unit.new_act(test_findfood))
        self.add_unit(
            Unit.new_act(
                lambda _,wld:wld.map
                [random.randint(1,wld.width-1)]
                [random.randint(1,wld.height-1)].append(FOOD)))
        
        pass
    def new_size(width,height):
        res=World()
        res.width,res.height=width,height
        res.map=[[Tile() for _ in range(width)] for _ in range(height)]
        return res
    def add_unit(self,u:Unit):
        self.unit.append(u)
        try:
            self.map[u.pos_x][u.pos_y].append(u)
        except:
            pass
    #other status
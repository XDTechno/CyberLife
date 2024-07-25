from core.entity.unit import Unit
from core.world.world import World
from core.world.tile import Tile
from core.util.scheduler import Scheduler
from view.base_view import View
from colorama import Back,Style,Fore
from core.constant import FOOD 
import time,random
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
        if(target[2]==0):
            tempref:Tile= wld.map[target[0]][target[1]]
            tempref.pop(tempref.index(FOOD))
            print(f"{self.id} ate the food@{self.pos_x}:{self.pos_y}")
            return None
        print(f"{self.id}@{self.pos_x}:{self.pos_y} -->food@{target[0]}:{target[1]}")
        dx,dy=px-target[0],py-target[1]
        if abs(dx) > abs(dy):
            if dx>0 :return 'left'
            else :return "right"
        else :
            if dy>0:return 'up'
            else :return 'down'
    else:
        pass
    return None
def test_setfood(self:Unit,wld):
    pos1=random.randint(1,wld.width-1)
    pos2=random.randint(1,wld.height-1)
    wld.map[pos1][pos2].append(FOOD)
    print(f"{self.id} put food@{pos1}:{pos2}")
def dealEntity(unit:Unit,wld:World=0):
    dna_iter=0
    count=0
    uDNA=unit.DNA
    while(dna_iter<len(unit.DNA)-1):
        dna_iter+=1
        if(uDNA[dna_iter]>30):
            count+=1
    print(f"{unit.id}'s gene larger than 30 is of {count}")
    unit.try_mutate()

def launch():
    scheduler=Scheduler.new_with_world(World.new_size(8,8))

    for _ in range(4):scheduler.world.add_unit(Unit.new_act(test_findfood))
    for _ in range(2):scheduler.world.add_unit(Unit.new_act(test_setfood))
    view=View()
    view.title="Pacman"
    view.on_message(lambda mes:print(Back.BLACK+Fore.WHITE+f"some bastard said {mes}"+Style.RESET_ALL))
    view.send("LAUNCH!")
    
    while True:
        time.sleep(0.5)

        #something concerned outside the world should be dealt here.
        res=scheduler.next()
        if res is not None:
            pass
        view.update_map(scheduler.world)

if __name__=="__main__":
    launch()

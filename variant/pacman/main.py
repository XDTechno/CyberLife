from core.entity.unit import Unit
from core.world.world import World
from core.util.scheduler import Scheduler
from view.base_view import View
import time
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

    view=View()
    view.title="Pacman"
    view.on_message(lambda mes:print("some bastard said {mes}"))
    view.send("LAUNCH!")
    
    scheduler.set(deal_unit=dealEntity).next()
    while True:
        time.sleep(1)
        scheduler.next()
        view.update_map(scheduler.world)
        view.send("tickle~")
if __name__=="__main__":
    launch()
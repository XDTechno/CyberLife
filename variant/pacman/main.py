from core.entity.unit import Unit
from core.world.world import World
from core.util.scheduler import Scheduler
from view.base_view import View
from colorama import Back,Style,Fore
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
    view.on_message(lambda mes:print(Back.BLACK+Fore.WHITE+f"some bastard said {mes}"+Style.RESET_ALL))
    view.send("LAUNCH!")
    
    scheduler.next()
    while True:
        time.sleep(0.5)

        #something concerned outside the world should be dealt here.
        scheduler.next()
        view.update_map(scheduler.world)
        # view.send("tickle~")
if __name__=="__main__":
    launch()

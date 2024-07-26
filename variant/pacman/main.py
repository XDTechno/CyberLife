from core.entity.unit import Unit
from core.world.world import World
from core.world.tile import Tile
from core.util.scheduler import Scheduler
from view.base_view import View
from colorama import Back, Style, Fore
from core.constant import FOOD
from core import constant
import time, random
from view.tui_view import TuiView
from core.constant import move_cmd,Eat,Gofor
view:View=...
def catch_pacman(self:Unit,wld):
    filterfn=lambda t:t.pos_x == self.pos_x and t.pos_y == self.pos_y and t is not self
    if len(list(filter(filterfn,wld.unit)))>0:
        return constant.Kill
    else :return (Gofor,constant.Pacman)

def test_findfood(self: Unit, wld):
    if FOOD in wld.map[self.pos_x][self.pos_y]:
        return Eat
    else :return (Gofor,FOOD)


def test_setfood(self: Unit, wld):
    pos1 = random.randint(1, wld.width - 1)
    pos2 = random.randint(1, wld.height - 1)
    wld.map[pos1][pos2].append(FOOD)
    global view
    view.send(f"{self.id} put food@{pos1}:{pos2}")


def dealEntity(unit: Unit, wld: World = 0):
    dna_iter = 0
    count = 0
    uDNA = unit.DNA
    while dna_iter < len(unit.DNA) - 1:
        dna_iter += 1
        if uDNA[dna_iter] > 30:
            count += 1
    print(f"{unit.id}'s gene larger than 30 is of {count}")
    unit.try_mutate()


def launch(view_type: View):
    scheduler = Scheduler.new_with_world(World.new_size(16, 16))

    global view 
    view= view_type
    for _ in range(4):
        scheduler.world.add_unit(Unit.new_act(test_findfood))
    for _ in range(2):
        scheduler.world.add_unit(Unit.new_act(test_setfood))
    scheduler.world.add_unit(Unit.new_act(catch_pacman))
    view.title = "Pacman"
    view.on_message(
        lambda mes: print(
            Back.BLACK + Fore.WHITE + f"some bastard said {mes}" + Style.RESET_ALL
        )
    )
    view.send("LAUNCH!")

    while True:
        time.sleep(0.5)
        if random.random()>0.8:view.send("~")
        # something concerned outside the world should be dealt here.
        res = scheduler.next(view=view)
        
        if res is not None:
            pass
        view.update_map(scheduler.world)


if __name__ == "__main__":
    launch()

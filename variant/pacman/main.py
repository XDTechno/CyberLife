from core.entity.unit import Unit
from core.world.world import World
from core.world.tile import Tile
from core.util.scheduler import Scheduler
from view.base_view import View
from colorama import Back, Style, Fore
from core.constant import FOOD
import time, random
from view.tui_view import TuiView
from core.constant import move_cmd,Eat
def catch_pacman(self:Unit,wld):
    huntee = []
    (px, py) = (self.pos_x, self.pos_y)
    for index, target in enumerate(wld.unit):
        if target==self:
            continue
        dist=abs(px+py-target.pos_x-target.pos_y)
        huntee.append((target.pos_x,target.pos_y,dist,index))
    if len(huntee) > 0:
        target = min(huntee, key=lambda x: x[2])
        if target[2] == 0:
            
            print(f"{self.id} killing the pacman<{wld.unit[target[3]].id}>@{self.pos_x}:{self.pos_y}")
            if random.random()>0.4:
                wld.unit.pop(target[3])
            return None
        print(f"{self.id}@{self.pos_x}:{self.pos_y} -->pacman@{target[0]}:{target[1]}")
        dx, dy = px - target[0], py - target[1]
        if abs(dx) > abs(dy):
            if dx > 0:
                return move_cmd["left"]
            else:
                return move_cmd["right"]
        else:
            if dy > 0:
                return move_cmd["up"]
            else:
                return move_cmd["down"]
    else:
        pass
    return None
    pass
def test_findfood(self: Unit, wld):
    foods = []
    (px, py) = (self.pos_x, self.pos_y)
    for ir, row in enumerate(wld.map):
        for ic, cell in enumerate(row):
            if FOOD in cell:
                foods.append((ir, ic, abs((ir - px) ** 2 + (ic - py) ** 2)))
    if len(foods) > 0:
        target = min(foods, key=lambda x: x[2])
        if target[2] == 0:
            return Eat
        print(f"{self.id}@{self.pos_x}:{self.pos_y} -->food@{target[0]}:{target[1]}")
        dx, dy = px - target[0], py - target[1]
        if abs(dx) > abs(dy):
            if dx > 0:
                return move_cmd["left"]
            else:
                return move_cmd["right"]
        else:
            if dy > 0:
                return move_cmd["up"]
            else:
                return move_cmd["down"]
    else:
        pass
    return None


def test_setfood(self: Unit, wld):
    pos1 = random.randint(1, wld.width - 1)
    pos2 = random.randint(1, wld.height - 1)
    wld.map[pos1][pos2].append(FOOD)
    print(f"{self.id} put food@{pos1}:{pos2}")


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
    scheduler = Scheduler.new_with_world(World.new_size(8, 8))

    view = view_type
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

        # something concerned outside the world should be dealt here.
        res = scheduler.next()
        if res is not None:
            pass
        view.update_map(scheduler.world)


if __name__ == "__main__":
    launch()

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
from core.constant import move_cmd, Eat, Gofor

view: View = ...


def test_catchpacman(self: Unit, wld):
    filterfn = lambda t: t.pos_x == self.pos_x and t.pos_y == self.pos_y and t is not self
    if len(list(filter(filterfn, wld.unit))) > 0:
        return constant.Kill
    else:
        return Gofor, constant.Pacman


def test_findfood(self: Unit, wld):
    if FOOD in wld[self.pos_x, self.pos_y]:
        return Eat
    else:
        return [Gofor, FOOD]


def test_setfood(self: Unit, wld: World):
    pos_x = random.randint(1, wld.width - 1)
    pos_y = random.randint(1, wld.height - 1)
    wld[pos_x, pos_y].append(FOOD)
    global view
    view.send(f"{self.id} put food@{pos_x}:{pos_y}")


# def dealEntity(unit: Unit, wld: World = 0):
#     dna_iter = 0
#     count = 0
#     uDNA = unit.DNA
#     while dna_iter < len(unit.DNA) - 1:
#         dna_iter += 1
#         if uDNA[dna_iter] > 30:
#             count += 1
#     print(f"{unit.id}'s gene larger than 30 is of {count}")
#     unit.try_mutate()


def launch(view_instance: View, time_flow=1):
    """
    main entrance of the simulation
    here deals with view and the model
    maybe outer interactions too"""

    world = World.new_size(8, 8)
    scheduler = Scheduler(world)

    global view
    view = view_instance
    for _ in range(4):
        scheduler.world.add_unit(Unit(test_findfood))
    for _ in range(2):
        scheduler.world.add_unit(Unit(test_setfood))
    # scheduler.world.add_unit(Unit(test_catchpacman, id="Killer"))
    view.title = "Pacman"
    view.on_message(
        lambda mes: print(
            Back.BLACK + Fore.WHITE + f"someon said {mes}" + Style.RESET_ALL
        )
    )
    view.send("Basic text view launched")

    while True:
        time.sleep(0.5 / time_flow)

        result = scheduler.next(view=view)
        if result is not None:
            pass
        view.update_map(scheduler.world)


if __name__ == "__main__":
    launch(View(), 10)

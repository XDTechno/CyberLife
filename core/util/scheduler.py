from ..world.world import World
from ..entity.unit import Unit
from ..constant import move_cmd, move_direction,Eat,FOOD
from colorama import Fore, Style


def default_dealer(du, wld):
    if hasattr(du, "act"):
        return du.act(du, wld)
    else:
        return "yep"
"""
manage the time process
"""
def recv_cmd(cur_unit:Unit,wld:World,cmd):
    if cmd == "yep":
        return None
    if cmd in move_cmd:
        cmd=move_cmd[cmd]
    if cmd in move_direction:
        dx, dy = move_direction[cmd]
        npx, npy = (cur_unit.pos_x + dx, cur_unit.pos_y + dy)
        if  npx > 0 and npx < wld.width and npy > 0 and npy < wld.height :
            cur_unit.pos_x, cur_unit.pos_y = npx, npy
        return None
    if cmd == Eat :
        tempref = wld.map[cur_unit.pos_x][cur_unit.pos_y]
        tempref.pop(tempref.index(FOOD))
        print(f"{cur_unit.id} ate the food@{cur_unit.pos_x}:{cur_unit.pos_y}")
        pass

class Scheduler:
    world: World
    cur_round: int = 0

    # the index of current entity being handled
    loop_iter: int = 0

    def __init__(self):
        # function used to handle the unit
        self.deal_unit = default_dealer
        self.cur_round = 0

    def next(self):
        # at current stage, each call deals one unit.
        if self.loop_iter > len(self.world.unit) - 1:
            self.loop_iter = 0
            self.cur_round += 1
            print(Fore.GREEN + " " * 6 + f"Round {self.cur_round}" + Style.RESET_ALL)

        cur_unit = self.world.unit[self.loop_iter]
        self.loop_iter += 1

        res = recv_cmd(cur_unit,self.world,self.deal_unit(cur_unit, self.world))
        if res is not None:
            pass
        return res

        

    @staticmethod
    def new_with_world(wld: World):
        res = Scheduler()
        res.world = wld
        return res

    # chain set
    def set(self, **args):
        if "deal_unit" in args:
            self.deal_unit = args["deal_unit"]
        return self

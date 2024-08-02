from ..world.world import World
from ..entity.unit import Unit
from ..constant import move_cmd, move_direction, Eat, FOOD, Gofor, Pacman, Kill
from .. import constant
from colorama import Fore, Style
from core.util.recv_f import recv_cmd


def default_dealer(u, wld):
    # use Unit.act as default
    if hasattr(u, "act"):
        return u.act(u, wld)
    else:
        return "Noob Unit"


def choose_direction_deprecated(dx, dy):
    # should be removed or lifted to __init__
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


class Scheduler:
    """
    manage the time process
    """
    world: World
    cur_round: int = 0
    # the index of current entity being handled
    loop_iter: int = 0
    # process the unit. the result will be sent to recv_cmd
    deal_unit: ...

    def __init__(self, world: World, dealfn=default_dealer):
        self.world = world
        # function used to handle the unit
        self.deal_unit = dealfn
        self.cur_round = 0

    def next(self, **args):
        # if all creatures has act, then go to next round
        if self.loop_iter > len(self.world.unit) - 1:
            self.loop_iter = 0
            self.cur_round += 1
            print(Fore.GREEN + " " * 6 + f"Round {self.cur_round}" + Style.RESET_ALL)

        cur_unit = self.world.unit[self.loop_iter]
        self.loop_iter += 1

        # the result of one unit's action. May need to handle if unit required
        action_result = recv_cmd(
            cur_unit,
            self.world,
            self.deal_unit(cur_unit, self.world),
            args['view'])

        if action_result is not None:
            if action_result == "Raise Biohazard Level":
                pass
            elif action_result == "Change weather to DaHuangXingYun":
                pass
        return action_result

    def set(self, **args):
        if "deal_unit" in args:
            self.deal_unit = args["deal_unit"]
        return self

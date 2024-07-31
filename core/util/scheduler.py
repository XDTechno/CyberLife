from ..world.world import World
from ..entity.unit import Unit
from ..constant import move_cmd, move_direction, Eat, FOOD, Gofor, Pacman, Kill
from .. import constant
from colorama import Fore, Style
from core.util.recv_f import recv_cmd as recv_cmd_by_search

def default_dealer(u, wld):
    #use Unit.act as default
    if hasattr(u, "act"):
        return u.act(u, wld)
    else:
        return "Noob Unit"


def choose_direction_deprecated(dx, dy):
    #should be removed or lifted to __init__
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





def recv_cmd_deprecated(cur_unit: Unit, wld: World, cmd, view):
    """
    primitive recv_cmd.
    """
    if cmd == "yep":
        return None
    if cmd in move_cmd:
        cmd = move_cmd[cmd]
    if cmd in move_direction:
        dx, dy = move_direction[cmd]
        npx, npy = (cur_unit.pos_x + dx, cur_unit.pos_y + dy)
        if wld[npx,npy]:
            # Clear the original coordinates of the unit in the world
            wld[cur_unit.pos_x,cur_unit.pos_y].remove(cur_unit)
            # Add the unit in the world (simulate move)
            cur_unit.pos_x, cur_unit.pos_y = npx, npy
            wld.map[npx][npy].append(cur_unit)
        return None
    if cmd == Eat :
        # tempref = wld.map[cur_unit.pos_x][cur_unit.pos_y]
        # tempref.pop(tempref.index(constant.FOOD))
        wld[cur_unit.pos_x,cur_unit.pos_y].remove(constant.FOOD)
        print(f"{cur_unit.id} ate the food@{cur_unit.pos_x}:{cur_unit.pos_y}")
        pass
    if cmd == Kill:
        index = ...
        (uidx,_)=wld.closest_unit((cur_unit.pos_x,cur_unit.pos_y),lambda i:i is not cur_unit)
        wld.unit.pop(uidx)
        pass
    if isinstance(cmd, tuple):
        if cmd[0] == Gofor:
            target = ...
            match cmd[1]:
                case constant.FOOD:
                    foods = []
                    (px, py) = (cur_unit.pos_x, cur_unit.pos_y)
                    # Todo 修改食物寻找方法，每次找食物都把地图找个遍也太神秘了
                    for ir, row in enumerate(wld.map):
                        for ic, cell in enumerate(row):
                            if FOOD in cell:
                                foods.append((ir, ic, abs((ir - px) ** 2 + (ic - py) ** 2)))
                    pass
                    if len(foods) <= 0:
                        return None
                    # find the closest food
                    target = min(foods, key=lambda x: x[2])

                    if view:
                        # the unit in the (pos_x, pos_y) wants to eat food in the (target[0],target[1])
                        view.send(f"{cur_unit.id}@{cur_unit.pos_x},{cur_unit.pos_y} --> food@{target[0]},{target[1]}")

                    dx, dy = cur_unit.pos_x - target[0], cur_unit.pos_y - target[1]
                    return recv_cmd_deprecated(cur_unit, wld, choose_direction_deprecated(dx, dy), view)

                case constant.Pacman:
                    huntee = []

                    (px, py) = (cur_unit.pos_x, cur_unit.pos_y)
                    for index, target in enumerate(wld.unit):
                        if target == cur_unit:
                            continue
                        dist = abs(px + py - target.pos_x - target.pos_y)
                        huntee.append((target.pos_x, target.pos_y, dist, index))
                    if len(huntee) <= 0:
                        return None
                    target = min(huntee, key=lambda x: x[2])

                    if view:
                        view.send(f"{cur_unit.id}@{cur_unit.pos_x},{cur_unit.pos_y} --> Pacman@{target[0]},{target[1]}")
                    dx, dy = cur_unit.pos_x - target[0], cur_unit.pos_y - target[1]
                    return recv_cmd_deprecated(cur_unit, wld, choose_direction_deprecated(dx, dy), view)

        pass


class Scheduler:
    """
    manage the time process
    """
    world: World
    cur_round: int = 0
    # the index of current entity being handled
    loop_iter: int = 0
    #process the unit. the result will be sent to recv_cmd
    deal_unit:...
    def __init__(self, world: World,dealfn=default_dealer):
        self.world = world
        # function used to handle the unit
        self.deal_unit = dealfn
        self.cur_round = 0

    def next(self, **args):
        # at current stage, each call deals one unit.
        if self.loop_iter > len(self.world.unit) - 1:
            self.loop_iter = 0
            self.cur_round += 1
            print(Fore.GREEN + " " * 6 + f"Round {self.cur_round}" + Style.RESET_ALL)

        cur_unit = self.world.unit[self.loop_iter]
        self.loop_iter += 1

        #the result of one unit's action. May need to handle if unit required
        action_result = recv_cmd_by_search(
            cur_unit,
            self.world,
            self.deal_unit(cur_unit, self.world),
            args['view'])
        if action_result is not None:
            if action_result=="Raise Biohazard Level":
                pass
            elif action_result=="Change weather to DaHuangXingYun":
                pass
        return action_result

    def set(self, **args):
        if "deal_unit" in args:
            self.deal_unit = args["deal_unit"]
        return self

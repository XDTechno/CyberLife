from core import constant
from core.constant import FOOD,Gofor,move_cmd,Pacman
from core.world.world import World
def choose_direction(dx, dy):
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

def foodfn(u,w:World,a,v):
    (px,py,_)=w.closest_map((u.pos_x,u.pos_y),FOOD)
    return ("repeat",choose_direction(px,py))
def pacmanfn(u,w,a,v):
    (px,py,_)=w.closest_unit((u.pos_x,u.pos_y),lambda i:i is not u)
    return ("repeat",choose_direction(px,py))
goforfood=[
    [Gofor,FOOD],
    foodfn
]
goforpacman=[
    [Gofor,Pacman],
    pacmanfn
]
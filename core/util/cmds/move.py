from core import constant
from core.constant import move_cmd,move_direction
def check(i):
    try:
        if i in move_cmd:
            return (True,0)
        return (False,0)
    except:
        print(f"check i error:{i}")
        return (False,0)
def dofn(u,w,a,v):
    dx, dy = move_direction[a]
    npx, npy = (u.pos_x + dx, u.pos_y + dy)
    if w[npx,npy]:
        w[u.pos_x,u.pos_y].remove(u)
        u.pos_x,u.pos_y=npx,npy
        w[u.pos_x,u.pos_y].append(u)
    else :return None
move_cmdd=[
    check,
    dofn
]
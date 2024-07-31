from core import constant
def dofn(u,w,a,v):
    (uidx,_)=w.closest_unit((u.pos_x,u.pos_y),lambda i:i is not u)
    w.unit.pop(uidx)
kill=[
    [constant.Kill],
    dofn
        
]
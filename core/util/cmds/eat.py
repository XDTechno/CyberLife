from core import constant
def doSomething(u,w,v):
    w[u.pos_x,u.pos_y].remove(constant.FOOD)
    v.send("ated")
eat = [[constant.Eat],lambda u,w,a,v:doSomething(u,w,v)]
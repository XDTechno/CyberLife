from ..world.world import World
"""
manage the time process
"""
class Scheduler:
    world:World
    cur_round:int=0
    #the index of current entity being handled
    loop_iter:int=0
    #function used to handle the unit
    #deal_unit=lambda _ :"yep"
    def next(self):
        if self.loop_iter > len(self.world.unit)-1:
            self.loop_iter=0
        res= self.world.unit[self.loop_iter]
        self.loop_iter+=1
        return self.deal_unit(res)
        
    def __init__(self):
        self.deal_unit=lambda _:"yep"
    def new_with_world(wld:World):
        res=Scheduler()
        res.world=  wld
        return res
    #chain set
    def set(self,**args):
        if("deal_unit" in args):self.deal_unit=args['deal_unit']
        return self
from ..world.world import World
from ..constant import move_cmd,move_direction
from colorama import Fore,Style
def default_dealer(du,wld):
    if hasattr( du,"act"):
        return du.act(du,wld)
    else :return "yep"
"""
manage the time process
"""
class Scheduler:
    world:World
    cur_round:int=0

    #the index of current entity being handled
    loop_iter:int=0


    def __init__(self):
        #function used to handle the unit
        self.deal_unit=default_dealer
    def next(self):
        #at current stage, each call deals one unit. 
        if self.loop_iter > len(self.world.unit)-1:
            self.loop_iter=0
            self.cur_round+=1
            print(Fore.GREEN+" "*6+f"Next turn:{self.cur_round}"+Style.RESET_ALL)
            
        cur_unit= self.world.unit[self.loop_iter]
        self.loop_iter+=1
        res=None
        
        res=self.deal_unit(cur_unit,self.world)
        
        if res=="yep":return None
        print(f"  result from {cur_unit.id}:"+str(res))
        if(res in move_cmd):
            dx,dy=move_direction[move_cmd[res]]
            (npx,npy)=(cur_unit.pos_x+dx,cur_unit.pos_y+dy)
            if True:
                (cur_unit.pos_x,cur_unit.pos_y)=(npx,npy)
                print(f"    {cur_unit.id} now at {cur_unit.pos_x},{cur_unit.pos_y}")
            
        

    def new_with_world(wld:World):
        res=Scheduler()
        res.world=  wld
        return res
    #chain set
    def set(self,**args):
        if("deal_unit" in args):self.deal_unit=args['deal_unit']
        return self
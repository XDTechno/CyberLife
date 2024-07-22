from ..world.world import World
"""
actually the game starts here.
"""
class Scheduler:
    world:World
    cur_round:int
    #the index of current entity being handled
    loop_iter:int
    def next(self):
        self.world.map.entity[self.loop_iter].next(...)
        pass
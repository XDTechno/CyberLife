from core.entity.entity import Entity
from core.world.world import World
from core.util.scheduler import Scheduler
from view.base_view import View
def launch():
    scheduler=Scheduler()
    view=View()
    view.title="Pacman"
    view.on_message(lambda:print("some bastard sent something..."))
    while(False):
        scheduler.next()
        view.update_map()
        view.send("tickle~")
if __name__=="__main__":
    launch()
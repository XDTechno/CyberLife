import time, random, threading
from colorama import Back, Style

from core.world.world import World


def test_message(d):
    count = 0
    while True:
        time.sleep(random.uniform(4, 20))
        d.recv("nihao" + str(count))
        count += 1


# lowest level View output in the console. A base class.
class View:
    mapdata: World
    entitydata: ...
    handle_message: ...
    _title:str
    @property 
    def title(self):
        return self._title
    @title.setter
    def title(self,v):
        self._title=v

    def update_map(self, map):
        # yep, asynchorus.
        self.mapdata = map
        pass

    def send(self, str):
        # simulator -> UI
        # maybe reply the result to simulator?
        print(Back.GREEN + f" View {self.title or ''} " + Style.RESET_ALL + "from model:" + str)
        # return None

    def recv(self, str):
        # UI -> simulator
        # maybe reply the result to UI?
        if hasattr(self, "handle_message") and self.handle_message(str) == False:
            print(f"Requested <{str}> but handler returned False")
            return False
        if str == "map":
            return self.mapdata

    def on_message(self, fn):
        # set handler for receiving messages from UI
        self.handle_message = fn
        pass

    def __init__(self):
        # here starts another thread to mock the message from UI.
        mock_thread = threading.Thread(target=lambda: test_message(self))
        mock_thread.start()
#And the view should be used as below?
#view=View()
#view.on_message(lambda info:print("oh info is "+str(info)))
#if(view.send('some requery')=="Some Token"):
#   scheduler.someactions()
##at UI's part
#res =view.recv("Ligea is not fat") #=>oh info is Ligea is not fat
#if(res===1):
#   UI.prompt("Ligea is truly not fat")#pop up a window or else

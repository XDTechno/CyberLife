import threading
import time

def test_message(d):
    import random
    count=0
    while True:
        time.sleep(random.uniform(1, 10))
        d.recv("nihao")
class View:
    mapdata:...
    entitydata:...
    listener:...
    def update_map(self,map):
        self.mapdata=map
        pass
    def send(self,str):
        print("[View]from model:"+str)
        pass
    def recv(self,str):
        if(str.startswith("@")):
            return self.reply(str)
        self.listener(str)
    def reply(str):
        #reply request from client or somewhere
        pass
    def on_message(self,fn):
        self.listener=fn
        pass
    def __init__(self):
        
        thread = threading.Thread(target=lambda:test_message(self))
        thread.start()
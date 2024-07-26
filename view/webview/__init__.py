from ..base_view import View
from .server import launch as mount_server
from typing import override
class WV(View):
    server:...
    fps:10
    handle_message:...
    message_cache:list=...
    def __init__(self):
        
        self.server=mount_server(self)
        self.message_cache=[]
        
    def send(self,str):
        self.message_cache.append(str)
        
    def recv(self,str):
        print("[WV server]"+str)
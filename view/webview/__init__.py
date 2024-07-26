from ..base_view import View
from .server import launch as mount_server
from typing import override
class WV(View):
    server:...
    fps:10
    handle_message:...
    def __init__(self):
        mount_server(self)
        
    def send(self,str):
        print("[WV]"+str)
        
    def recv(self,str):
        print("[WV server]"+str)
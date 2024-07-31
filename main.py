#!/usr/bin/env python
# coding=utf-8
from variant.pacman.main import launch
from view.base_view import View
from view.tui_view import TuiView
from view.webview import WV
if __name__ == "__main__":
<<<<<<< HEAD
    # launch(View())
    launch(TuiView(), 10)
    # launch(WV())
=======
    #launch(View())
    #launch(TuiView())
    launch(WV())
>>>>>>> webview
    pass
#new recv_cmd defined in recv_f.py
import core.constant as constant
from core.util.recv_f import recv_cmd
recv_cmd((),(),[constant.HELLO,234,2243324],())
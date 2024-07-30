#!/usr/bin/env python
# coding=utf-8
from variant.pacman.main import launch
from view.base_view import View
from view.tui_view import TuiView
from view.webview import  WV
if __name__ == "__main__":
    #launch(View())
    #launch(TuiView())
    #launch(WV())
    pass
#new recv_cmd defined in recv_f.py
import core.constant as constant
from core.util.recv_f import recv_cmd
recv_cmd((),(),[constant.Gofor,234,2243324],())
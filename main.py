#!/usr/bin/env python
# coding=utf-8
from variant.pacman.main import launch
from view.base_view import View
from view.tui_view import TuiView

if __name__ == "__main__":
    #launch(View())
    #launch(TuiView())
    pass
    
from view.webview import  WV
launch(WV())
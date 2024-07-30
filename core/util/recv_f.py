from ..entity.unit import Unit
from ..world.world import World
from view.base_view import View
from .. import constant
from typing import List,Tuple,Union,Callable
type single = List[Tuple[Union[int],Callable]]
type singleCallable=Callable[[Unit,World,List,View],any]
groups:list[single]=[
    [[constant.HELLO],lambda _1,_2,args,_3:print(args)],
    
]
def check_single_item(cmd,cont):
    if(callable(cont)):return cont(cmd)
    max_idx=0
    for idx,item in enumerate(cont):
        if(cmd[idx]!=item):
            return False
        max_idx=idx+1 #idx will drop after for statement closed
        
    return True,max_idx
def recv_cmd(u:Unit,wld:World,cmd,view:View):
    global groups
    if not isinstance (cmd,list):
        cmd=[cmd]
    
    for item in groups:
        res = check_single_item(cmd,item[0])
        if res[0]== True:
            return item[1](u,wld,cmd[res[1]:],view)
    return None
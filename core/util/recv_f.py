from ..entity.unit import Unit
from ..world.world import World
from view.base_view import View
from .. import constant
from typing import List,Tuple,Union,Callable
type single = List[Tuple[Union[int],Callable]]
type singleCallable=Callable[[Unit,World,List,View],any]
from .cmds.eat import eat
from .cmds.move import move_cmdd
from .cmds.kill import kill
from  .cmds .gofor import goforfood,goforpacman
groups:list[single]=[
    [[constant.HELLO],lambda _1,_2,args,_3:print(args)],
    [['yep'],lambda _1,_2,_3,_4:None],
    eat,move_cmdd,kill,goforpacman,goforfood
]

def check_single_item(cmd,cont):
    if(callable(cont)):return cont(cmd)
    max_idx=0
    for idx,item in enumerate(cont):
        if(cmd[idx]!=item):
            return False,max_idx
        max_idx=idx+1 #idx will drop after for statement closed
    return True,max_idx
def recv_cmd(u:Unit,wld:World,cmd,view:View):
    global groups
    if not isinstance (cmd,list):
        cmd=[cmd]
    
    for item in groups:
        valid = check_single_item(cmd,item[0])
        if isinstance(valid,bool) and valid== False :
            continue
        elif isinstance(valid,list) and valid[0]==False:
            continue
        
        idx=valid[1] if isinstance(valid,list) else 0
        res = item[1](u,wld,cmd[idx:],view)
        if res == None :return None
        if res[0] == 'repeat':
            return recv_cmd(u,wld,res[1:],view=view)
        else :return valid

    return None
from ..entity.unit import Unit
from ..world.world import World
from view.base_view import View
from .. import constant
from typing import List,Tuple,Union,Callable
type single = List[Tuple[Union[int],Callable]]
type rule=Callable[[Unit,World,List,View],any]
from .cmds.eat import eat
from .cmds.move import move_cmdd
from .cmds.kill import kill
from .cmds .gofor import goforfood,goforpacman
rules:list[single]=[
    [[constant.HELLO],lambda _1,_2,args,_3:print(args)],
    [['yep'],lambda _1,_2,_3,_4:None],
    eat,move_cmdd,kill,goforpacman,goforfood
]

def check_single_rule(cmd,condition)->Tuple[bool,int]:
    #if condition is a callable,use it to check cmd directly
    if(callable(condition)):return condition(cmd)
    #record ,used to decide arguments
    max_idx=0
    #check one by one,by condition not cmd
    for idx,item in enumerate(condition):
        if(cmd[idx]!=item):
            return False,max_idx
        max_idx=idx+1 #idx will drop after for statement closed
    return True,max_idx
def recv_cmd(u:Unit,wld:World,cmd,view:View):
    global rules
    #reassemble command to list
    if isinstance(cmd,tuple):
        cmd=list(cmd)
    if not isinstance (cmd,list):
        cmd=[cmd]
    
    for cur_rule in rules:
        #search each rule and execute
        condition=cur_rule[0]
        valid = check_single_rule(cmd,condition)
        if  valid[0]== False :
            continue
        
        idx=valid[1]
        #slice the rest of cmd as arguments passed to fnbody
        arguments=cmd[idx:]
        fnbody=cur_rule[1]
        rule_result = fnbody(u,wld,arguments,view)
        #some cmd need to execute other cmds.
        if rule_result[0] == 'jmp':
            next_cmd=rule_result[1:]
            return recv_cmd(u,wld,next_cmd,view=view)
        else :return rule_result

    return None
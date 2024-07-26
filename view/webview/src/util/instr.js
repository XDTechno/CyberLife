import { logerror, logsuccess } from "./notyf";

function arr(arrr) {
    let ret = {}
    for (let i in arrr) {
        ret[arrr[i]] = i
    }
    return ret;
}
export const instr = arr([
    "move",
    "left",
    "right",
    "up","near",
    "down","attack",
    "turnstart",
    "rejected"
])
export function dir(_dir) {
    return { dx: _dir === instr.left ? -1 : _dir === instr.right ? 1 : 0,
         dy: _dir === instr.up ? -1 : _dir === instr.down ? 1 : 0,flip(){
            this.dx=-this.dx;
            this.dy=-this.dy;
            return this;
         } }
}
export function toDir(dx, dy) {
   // console.log("toDir",dx,dy)
    if(dx==undefined||dy==undefined){
        logerror("No, wrong dir")
    }
    if(Math.abs(dx)>Math.abs(dy)){
        if(dx>0){
            return instr.right
        }else{
            return instr.left
        }
    }else{
        if(dy>0){
            return instr.down
        }else{
            return instr.up
        }
    }

    return null
}
export function instrname(number){

    return Object.keys(instr)[number]

}
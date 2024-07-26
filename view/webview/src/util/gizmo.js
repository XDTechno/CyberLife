import { instr, dir } from "./instr";
import { logsuccess } from "./notyf";
export class Unit {
    constructor(x = 8, y = 8) {
        this.name = Math.floor(Math.random() * 1000)
        this.x = Math.ceil(Math.random() * x)
        this.y = Math.ceil(Math.random() * y)
        this.HP=Math.random()*4+8
    }
    name;
    x; y;
    HP=10;
    action(handle, rec, other) {
        if (handle === instr.turnstart) {
            return [instr.move,instr.near,
                     instr[
                        ["left", "right", "up", "down"][Math.floor(Math.random() * 4)]]]
        } else if (handle === instr.move) {
            this.x+=dir(rec).dx
            this.y+=dir(rec).dy
        } else if (handle === instr.rejected) {
           
            return [instr.attack, instr.near]
        }
    }
    can_pass=false;
}
export class Block {
    r;
    g;
    b;
    can_pass = false
}
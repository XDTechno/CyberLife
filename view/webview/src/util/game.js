import Tilemap from "./tilemap";
import { Unit } from "./gizmo";
import { instr, dir, toDir, instrname } from "./instr";
import { logsuccess } from "./notyf";

export function game(x, y) {
    return {
        base: new Tilemap(x, y, () => Math.random() > 0.5 ? 1 : 0),
        instant_map: null,
        units: [],
        init() {
            this.units = [new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y), new Unit(x,y)]
            this.base = new Tilemap(x, y)
            this.base.row(1).forEach(i => i.push({ can_pass: false }))
            this.base.row(y).forEach(i => i.push({ can_pass: false }))
            this.base.column(1).forEach(i => i.push({ can_pass: false }))
            this.base.column(x).forEach(i => i.push({ can_pass: false }))
            this.instant_map = this.draw_map();
        }, tick() {
            this.units.forEach(u => {
                let n = u.action(instr.turnstart)
                if (n[0] === instr.move) {
                    let wt;
                    if (n[1] == instr.near) {
                        let nu=this._closest_unit(u.x,u.y)
                        wt = dir(toDir(u.x-nu[0],u.y-nu[1])).flip()
                    }
                    else {
                        wt = dir(n[1])
                    }
                    //
                    let pass = !this._blocked(u.x + wt.dx, u.y + wt.dy)
                    if (pass) {
                        u.x += wt.dx
                        u.y += wt.dy
                    }
                    else {
                        let res = u.action(instr.rejected, instr.move, n[1])
                        if (res[0] === instr.attack) {
                            let [n, m] = [u.x, u.y];

                            if (res[1] != instr.near) {
                                n += dir(res[1]).dx
                                m += dir(res[1]).dy
                            } else {
                                let ddd = this._closest_unit(n, m)
                                let dddd = dir(toDir(ddd[0], ddd[1]))
                                n += dddd.dx
                                m += dddd.dy
                            }

                            let o = this?.instant_map?.get(n, m)?.findLast?.(i => i?.HP)
                            if (o) {
                                o.HP-=4;
                                logsuccess("attack"+`${u.name} attack ${o.name} ${o.HP}`)
                            }
                        }
                    }
                }
            })

            this.units = this.units.filter(i => (i?.HP ?? 0) > 0)
            console.log(this.units.length)
        }, _deal(n) {

        },
        draw_map() {
            this.tick();
            let ret = new Tilemap(x, y)

            for (let { value, x, y } of this.base.each_with_ord()) {
                ret.get(x, y).push(value.top)
            }

            this.units.forEach(u => {
                ret.get(u.x, u.y)?.push?.(u)
            })

            this.instant_map = ret

            return ret;
        },
        _blocked(x, y) {
            let item = this.instant_map?.get?.(x, y)
            if (item == null) return true;
            return !item.can_pass?.()
        },
        _closest_unit(x, y) {
            let gap = Infinity, theunit = null;
            let posx = Infinity;
            let posy = Infinity;

            for (let i of this.instant_map?.each_with_ord() ?? []) {
                if (i.value.has_prota()) {

                    let new_r = i.value.findLast(i => i.HP > 0);
                    if (new_r) {
                        let d = Math.abs(x - new_r.x) + Math.abs(y - new_r.y)
                        if (d < gap && d >= 1) {
                            gap = d
                            posx = i.x
                            posy = i.y
                            theunit = new_r
                        }
                    }

                }
            }
            return [posx, posy, theunit]
        }
    }
}
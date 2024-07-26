import Tile from './tile.js'
export default class Tilemap extends Array {
    constructor(x_size, y_size, fillfn = _ => 0) {
        super(x_size);
        for (let i = 0; i < x_size; i++) {
            this[i] = [];
            for (let j = 0; j < y_size; j++) {
                this[i][j] = new Tile(fillfn(i, j, x_size, y_size))
            }
        }
    }
    get(x, y) {
        return this[x - 1]?.[y - 1] ?? null
    }
    column(x) {
        return this._setProto(this[x - 1])
    }
    row(y) {
        return this._setProto(this.map(x => x[y - 1]))
    }
    _setProto(n) {
        Object.setPrototypeOf(n, Tilemap.prototype);
        return n;
    }
    *each() {
        for (let i = 0; i < this.length; i++) {
            for (let j = 0; j < this[i].length; j++) {
                yield this[i][j]
            }
        }
    }
    *each_with_ord() {
  
            for (let i = 0; i < this.length; i++) {
                for (let j = 0; j < this[i].length; j++) {
                   
                yield { value: this[i][j], x: i + 1, y: j + 1 }
                
            }
        }
    }
}
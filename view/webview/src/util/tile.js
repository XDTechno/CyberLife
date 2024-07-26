export default class Tile extends Array{
    get top(){
        return this[this.length-1]??null
    }
    constructor(n){
        super();
        Object.assign(this,n)
    }
    has_prota(){
        return this.some(i=>i?.name&&i.HP>=0)
    }
    can_pass(){
        return this.every(i=>i?.can_pass??true)
    }
}
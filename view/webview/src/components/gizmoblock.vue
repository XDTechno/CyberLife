<script setup>
import { ref, onMounted } from "vue";
let props = defineProps(['x', 'y', 'value','units']);
//gizmo is the block
function hasfood(n){
    return n.filter(i=>i==1919).length
}
function hasunit(x,y,unitlist){
    for(let u of unitlist){
        if(u.pos_x==x&&u.pos_y==y)return true
    }
}
</script>
<template>
    <div :title="`(${props.x},${props.y})`" class="tile">
        <slot>{{hasunit(props.x,props.y,props.units)?"@":" " }} </slot>

        <div class="foods">

      <div class="food_token" v-for="_ in hasfood(props.value)"></div>
        </div>
    </div>
</template>
<style scoped>
.tile {
    width: 50px;
    height: 50px;
    background-color: #ccc;
    border: 3px solid #999;
    box-sizing: border-box;
    position:relative;
    display: flex;
    justify-content: center;
    align-items: center;
    color: azure;
}

.tile_block {
    border-color: #000000;
    background-color: #454545;
}
.foods{
    position:absolute;
    bottom:0px;
    left:0px;
    flex-direction: row;
    display: flex;
  justify-content: flex-start;
  align-items: flex-end;
}
.food_token{
    width:4px;
    height:4px;
    background-color: rgb(255, 100, 100);
    border:1px white solid;
}
</style>
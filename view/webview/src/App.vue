<script setup>
import { ref ,onMounted} from 'vue';
import tilemap from './util/tilemap';
import gizmoblock from './components/gizmoblock.vue';

const size=20
const tm=ref(new tilemap(size,size,()=>Math.random()>0.5?1:0))
window.tm=tm;

import { game as Game } from './util/game';
const game=ref(Game(size,size))
onMounted(()=>{
  game.value.init()
  setInterval(()=>atclick(),2000)})

const atclick=()=>{
  tm.value=game.value.draw_map()
}
</script>

<template>
<div class="tilemap" v-for="i in tm[0].length" @click="atclick">

  <gizmoblock 
    v-for="j in tm.length" 
    :x="i" :y="j" :gizmo="tm.get(j,i)"
  />
</div>
</template>

<style scoped>
.tilemap {
      display: flex;
      flex-wrap: wrap;
    }
</style>

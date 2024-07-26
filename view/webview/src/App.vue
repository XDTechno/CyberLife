<script setup>
import { ref ,onMounted} from 'vue';
import gizmoblock from './components/gizmoblock.vue';

const tm=ref([])
const units=ref([])
setInterval(()=>{
  req("map").then(i=>{
    tm.value=i.map;
    units.value=i.unit})
},1000)
</script>

<template>
  alive units:{{ units.length }}
<div class="tileline" v-for="(row,ri) in tm">
  
  <gizmoblock v-for="(cell,ci) in row" :y="ri" :x="ci" :value="cell" :units="units"></gizmoblock>
</div>
</template>

<style scoped>
.tileline {
      display: flex;
      flex-wrap: wrap;
    }
</style>

<script setup>
import { ref, onMounted } from "vue";
let props = defineProps(['x', 'y', 'gizmo']);
//gizmo is the block
</script>
<template>
    <div :title="`(${props.x},${props.y})`" :class="{ tile_block: gizmo.can_pass(), tile: true }">
        <slot>{{ gizmo.has_prota() ? "@" : " " }} </slot>
    </div>
</template>
<style scoped>
.tile {
    width: 30px;
    height: 30px;
    background-color: #ccc;
    border: 3px solid #999;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
    color: azure;
}

.tile_block {
    border-color: #000000;
    background-color: #454545;
}
</style>
Math.randi=(n)=>Math.floor(Math.random()*n)
import { createApp } from 'vue'
import './style.css'
import 'notyf/notyf.min.css';
import App from './App.vue'
import tile from './util/tile'
import tilemap from './util/tilemap'
createApp(App).mount('#app')

window.tile=tile;
window.tilemap=tilemap
import { instr } from './util/instr'
window.instr=instr

fetch('http://localhost:8008/fps').then(res=>res.json()).then(
    i=>{console.log(i)}
)
fetch('http://localhost:8008/map').then(res=>res.json()).then(
    i=>{console.log(i)}
)
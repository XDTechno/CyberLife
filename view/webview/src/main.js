Math.randi=(n)=>Math.floor(Math.random()*n)
import { createApp } from 'vue'
import './style.css'
import 'notyf/notyf.min.css';

import App from './App.vue'

window.req=function(path){
    const res =fetch("http://localhost:8008/" + path);
    res.catch(reason=>{
        if(reason instanceof TypeError){}else        
        console.log("Nooo,request rejected:"+reason)})
    return  res.then(res=>res.json()).catch(j=>console.log("parsing json failed"));
}
createApp(App).mount('#app')
import { Notyf } from 'notyf'
let notyf=new Notyf()
setInterval(() => {
    req("message").then(i=>{
        i.forEach(msg=>notyf.success(msg))
    })
}, 60);
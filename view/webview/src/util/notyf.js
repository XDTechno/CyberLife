import { Notyf } from 'notyf'
let notyf=new Notyf()
export function logsuccess(msg){
    notyf.success(msg)
}
export function logerror(msg){
    notyf.error(msg)
}
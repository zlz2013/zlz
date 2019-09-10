//获取元素
function $(tag,index){
    var elems
    if(index){
        elems=document.getElementsByTagName(tag)[index]
    }else{
        elems=document.getElementsByTagName(tag)[0]
    }

    return elems
}
$("h1",2)
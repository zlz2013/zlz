function createXhr(){
         //根据不同的浏览器创建不同的异步(XHR)对象
        var xhr=null;
        if(window.XMLHttpRequest){
            xhr=new XMLHttpRequest();

        }else{
            xhr=new ActiveXObject('Microsoft.XMLHTTP');

        }
        return xhr;
        }

        /*
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4 && xhr.status==200){
                console.log(xhr.responseText);
            }
        }
        */
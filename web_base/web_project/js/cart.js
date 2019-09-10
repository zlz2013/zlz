$(function(){
            /*全选和去选全选*/
            var isChecked=false
            $(".checkAll").click(function(){
                //自定义标签属性或属性值
                /*$(this).prop('a','b').attr('aa','bb')
                console.log($(this).prop('a'))
                var value=$(this).prop("checked")
                console.log(value)
                $(".checkItem").prop("checked",value)*/
                isChecked=!isChecked
                if(isChecked){
                    $(".checkAll").attr("src","../images/cart/product_true.png")
                    $(".checkItem").attr("src","../images/cart/product_true.png")
                    .attr("checked",true)
                }else{
                    $(".checkAll").attr("src","../images/cart/product_normal.png")
                    $(".checkItem").attr("src","../images/cart/product_normal.png")
                    .attr("checked",false)
                }
                sum()
            })
            $(".checkItem").click(function(){
                //按钮自身状态及样式的修改
                //如果存在checked属性，说明当前是选中，需要修改为未选中
                if($(this).attr("checked")){
                    //移除标记
                    //修改标记的同时，修改显示图片
                    $(this).attr("checked",false)
                    .attr("src","../images/cart/product_normal.png")
                }else{
                    $(this).attr("checked",true)
                    .attr("src","../images/cart/product_true.png")
                }
                sum()
            })
            /*2.反选
                被选中的商品数量等于商品按钮的数量。视为全选
                未被选中的商品数量为0，视为全选
            */
            //方式二 未被选中的商品数量为0
            /*
            $(".checkItem").click(function(){
                //获取被选中的商品数量
                //伪类:checked表示按钮的选中状态
                //console.log($(".checkItem[checked=checked]").length)
                //否定筛选 not()

                var len=$(".checkItem").not(".checkItem[checked=checked]").length
                console.log(len)
                if(len==0){
                    $(".checkAll").attr("src","../images/cart/product_true.png")
                    isChecked=true
                }else{
                    $(".checkAll").attr("src","../images/cart/product_normal.png")
                    isChecked=false
                }
            })
            */

             $(".checkItem").click(function(){
                //获取被选中的商品数量
                //伪类:checked表示按钮的选中状态
                //console.log($(".checkItem[checked=checked]").length)
                //否定筛选 not()

                var len=$(".checkItem[checked=checked]").length
               // console.log(len)
               // console.log($(".checkItem").length)
                if(len==$(".checkItem").length){
                    $(".checkAll").attr("src","../images/cart/product_true.png")
                    isChecked=true
                }else{
                    $(".checkAll").attr("src","../images/cart/product_normal.png")
                    isChecked=false
                }

                //工具栏联动
                sum()
            })


             //3.数量增减
             $(".add").click(function(){
                //获取输入框的值
                var value=$(this).prev().val()
                value++
                $(this).prev().val(value)
                //价格联动
                //获取单价
                var s1=$(this).parent().prev().find("p").html()
                var s2=$(this).parents(".item").find(".price p").html()
                var price=s1.substring(1)   //299
                var tolPrice=price*value
                tolPrice=tolPrice.toFixed(2)
                console.log(s1,s2,tolPrice)

                //显示总金额
                $(this).parents(".item").find(".sum").html("¥"+tolPrice)
                sum()
             })
             $(".minus").click(function(){
                var value=$(this).next().val()
                if(value>1){
                    value--
                }
                $(this).next().val(value)
                //价格联动函数
                changeSum($(this),value)
                sum()
             })


             //4.价格联动
             function changeSum(that,value){
                 //价格联动
                //获取单价
                var s1=that.parent().prev().find("p").html()
                var s2=that.parents(".item").find(".price p").html()
                var price=s1.substring(1)   //299
                var tolPrice=price*value
                tolPrice=tolPrice.toFixed(2)
                console.log(s1,s2,tolPrice)

                //显示总金额
                that.parents(".item").find(".sum").html("¥"+tolPrice)

             }

             //5.移除商品
             $(".item .action").click(function(){
                $(this).parent().remove()
                sum()
             })

             //6.获取总数量和总价格
             function sum(){
                //获取被选中的商品的总数量和总金额进行累加
                var num=0
                var price=0
                $(".checkItem[checked=checked]").each(function(){
                    num+=Number($(this).parents(".item")
                    .find(".count input").val())
                    var str=$(this).parents(".item")
                    .find(".sum").html()
                    var s=Number(str.substring(1))
                    price+=s
                })
                //修改显示
                $(".total_count").html(num)
                price=price.toFixed(2)
                $(".total_price").html(price)
             }

        })
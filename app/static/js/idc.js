
/* 编辑机房信息模态框*/

$(".update").on('click',function(){
    $('#updateIdcModal').modal('show')  
    })


// 点击编辑按钮，获取id，从逻辑端查出对应的数据，弹出模态窗渲染数据
$(".update").click(function(){   
    var id=$(this).attr("data-id")
    $.getJSON("/idcupdate",{'id':id},function(data){
            console.log(data);
            idc = data['msg']
            $("#updateid").val(idc["id"]);
            $("#updatename").val(idc["name"]);
            $("#updatename_cn").val(idc["name_cn"]);
            $("#updatephone").val(idc["phone"]);
            $("#updateaddress").val(idc["address"]);
            $("#updateadminer").val(idc["adminer"]);
            $('#updateModal').modal('show')
        })
})

// 更新机房信息数据
$("#updateIdcbtn").click(function(){
$.post("/idcupdate",$("#updateidcForm").serialize(),function(data) {
    data=JSON.parse(data)
    if(data["code"]==0){
        swal({
                title:"success",
                text:"更新成功",
                type:"success",
                confirmButtonText:'确定'
                },function(){
                    location.reload()
                })

    }else{
        alert("update error")
    }
    })
    return false;
})



/* 添加机房模态框*/

$("#addidc").on('click',function(){
    $('#IdcModal').modal('show')  
    })


/* 添加机房*/
$("#Idcbtn").click(function(){
	$.post("/idcadd",$("#idcForm").serialize(),function(data){
	    console.log(data)
	    data=JSON.parse(data);
	    if(data["code"] == 0){
		swal({
		    title:'Congratulation',
		    text:data['result'],
		    type:'success',
		    confirmButtonText:'确定'
		    },function(){
			location.href='/idc'
		    })
	    }else{
		swal('Error',data['errmsg'],'error')
	    }
	})
    return false
})

/* 取消模态框*/
$('#cancel_button').click(function(){
    location.href='/idc'
})



/* 删除机房*/
$('.del').click(function(){
    var id=$(this).attr('data-id')
    var str="id="+id
    $.post('/idcdelete',str,function(data){
        data=JSON.parse(data);
	    if(data["code"] == 0){
		swal({
		    title:'删除成功',
		    text:data['result'],
		    type:'success',
		    confirmButtonText:'Cool'
		    },function(){
			     location.reload()
		    })
	 }else{
	    	swal('Error',data['errmsg'],'error')
	}
   })
    return false
})
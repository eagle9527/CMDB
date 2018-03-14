/* 添加机柜模态框 */
$("#cabinetadd").on('click',function(){
    $('#AddcabinetModal').modal('show')  
})

/*获取机房列表*/
$(".update").click(function(){   
    $.getJSON("/cabinetadd",function(data){
            console.log(data);
            var selectdom= $("#id_idc");
            selectdata = (data['msg']);
            selectdom.empty()
            for (var i=0;i<selectdata.length;i++)
            {
                selectdom.append("<option value="  + selectdata[i]['id'] + ">"  + selectdata[i]['name'] +  "</option>");
            }

            
        })
        return false
})


/* 添加机柜*/
$("#cabinetbtn").click(function(){
    $.post("/cabinetadd",$("#cabinetForm").serialize(),function(data){
        console.log(data)
        data=JSON.parse(data);
        if(data["code"] == 0){
        swal({
            title:'Congratulation',
            text:data['result'],
            type:'success',
            confirmButtonText:'确定'
            },function(){
            location.href='/cabinet'
            })
        }else{
        swal('Error',data['errmsg'],'error')
        }
    })
    return false
})


/* 修改机柜信息模态框 */

$(".cabinetupdate").on('click',function(){
    $('#updatecabinetModal').modal('show')  
})

/*点击编辑按钮，获取id，从逻辑端查出对应的数据，弹出模态窗渲染数据*/

$(".cabinetupdate").click(function(){                                                                                                 
    var id=$(this).attr("data-id")
    $.getJSON("/cabinetupdate",{'id':id},function(data){
            console.log(data)
            cabinet  = data['cabinet']
    /*填充idc列表*/
            selectdom= $("#updateid_idc");
            selectdata = (data['idc']);
            selectdom.empty()
            for (var i=0;i<selectdata.length;i++)
            {
                     console.log(selectdata[i]['id'])
                     console.log(cabinet["idc_id"])
                if (selectdata[i]['id'] == cabinet["idc_id"])
                    {

                    selectdom.append("<option value='"  + selectdata[i]['id'] + "' selected>"  + selectdata[i]['name'] +  "</option>");
                    }
                else
                  {
                    selectdom.append("<option value="  + selectdata[i]['id'] + ">"  + selectdata[i]['name'] +  "</option>");
                    }
        
            }
   /*填充机柜数据*/
           $("#updateid").val(cabinet["id"]);
           $("#updatename").val(cabinet["name"]);
           $("#updateu_num").val(cabinet["u_num"]);
           $("#updatepower").val(cabinet["power"]);
           $('#updatecabinetModal').modal('show')

            })
           

       return false
})

/*更新机柜信息*/
$("#updatecabinetbtn").click(function(){
    $.post("/cabinetupdate",$("#updatecabinetForm").serialize(),function(data){
        console.log(data)
        data=JSON.parse(data);
        if(data["code"] == 0){
        swal({
            title:'Successful',
            text:data['result'],
            type:'success',
            confirmButtonText:'确定'
            },function(){
            location.href='/cabinet'
            })
        }else{
        swal('Error',data['msg'],'error')
        }
    })
    return false
})


/*删除机柜*/
$('.del').click(function(){
    var id=$(this).attr('data-id')
    var str="id="+id
    $.post('/cabinetdelete',str,function(data){
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


/* 添加服务器模态框 */
					$("#serveradd").on('click',function(){
						$('#AddServerModal').modal('show')  
					})


/*获取机房列表 机柜列表*/
			$(".update").click(function(){   
				$.getJSON("/serveradd",function(data){
						console.log(data);
					/* idc 下拉列表填充*/
						var selectdom= $("#id_idc");
						selectdata = (data['idc']);
						selectdom.empty()
						for (var i=0;i<selectdata.length;i++)
						{
							selectdom.append("<option value="  + selectdata[i]['id'] + ">"  + selectdata[i]['name'] +  "</option>");
						}
					/* 机柜 下拉列表填充*/
						var servselect= $("#id_cabinet");
						serverdata = (data['cabinet']);
						servselect.empty()
						for (var k=0;k<serverdata.length;k++)
						{
							servselect.append("<option value="  + serverdata[k]['id'] + ">"  + serverdata[k]['name'] +  "</option>");
						}
						
					})
					
					return false
			})

/*添加服务器*/
			$("#serverbtn").click(function(){
				$.post("/serveradd",$("#serverForm").serialize(),function(data){
					console.log(data)
					data=JSON.parse(data);
					if(data["code"] == 0){
					swal({
						title:'Successful',
						text:data['result'],
						type:'success',
						confirmButtonText:'确定'
						},function(){
						location.href='/server'
						})
					}else{
					swal('Error',data['msg'],'error')
					}
				})
				return false
			})



/* 修改服务器资料模态框 */
			$(".serverupdate").on('click',function(){
				$('#ChangeServerModal').modal('show')  
			})


/*  点击编辑按钮，获取id，从逻辑端查出对应的数据，弹出模态窗渲染数据*/
			$(".serverupdate").click(function(){                                                                                                 
				var id=$(this).attr("data-id")
				$.getJSON("/serverupdate",{'id':id},function(data){
						console.log(data)
                        server  = data['server']
					  /*填充idc列表*/
						selectdom= $("#Changeid_idc");
						selectdata = (data['idc']);
						selectdom.empty()
						for (var i=0;i<selectdata.length;i++)
						{
                                                      if (selectdata[i]['id'] == server["idc"] )
                                                         {
                                                              selectdom.append("<option value='"  + selectdata[i]['id'] + "' selected>"  + selectdata[i]['name'] +  "</option>");
                                                          }
                                                     else {
                                                         selectdom.append("<option value="  + selectdata[i]['id'] + ">"  + selectdata[i]['name'] +  "</option>");
                                                          }
						}
					  /* 机柜 下拉列表填充*/
						var servselect= $("#Changeid_cabinet");
						serverdata = (data['cabinet']);
						servselect.empty()
						for (var k=0;k<serverdata.length;k++)
						{
                                                         if (serverdata[k]['id'] == server["cabinet"] ) 
                                                              {
			                                  				    servselect.append("<option value='"  + serverdata[k]['id'] + "' selected>"  + serverdata[k]['name'] +  "</option>");
                                                               }
                                                         else {
                               
					                                  		    servselect.append("<option value="  + serverdata[k]['id'] + ">"  + serverdata[k]['name'] +  "</option>");
                                                              }
                             
						}
				     
					 /*填充机柜数据*/
						$("#updateid").val(server["id"]);
						$("#Changeid_hostname").val(server["hostname"]);
						$("#Changeid_ip").val(server["ip"]);
						$("#Changeid_mac").val(server["mac"]);
						 $("#Changeid_username").val(server["username"]);
						$("#Changeid_password").val(server["password"]);
						$("#Changeid_port").val(server["port"]);
						$("#Changeid_brand").val(server["brand"]);
						$("#Changeid_cpu").val(server["cpu"]);
						$("#Changeid_memory").val(server["memory"]);
						$("#Changeid_disk").val(server["disk"]);
						$("#Changeid_system_type").val(server["system_type"]);
						$("#Changeid_number").val(server["number"]);
						$("#Changeid_number").val(server["number"]);
						$('#ChangeServerModal').modal('show')

						
						})
					   

				   return false
			})


/*更新服务器资料*/

				$("#changeserverbtn").click(function(){
					$.post("/serverupdate",$("#ChangeserverForm").serialize(),function(data){
						console.log(data)
						data=JSON.parse(data);
						if(data["code"] == 0){
						swal({
							title:'Successful',
							text:data['result'],
							type:'success',
							confirmButtonText:'确定'
							},function(){
							location.href='/server'
							})
						}else{
						swal('Error',data['msg'],'error')
						}
					})
					return false
				})






/*删除服务器*/

				$('.del').click(function(){
					var id=$(this).attr('data-id')
					var str="id="+id
					$.post('/serverdelete',str,function(data){
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

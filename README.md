第11天作业

作业：

       新增功能:   
	               * ansible第三方接口
	               * Bind-DLZ DNS 管理  
				      bind 方面的配置请参阅 https://github.com/1032231418/Bind-Web
	               * 日志可视化			 
				   
				   

1.项目分析：

       1).用户管理
	   
	         *.个人中心
			 
			        * 显示个人信息，以及可以，修改个人信息，及用户密码
				
	         *. 用户列表
			 
			        * 显示所有已添加用户信息，可以对用户进行，增加，删除，修改
			
	   2).资产管理	
	   
             *.机房管理
			 
			        * 显示已添加机房信息，可以对机房信息，进行，增加，删除，修改
			 
	         *.机柜管理
			 
			        * 显示已添加机柜列表，可以对机柜，进行，增加，删除，修改
				 
             *.服务器管理
			 
			        * 显示已添加主机列表，可以对主机，进行，增加，删除，修改				 
	  3).工单系统
	            
             *.工单申请
				
			        * 提交新工单
				
             *.申请列表
				
			        * 显示已提交，未完成工单,可对工单状态，工单信息进行修改
					
             *.历史工单
				
			        * 可以看到，已提交所有工单，可以查看工单详情
				
	  4).第三方接口

             *.批量执行命令
			 
			        * 调用 ansible接口，远程执行命令
					
	  5).域名管理
	     
             *.显示已经添加的域名解析列表,可以对解析记录进行，增加，删除，修改
			 
	  6).日志可视化
	  
             *.网站浏览状态分析  
			 
			        *.查库获取状态码统计数据,返回前端，进行渲染	
					
              *.网站访问IP来源
                   			  
			        *.查库获取各省访问ip统计信息，格式化输出，前端渲染          
	  
2.项目功能分析:

       1).用户管理
	   
	       *.用户登录/退出 
		   
		        函数文件: login.py 
			   
			          login()            获取前端输入账号密码，进行判断是否正确,用户是否锁定
			          loginout()         用户退出
                      
	       *.个人中心
		   
		        函数文件:  user.py
			   
			          center()           用户个人中心，显示已登录用户个人信息
			          chpwdoneself()     修改个人密码
			          chmessageoneself() 修改个人资料
			   
		   *. 用户列表
		       
		        函数文件： userlist.py
				
			          userlist()         用户列表，显示已添加用户列表
			          update()           更新用户信息
			          add()              添加新用户
			          delete()           删除用户
			
	   2).资产管理

             *.机房管理
			     
		        函数文件：idc.py
				      
			          idc()             显示已添加 idc列表
			          idcadd()          添加机房
			          idcupdate()       修改机房信息
			          idcdelete()       删除机房
		
	         *.机柜管理
                  
		        函数文件： cabinet.py
                       
 			          cabinet()         机柜列表，显示已添加机柜信息
			          cabinetadd()      添加新机柜
			          cabinetupdate()   机柜信息修改
			          cabinetdelete()   删除机柜
				 
	         *.服务器管理
         	    
		        函数文件: server.py
				 
 			          server()          显示已添加机服务器列表
 			          serveradd()       添加新服务器
 			          serverupdate()    更新服务器信息
 			          serverdelete()    删除服务器
		                               
	  3).工单系统
	          
		        函数文件：  job.py
            	  
            *.工单申请
			    
 			          jobadd()          添加新工单
				
            *.申请列表
				
 			          joblist()         工单列表
 			          jobupdate()       更新工单信息
 			          jobdetail()       查看工单详情
				     
            *.历史工单
			    
 			          jobhistory() 历史工单列表
				
 				
	  4).第三方接口	

		        函数文件：  ansibles.py  调用 ansible API 文件	  commands.py
				
 			          ansible()         ansible远程执行命令
 			          history()         ansible历史记录	  
                      					  
	  5).域名管理
     	  
		        函数文件：  named.py

 			          namedlist()         已添加域名列表
 			          namedadd()          添加解析记录
 			          namedupdate()       更新接记录
 			          nameddelete()       删除解析记录
                			
	  6).日志可视化
	      
            *.日志状态饼图
			
      			函数文件：  log.py
				
 			          log()             日志页面
 			          status()          日志状态数据

            *.日志来源地图

      			函数文件：  map.py			

 			          map()             地图展示
 			          mapdata()         传输地图数据			
				
	 
<center>3.流程图</center > 

![image](https://github.com/1032231418/python/blob/master/day11/naotu.png)


<center>4.演示 </center > 

		演示地址:  
		
[演示服务器地址](http://120.78.80.49:8080/) http://120.78.80.49:8080/ 账号:  eagle  密码 123456

		

添加用户

![image](https://github.com/1032231418/python/blob/master/day9/adduser.png)

用户详情

![image](https://github.com/1032231418/python/blob/master/day9/userxq.png)


修改用户信息

![image](https://github.com/1032231418/python/blob/master/day9/changeuser.png)


添加服务器

![image](https://github.com/1032231418/python/blob/master/day9/addserver.png)


修改服务器信息

![image](https://github.com/1032231418/python/blob/master/day9/changeserver.png)



域名管理

添加域名解析

![image](https://github.com/1032231418/python/blob/master/day11/zoneadd.png)

修改域名解析

![image](https://github.com/1032231418/python/blob/master/day11/zoneupdate.png)

测试解析记录

![image](https://github.com/1032231418/python/blob/master/day11/zonejx.png)


ansible 远程执行命令

远程执行命令

![image](https://github.com/1032231418/python/blob/master/day11/cmd1.png)

查看命令历史

![image](https://github.com/1032231418/python/blob/master/day11/cmd2.png)

日志状态饼图

![image](https://github.com/1032231418/python/blob/master/day11/bingtu.png)

日志来源地图

![image](https://github.com/1032231418/python/blob/master/day11/map.png)

<center>5.目录结构</center > 

![image](https://github.com/1032231418/python/blob/master/day11/jiegou.png)


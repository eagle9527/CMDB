#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,lists
from . import app
from sessions import sessionmsg
import json
import  sys
from datetime import datetime
from   commands     import   ansiblecommand
server_fields = ['id','hostname']

# ansible 执行命令
@app.route('/ansible',methods=['GET', 'POST'])
def ansible():
        if 'username' not in  session:
            return redirect('/login/')
        msg = sessionmsg()
        if request.method=='GET':
            server  = lists('server',server_fields)
            return render_template('ansible.html',msg=msg,server=server['msg'])

        if request.method=='POST':
            cmdmsg  = {k:v[0] for k,v in dict(request.args).items()}
            #记录日志写入文件
            cmd_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cmd_history = "Time: %s User: %s Host: %s Cmd: %s \n" % (cmd_time,msg['username'],cmdmsg['pattern'],cmdmsg['cmd'])
            with open("/tmp/ansible.log",'a') as ansible_log:
                ansible_log.write(cmd_history)
                ansible_log.close

            ansiblecmd = ansiblecommand(cmdmsg['cmd'],cmdmsg['pattern']) 
            pattern = cmdmsg['pattern']
            result = ansiblecmd['contacted'][pattern]['stdout']
            if  result:
                ansible_cmd = "host: %s | CMD:  %s | success >> \n" % (cmdmsg['pattern'],cmdmsg['cmd'])
                ansible_msg =  ansible_cmd + result
                results = ansible_msg.replace('\n','<br>')
                return json.dumps(results)
#ansible 历史记录
@app.route('/history',methods=['GET', 'POST'])
def  history():
        if 'username' not in  session:
            return redirect('/login/')
        msg = sessionmsg()
        if request.method=='GET':
            ansible_history = ""
            with file("/tmp/ansible.log")  as f:
                for line in reversed(f.readlines()):
                    ansible_history +=line+"</br>"
            f.close 
        return json.dumps(ansible_history)



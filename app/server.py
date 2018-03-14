#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,lists
from . import app
from sessions import sessionmsg
import json

cabinet_fields=['id','name']

idc_fields = ['id','name']

server_field = ['hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number', 'cabinet']
server_fields = ['id','hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number', 'cabinet']

# 主机列表
@app.route('/server',methods=['GET', 'POST'])
def server():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    idcs   =  lists('idc',idc_fields)
    cabinets   = lists('cabinet',cabinet_fields)
    servers  = lists('server',server_fields)

    for cab  in servers['msg']:

        for items in cabinets['msg']:
            if  cab['cabinet'] == items['id']:
                cab['cabinet'] = items['name']

            for cac in idcs['msg']:
                if cab['idc'] == cac['id']:
                    cab['idc'] = cac['name']
    return render_template('server.html',msg=msg,server_list=servers['msg'])

# 添加主机
@app.route('/serveradd',methods=['GET', 'POST'])
def serveradd():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        idc   =  lists('idc',idc_fields)
        cabinet   =  lists('cabinet',cabinet_fields)
        result = {'code':0,'idc':idc['msg'],'cabinet':cabinet['msg']}
        return  json.dumps(result)

    if request.method=='POST':
       server  = {k:v[0] for k,v in dict(request.form).items()}
       result = insert_sql('server',server_field,server)
       if  result['code'] == 0:
           result ={'code':0, 'msg':"success"}
           return  json.dumps(result)

# 更新主机信息
@app.route('/serverupdate',methods=['GET', 'POST'])
def serverupdate():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        id = request.args.get('id')
        data={'id':id}
        server  = getone('server',data,server_fields)
        idc   =  lists('idc',idc_fields)
        cabinet   =  lists('cabinet',cabinet_fields)
        result = {'code':0,'idc':idc['msg'],'cabinet':cabinet['msg'],'server':server['msg']}
        return  json.dumps(result)

    if request.method=='POST':
        server  = {k:v[0] for k,v in dict(request.form).items()} 
        print  server
        result = _update('server',server_fields,server)
        if  result['code'] == 0:
            return  json.dumps(result)
# 删除主机
@app.route('/serverdelete',methods=['GET', 'POST'])
def serverdelete():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='POST':
       server  = {k:v[0] for k,v in dict(request.form).items()}
 
       if _delete('server',server):
           result ={'code':0, 'msg':"delete   success"}
           return  json.dumps(result)


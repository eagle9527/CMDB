#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,lists
from . import app
from sessions import sessionmsg
import json

fields = ['id','name','name_cn','address','adminer','phone']

# 机房管理
@app.route('/idc',methods=['GET', 'POST'])
def idc():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    result = lists('idc',fields)
 
    return render_template('idc.html',msg=msg,idc=result['msg'])

# 添加机房
@app.route('/idcadd',methods=['GET', 'POST'])
def idcadd():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='POST':
        idc = {k:v[0] for k,v in dict(request.form).items()}
        field = ['name','name_cn','address','adminer','phone']
        result = insert_sql('idc',field,idc)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"IDC user success"}
            return  json.dumps(result)

# 修改机房信息
@app.route('/idcupdate',methods=['GET', 'POST'])
def idcupdate():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        id = request.args.get('id')
        data={'id':id}
        result = getone('idc',data,fields)
        return  json.dumps(result)

    if request.method=='POST':
        idc = {k:v[0] for k,v in dict(request.form).items()}
        print idc
        result = _update('idc',fields,idc)
        if  result['code'] == 0:
            return  json.dumps(result)

# 删除机房信息
@app.route('/idcdelete',methods=['GET', 'POST'])
def idcdelete():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='POST':
        idc = {k:v[0] for k,v in dict(request.form).items()}
        if _delete('idc',idc):
            result ={'code':0, 'msg':"delete user success"}
            return  json.dumps(result)


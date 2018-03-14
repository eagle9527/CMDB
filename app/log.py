#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,logs
from . import app
from sessions import sessionmsg
import json

#日志
@app.route('/log/',methods=['GET', 'POST'])
def log():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        return render_template('log.html',msg=msg)

#日志状态数据
@app.route('/status/',methods=['GET', 'POST'])                                                                          
def  status():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        field=["200","304","404","206","301","403"]
        result = logs('log',field)
        return json.dumps(result)

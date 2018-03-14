#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,logs,maps
from . import app
from sessions import sessionmsg
import json

# 地图展示
@app.route('/map/',methods=['GET', 'POST'])
def map():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        return render_template('map.html',msg=msg)

# 传输地图数据
@app.route('/mapdata/',methods=['GET', 'POST'])                                                                                    
def  mapdata():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        result = maps('map')
        print result
        return json.dumps(result)

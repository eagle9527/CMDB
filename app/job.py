#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql,lists
from . import app
from sessions import sessionmsg
import json
import datetime

field = ['id','apply_name','handle_name','apply_type','apply_desc','handle_desc','status','created','modified']

# Date 数据处理
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

# 添加工单
@app.route('/jobadd/',methods=['GET', 'POST'])
def jobadd():
        if 'username' not in  session:
             return redirect('/login/')
        msg = sessionmsg()
        if request.method=='GET':
            return render_template('jobadd.html',msg=msg)

        if request.method=='POST':
            job  = {k:v[0] for k,v in dict(request.form).items()}
            job['apply_name'] = session['username']
            field = ['apply_type','apply_name','apply_desc']
            result = insert_sql('job',field,job)
            if  result['code'] == 0:
                result ={'code':0, 'msg':"Job Add  success"}
                return  json.dumps(result)
# 工单列表
@app.route('/joblist/',methods=['GET', 'POST'])
def joblist():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        jobs = []
        result = lists('job',field)
        results = result['msg']
        for x in results:
            if x['status'] < 2:
                jobs.append(x)
        return render_template('joblist.html',msg=msg,joblist=jobs)

# 更新工单信息        
@app.route('/jobupdate/',methods=['GET', 'POST'])
def jobupdate():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        field = ['id','handle_name','status']
        job  = {k:v[0] for k,v in dict(request.args).items()}
        job['handle_name'] =  session['username']
        job['status'] = 1
        result = _update('job',field,job)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"Job Update  success"}
            return  json.dumps(result)
    if request.method=='POST':
        job  = {k:v[0] for k,v in dict(request.form).items()}
        field = ['id','handle_desc','status']
        job['status'] = 2
        result = _update('job',field,job)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"Job Update  success"}
            return  json.dumps(result)

# 查看工详情
@app.route('/jobdetail/',methods=['GET', 'POST'])
def  jobdetail():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        job  = {k:v[0] for k,v in dict(request.args).items()}
        field = ['id','apply_name','created','apply_desc','apply_desc','handle_desc']
        result = getone('job',job,field)
        if  result['code'] == 0:
            return  json.dumps(result, cls=DatetimeEncoder)
# 历史工单
@app.route('/jobhistory/',methods=['GET', 'POST'])
def jobhistory():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method=='GET':
        job  = lists('job',field)
    return render_template('jobhistory.html',msg=msg,joblist=job['msg'])


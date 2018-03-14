#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import request,render_template, redirect,session
from . import app
from sessions import sessionmsg
import json
import  time
import time

result = []
def getMem():
    data = {}
    f = open('/proc/meminfo')
    TotalMem = int(f.readline().split()[1])
    FreeMem = int(f.readline().split()[1])
    BufferMem = int(f.readline().split()[1])
    CacheMem = int(f.readline().split()[1])
    used = round((TotalMem-FreeMem-BufferMem-CacheMem)/round(TotalMem,4)*100,2)
    data[int(time.time())]= [int(time.time())*1000,used]
    result.append(data)
    print result
    return result

@app.route('/monitor')
def memdata():
    msg = sessionmsg()
    return  render_template('mem.html',msg=msg)

@app.route('/memdata')
def monitor():
   msg = sessionmsg()
   result = getMem()
   print result
   data = {'data':[]}
   times = int(time.time())
   for mem in result:
        data['data'].append({'name':mem.keys()[0],'value':mem.values()[0]})
   return json.dumps(data)

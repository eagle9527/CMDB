#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect,session
import json
import hashlib
import paramiko

salt='98b85629951ad584feaf87e28c073088'

app = Flask(__name__)
app.secret_key = "98b85629951ad584feaf87e28c0730881"

import login
import user
import userlist
import idc
import cabinet
import server
import job
import ansibles
import monitor
import named
import  log
import map

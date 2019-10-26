from flask import render_template,redirect,g,request,url_for,flash,g,session,json,make_response,jsonify,Response,current_app
import hashlib
import datetime
from app.auth import auth
import requests
from ..dataPort import dataPort
import redis
from functools import wraps

rs=redis.Redis(host='10.132.166.125',port=6379,decode_responses=True)

@auth.route('/login.html',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    if request.method == 'POST':
        return redirect(url_for('security.userList'))

@auth.route('/logout')
def logout():
    if session.get('username') is not None:
        inf = 'Successed!' + ' 用户 ' + session.get("username") + ' 注销成功'
        print(inf)
    else:
        print('Failed!,无效注销')
    session.clear()
    session.pop('username',None)
    flash('You were logged out')
    return redirect(url_for('auth.login'))
    # return render_template('auth/login.html')

def acquire_data(url):
    if session.get('token')==None or session.get('token')!=rs.get(session.get('username')):
        flash('token过期,请重新登录')
        print('token为None,请重新登录')
        return None
    elif session.get('token')==rs.get(session.get('username')):
        print('"tokenId:'+session['token'])
        r=requests.get(url)
        data=r.json()
        print(data)
        if data['msg']=="成功":
            return data
        elif data['code']=='412' or data['code']=='406':
            return None
        else:
            return None
    else:
        return None



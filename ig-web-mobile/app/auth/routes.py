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
        username = request.form.get('username')
        password=request.form.get('password')
        # password_origin=request.form.get('password')
        # password=hashlib.md5(password_origin.encode(encoding='UTF-8')).hexdigest()
        print(username)
        print(password)
        # headers={'content-type': 'application/json'}
        dataload={"username":username,"password":password}
        # dataload={'employCode':username,'accountPassword':password,'accountType':'web'}
        # r=requests.post(dataPort.part_login, data=json.dumps(dataload),headers=headers)
        r=requests.post(dataPort.part_login, data=json.dumps(dataload))
        print(r.json())
        if r.json()['result'] is None:
            flash('Invalid urername or password')
            return redirect(url_for('auth.login'))
        else:
            token=r.json()['result']['tokenId']
            session.clear()
            session['username']=username
            session['token']=token
            rs.set(username,token)
            print(rs)
            print(session.get('token'))
            print("111111111:"+rs.get(session.get('username')))
            # tokenId=rs.get(session['username'])
            dataDoor=acquire_data(dataPort.part_doorlog)
            dataTime=acquire_data(dataPort.part_doorlogT)
            data=acquire_data(dataPort.part_index)
            if(dataDoor!=None and dataTime!=None and data!=None):
                return render_template('security/userList.html',data=data,dataDoor=dataDoor,dataTime=dataTime)
            else:
                flash('token过期,请重新登录')
                return render_template('auth/login.html')

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
    # return redirect(url_for('auth.login'))
    return render_template('auth/login.html')

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



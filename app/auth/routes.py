from flask import render_template,redirect,request,url_for,flash,g,session,json,make_response,jsonify,Response,current_app
import hashlib
import datetime
from app.auth import auth
import requests
from ..dataPort import dataPort


@auth.route('/login.html',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password=request.form.get('password')
        # password_origin=request.form.get('password')
        # password=hashlib.md5(password_origin.encode(encoding='UTF-8')).hexdigest()
        print(password)
        headers={'content-type': 'application/json'}
        dataload={"username":username,"password":password}
        data=json.dumps(dataload)
        print(data)
        # dataload={'employCode':username,'accountPassword':password,'accountType':'web'}
        r=requests.post(dataPort.part_login, data=json.dumps(dataload),headers=headers)
        print(r.json())
        if r.json()['result'] is None:
            flash('Invalid urername or password')
            return redirect(url_for('auth.login'))
        else:
            token=r.json()['result']['tokenId']
            session.clear()
            session['username']=username
            session['token']=token
            print(session['token'])
            return render_template('base.html')

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
    r=requests.get(url)
    data=r.json()
    if data['msg']=="成功":
        # return jsonify(data)
        return data
    flash('登录超时,请重新登录')
    # return 'toekn超时'
    return render_template('auth/login.html')
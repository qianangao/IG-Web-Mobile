from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.hr import hr
import requests
from ..dataPort import dataPort 
from ..auth.routes import acquire_data,rs
# 用工分布
@hr.route('/ygList',methods=['GET'])
def ygList():
    print("tokenId1111:"+rs.get(session['username']))
    print(type(session['token']))
    if session.get('token')==None:
        print('nullNULL')
        flash('token超时,请重新登录')
        return render_template('auth/login.html')
    elif session['token']==rs.get(session['username']):
        headers={'token':session['token']}
        data=requests.post(dataPort.part_staff, headers=headers)
        result=data.json()
        if result['code']=='412':
            flash('token超时,请重新登录')
            return render_template('auth/login.html')
        print(result)
        return render_template('hr/ygList.html',data=result)
    else:
        flash('请重新登录')
        # return 'toekn超时'
        return render_template('auth/login.html')

@hr.route('/zcList',methods=['GET'])
def zcList():
    if session.get('token')==None:
        print('nullNULL')
        flash('token超时,请重新登录')
        return render_template('auth/login.html')
    elif session['token']==rs.get(session['username']):
        headers={'token':session['token']}
        data=requests.post(dataPort.part_protitle, headers=headers)
        result=data.json()
        print(result)
        if result['code']=='412':
            flash('token超时,请重新登录')
            return render_template('auth/login.html')
        
        return render_template('hr/zcList.html',data=result)
    else:
        flash('请重新登录')
        # return 'toekn超时'
        return render_template('auth/login.html')
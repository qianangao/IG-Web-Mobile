from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.hr import hr
import requests
from ..dataPort import dataPort 
from ..auth.routes import acquire_data,rs

# 用工分布
@hr.route('/ygList',methods=['GET'])
def ygList():
    if session.get('token')==None or session.get('token')!=rs.get(session.get('username')):
        print('nullNULL')
        flash('token过期,请重新登录')
        return redirect(url_for('auth.login'))
    elif session.get('token')==rs.get(session.get('username')):
        headers={'token':session['token']}
        data=requests.post(dataPort.part_staff, headers=headers)
        result=data.json()
        if result['code']=='412':
            flash('token过期,请重新登录')
            return redirect(url_for('auth.login'))
        print(result)
        return render_template('hr/ygList.html',data=result)
    else:
        flash('请重新登录')
        return redirect(url_for('auth.login'))

@hr.route('/zcList',methods=['GET'])
def zcList():
    if session.get('token')==None or session.get('token')!=rs.get(session.get('username')):
        print('nullNULL')
        flash('token过期,请重新登录')
        return redirect(url_for('auth.login'))
    elif session.get('token')==rs.get(session.get('username')):
        headers={'token':session['token']}
        data=requests.post(dataPort.part_protitle, headers=headers)
        result=data.json()
        print(result)
        if result['code']=='412':
            flash('token过期,请重新登录')
            return redirect(url_for('auth.login'))
        return render_template('hr/zcList.html',data=result)
    else:
        flash('请重新登录')
        return redirect(url_for('auth.login'))
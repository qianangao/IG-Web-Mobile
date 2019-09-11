from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.hr import hr
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data
# 用工分布
@hr.route('/ygList',methods=['GET'])
def ygList():
    if session['token']:
        headers={'token':session['token']}
        data=requests.post(dataPort.part_staff, headers=headers)
        result=data.json()
        print(result)
        return render_template('hr/ygList.html',data=result)

@hr.route('/zcList',methods=['GET'])
def zcList():
    if session['token']:
        headers={'token':session['token']}
        data=requests.post(dataPort.part_protitle, headers=headers)
        result=data.json()
        print(result)
        return render_template('hr/zcList.html',data=result)
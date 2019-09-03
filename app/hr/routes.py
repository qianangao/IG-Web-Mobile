from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.hr import hr
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data
# 用工分布
@hr.route('/ygList',methods=['GET'])
def ygList():
    if session['token']:
        data=acquire_data(dataPort.part_staff)
        # r=requests.get(dataPort.part_staff)
        datas=data['result']['list']
        return render_template('hr/ygList.html',result=datas)

@hr.route('/userList',methods=['GET'])
def userList():
    if session['token']:
        # r=requests.get(dataPort.part_user)
        # data=r.json()
        data=acquire_data(dataPort.part_user)
        return render_template('hr/userList.html',data=data)

# 职称分布
@hr.route('/zcList',methods=['GET'])
def zcList():
    if session['token']:
        # r=requests.get(dataPort.part_protitle)
        data=acquire_data(dataPort.part_protitle)
        print(data)
        datas=data['result']['list']
        print(datas)
        username=[]
        count=[]
        jsonData={}
        for data in datas:
            username.append(data['name'])
            count.append(data['userNum'])
        jsonData['username']=username
        jsonData['count']=count
        content = json.dumps(jsonData)
        return render_template('hr/zcList.html',result=datas)
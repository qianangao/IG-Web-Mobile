from flask import render_template,redirect,g,request,url_for,flash,session,json,jsonify,current_app
from app.security import security
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data,rs

#人员详情
@security.route('/getPersontrail',methods=['POST'])
def getPersontrail():
    if session.get('token')==None or session.get('token')!=rs.get(session.get('username')):
        flash('token过期,请重新登录')
        print('token过期,请重新登录人员详情')
        return redirect(url_for('auth.login'))
    elif session.get('token')==rs.get(session.get('username')):
        employCode = request.form.get("employCode")
        print(employCode)
        headers={'content-type': 'application/json','token':rs.get(session.get('username'))}
        # headers={'content-type': 'application/json','token':session['token']}
        dataload={'employCode':employCode}
        r=requests.post(dataPort.part_persontrail, data=json.dumps(dataload),headers=headers)
        employ=r.json()
        print(employ)
        return jsonify(employ)
    else:
        flash('请重新登录')
        return redirect(url_for('auth.login'))

# 人员轨迹
@security.route('/getPersonTrack',methods=['POST'])
def getPersonTrack():
    if session.get('token')==None or session.get('token')!=rs.get(session.get('username')):
        flash('token过期,请重新登录')
        print('token过期,请重新登录人员轨迹')
        return redirect(url_for('auth.login'))
    elif session.get('token')==rs.get(session.get('username')):
        headers={'content-type': 'application/json','token':session['token']}
        # headers={'Access-Control-Allow-Origin':'*','content-type': 'application/json','token':session['token']}
        employCode=request.form.get("employCode")
        startTime=request.form.get("startTime")
        endTime=request.form.get("endTime")
        dataload = {'employCode': employCode,'startTime': startTime,'endTime': endTime}
        print(dataload)
        print(headers)
        r=requests.post(dataPort.part_personTrack,data=json.dumps(dataload),headers=headers)
        personTrack=r.json()
        return jsonify(personTrack)
    else:
        flash('请重新登录')
        print('token过期,请重新登录人员轨迹token出错')
        return redirect(url_for('auth.login'))

#园区地图
@security.route('/getMap',methods=['get'])
def getMap():
    print(session.get('token'))
    if session.get('token')==None or session.get('token')!=rs.get(session.get('username')):
        flash('token过期,请重新登录')
        print('token过期,请重新登录地图问题')
        return redirect(url_for('auth.login'))
    elif session['token']==rs.get(session['username']):
        return render_template('security/getMap.html',token=json.dumps(session['token']))  
    else:
        print('请重新登录token问题')
        flash('请重新登录')
        return redirect(url_for('auth.login'))

#路口抓拍
@security.route('/getDeviceCount',methods=['get'])
def getDeviceCount():
    data=acquire_data(dataPort.part_facepic)
    if(data!=None):
        return render_template('security/DeviceCount.html',data=data)
    else:
        return redirect(url_for('auth.login'))

#一线门岗进出人流
@security.route('/userList',methods=['GET','POST'])
def userList():
    if request.method=='GET':
        dataDoor=acquire_data(dataPort.part_doorlog)
        dataTime=acquire_data(dataPort.part_doorlogT)
        data=acquire_data(dataPort.part_index)
        if(data!=None and dataTime!=None and dataDoor!=None):
            return render_template('security/userList.html',data=data,dataDoor=dataDoor,dataTime=dataTime)
        else:
            return redirect(url_for('auth.login'))
    if request.method=='POST':
        username = request.form.get('username')
        password=request.form.get('password')
        dataload={"username":username,"password":password}
        r=requests.post(dataPort.part_login, data=json.dumps(dataload))
        if r.json()['result'] is None:
            flash('Invalid urername or password')
            return redirect(url_for('auth.login'))
        else:
            token=r.json()['result']['tokenId']
            session.clear()
            session['username']=username
            session['token']=token
            rs.set(username,token)
            dataDoor=acquire_data(dataPort.part_doorlog)
            dataTime=acquire_data(dataPort.part_doorlogT)
            data=acquire_data(dataPort.part_index)
            if(dataDoor!=None and dataTime!=None and data!=None):
                return render_template('security/userList.html',data=data,dataDoor=dataDoor,dataTime=dataTime)
            else:
                return redirect(url_for('auth.login'))

# 门岗进出
@security.route('/getDoorDetail',methods=['GET'])
def getDoorDetail():
    if session.get('token')==None or session.get('token')!=rs.get(session.get('username')):
        print('nullNULL')
        flash('token过期,请重新登录')
        return redirect(url_for('auth.login'))
    elif session['token']==rs.get(session.get('username')):
        headers={'content-type': 'application/json','token':rs.get(session.get('username'))}
        # dataload={"num":""}
        data=requests.post(dataPort.part_doorDetail,headers=headers)
        # data=requests.post(dataPort.part_doorDetail, data=json.dumps(dataload),headers=headers)
        result=data.json()['data']
        print(type(result)) #list
        gateName=[]
        inDoor=[]
        outDoor=[]
        for data in result:
            gateName.append(data['gate_name'])
            inDoor.append(data['in'])
            outDoor.append(data['out'])
        # return render_template('security/getDoorDetail.html')
        return render_template('security/getDoorDetail.html',gateName=gateName,inDoor=inDoor,outDoor=outDoor)
    else:
        flash('请重新登录')
        return redirect(url_for('auth.login'))


from flask import render_template,redirect,g,request,url_for,flash,session,json,jsonify,current_app
from app.security import security
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data,rs

# #安防设备
# @security.route('/getDeviceList',methods=['POST'])
# def getDeviceList():
#     if session['token']:
#         pageno=request.form.get("pageno")
#         pagesize=request.form.get("pagesize")
#         devicetype=request.form.get("devicetype")
#         dataload={'pageno':pageno,'pagesize':pagesize,'devicetype':devicetype}
#         print(dataload)
#         r=requests.post(dataPort.part_deviceList,data=json.dumps(dataload))
#         result=r.json()
#         if result['code']==412:
#             flash('登录超时,请重新登录')
#             return render_template('auth/login.html')
#         print(result)
#         return jsonify(result)

# #人员轨迹
# @security.route('/getPersontimetrail',methods=['POST'])
# def getPersontimetrail():
#     if session['token']:
#         employCode = request.form.get("employCode")
#         time = request.form.get("time")
#         print(employCode,time)
#         headers={'content-type': 'application/json','token':session['token']}
#         dataload={'employCode':employCode,'time':time}
#         r=requests.post(dataPort.part_persontimetrail, data=json.dumps(dataload),headers=headers)
#         result=r.json()
#         if result['code']==412:
#             flash('登录超时,请重新登录')
#             return render_template('auth/login.html')
#         print(result)
#         return jsonify(result)

#人员详情
@security.route('/getPersontrail',methods=['POST'])
def getPersontrail():
    # if session['token']:
    employCode = request.form.get("employCode")
    print(employCode)
    headers={'content-type': 'application/json','token':gloVal.token}
    # headers={'content-type': 'application/json','token':session['token']}
    dataload={'employCode':employCode}
    r=requests.post(dataPort.part_persontrail, data=json.dumps(dataload),headers=headers)
    employ=r.json()
    if employ['code']==412:
        flash('登录超时,请重新登录')
        return render_template('auth/login.html')
    print(employ)
    return jsonify(employ)
#关注人员
# @security.route('/getMyFollow',methods=['POST'])
# def getMyFollow():
#     if session['token']:
#         # tokenId
#         # dataload={'employCode':session['username']}
#         # headers={'content-type': 'application/json','token':session['token']}
#         headers={'content-type': 'application/json','tokenId':session['token']}
#         dataload={"pagesize":"15","pageno":"1"}
#         r=requests.post(dataPort.part_attentionTrail,data=json.dumps(dataload),headers=headers)
#         employ=r.json()
#         # if employ['code']==412:
#         #     flash('登录超时,请重新登录')
#         #     return render_template('auth/login.html')
#         print(employ)
#         return jsonify(employ)

#园区地图
@security.route('/getMap',methods=['get'])
def getMap():
    if session.get('token')==None:
        print('nullNULL')
        flash('token超时,请重新登录')
        return render_template('auth/login.html')
    elif session['token']==rs.get(session['username']):
        print(session['token'])
        return render_template('security/getMap.html',token=json.dumps(session['token']))
        # return render_template('security/getMap.html',token=json.dumps(session['token']))
    else:
        flash('请重新登录')
        return render_template('auth/login.html')
# #园区地图
# @security.route('/getMap',methods=['get'])
# def getMap():
#     if session['token']: 
#         return render_template('security/demo.html',tokens=json.dumps(session['token']))
#路口抓拍
@security.route('/getDeviceCount',methods=['get'])
def getDeviceCount():
    # if session['token']:
        # r=requests.get(dataPort.part_facepic)
        # data=r.json()
    data=acquire_data(dataPort.part_facepic)
    if(data!=None):
        return render_template('security/DeviceCount.html',data=data)
    else:
        flash('token超时,请重新登录')
        return render_template('auth/login.html')
# # 车辆类型
# @security.route('/carTypeList')
# def carTypeList():
#     if session['token']:
#         # r=requests.get(dataPort.part_carType)
#         # data=r.json()
#         data=acquire_data(dataPort.part_carType)
#         return render_template('security/carTypeList.html',data=data)

# 一线门岗进出车流
# @security.route('/carList')
# def carList():
#     if session['token']:
#         # rDoor=requests.get(dataPort.part_cardoorlog)
#         # rTime=requests.get(dataPort.part_cardoorlogT)
#         # dataDoor=rDoor.json()
#         # dataTime=rTime.json()
#         dataDoor=acquire_data(dataPort.part_cardoorlog)
#         dataTime=acquire_data(dataPort.part_cardoorlogT)
#         print(dataDoor)
#         return render_template('security/carList.html',dataDoor=dataDoor,dataTime=dataTime)


#一线门岗进出人流
@security.route('/userList')
def userList():
    dataDoor=acquire_data(dataPort.part_doorlog)
    dataTime=acquire_data(dataPort.part_doorlogT)
    data=acquire_data(dataPort.part_index)
    if(data!=None and dataTime!=None and dataDoor!=None):
        return render_template('security/userList.html',data=data,dataDoor=dataDoor,dataTime=dataTime)
    else:
        flash('token超时,请重新登录')
        return render_template('auth/login.html')

#园区安全
# @security.route('/getCampusSecurity')
# def getCampusSecurity():
#     if session['token']:
#         # r=requests.get(dataPort.part_secuindex)
#         data=acquire_data(dataPort.part_secuindex)
#         print(data)
#         data=data['result']
#         print(data)  
#         return render_template('security/getCampusSecurity.html',data=data)
# # 安防告警
# @security.route('/getAlarm')
# def getAlarm():
#     if session['token']:
#         # r=requests.get(dataPort.part_security_warning)
#         # data=r.json()
#         data=acquire_data(dataPort.part_security_warning)
#         return render_template('security/getAlarm.html',data=data)


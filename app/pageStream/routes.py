from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.pageStream import stream
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data

#园区基本信息
@stream.route('/getCampusInfo')
def getCampusInfo():
    if session['token']:
        # r=requests.get(dataPort.part_index)
        # data=r.json()
        data=acquire_data(dataPort.part_index)
        return render_template('pageStream/getCampusInfo.html',data=data)

# 園區安防告警趨勢
@stream.route('/getAlarmTrend')
def getAlarmTrend():
    # print(session['token'])
    # print('***************')
    # if session['token']:
    #     print('---------------')
    #     # r=requests.get(dataPort.part_secutrend)
        # data=r.json()
    data=acquire_data(dataPort.part_secutrend)
    print(data)
    return render_template('pageStream/getAlarmTrend.html',data=data)
    # return render_template('auth/login.html')

#设备在线状态展示
@stream.route('/getDeviceStatus')
def getDeviceStatus():
    if session['token']:
        # r=requests.get(dataPort.part_devicestat)
        # data=r.json()
        data=acquire_data(dataPort.part_devicestat)
        print(data)
        return render_template('pageStream/getDeviceStatus.html',data=data)


from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.pageStream import stream
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data

# 園區安防告警趨勢
@stream.route('/getAlarmTrend')
def getAlarmTrend():
    data=acquire_data(dataPort.part_secutrend)
    if(data!=None):
        return render_template('pageStream/getAlarmTrend.html',data=data)
    else:
        return redirect(url_for('auth.login'))

#设备在线状态展示
@stream.route('/getDeviceStatus')
def getDeviceStatus():
    data=acquire_data(dataPort.part_devicestat)
    if(data!=None):
        return render_template('pageStream/getDeviceStatus.html',data=data)
    else:
        return redirect(url_for('auth.login'))

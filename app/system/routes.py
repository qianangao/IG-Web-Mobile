from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.system import system
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data

#平台运行状态
@system.route('/getSysStatus')
def getSysStatus():
    if session['token']:
        # r=requests.get(dataPort.part_sysStatus)
        # data=r.json()
        data=acquire_data(dataPort.part_sysStatus)
        return render_template('system/getSysStatus.html',data=data)

#接入曾状态
@system.route('/getSysAccess')
def getSysAccess():
    if session['token']:
        # r=requests.get(dataPort.part_sysAccess)
        # data=r.json()
        data=acquire_data(dataPort.part_sysAccess)
        return render_template('system/getSysAccess.html',data=data)

#运维日志
@system.route('/getSysLog')
def getSysLog():
    if session['token']:
        # r=requests.get(dataPort.part_sysLog)
        # data=r.json()
        data=acquire_data(dataPort.part_sysLog)
        return render_template('system/getSysLog.html',data=data)

#数据接入状态
@system.route('/getDataStatus')
def getDataStatus():
    if session['token']:
        # r=requests.get(dataPort.part_sysdataStatus)
        # data=r.json()
        data=acquire_data(dataPort.part_sysdataStatus)
        print(data)
        return render_template('system/getDataStatus.html',data=data)

#数据接入趋势图
@system.route('/getDataCount')
def getDataCount():
    if session['token']:
        # r=requests.get(dataPort.part_sysdataCount)
        # data=r.json()
        data=acquire_data(dataPort.part_sysdataCount)
        print(data)
        return render_template('system/getDataCount.html',data=data)

#微服务调用状态
@system.route('/getMicroStatus')
def getMicroStatus():
    if session['token']:
        # r=requests.get(dataPort.part_sysmicroStatus)
        # data=r.json()
        data=acquire_data(dataPort.part_sysmicroStatus)
        print(data)
        return render_template('system/getMicroStatus.html',data=data)


#其他数据
@system.route('/getOther')
def getOther():
    if session['token']:
        # r=requests.get(dataPort.part_sysOther)
        # data=r.json()
        data=acquire_data(dataPort.part_sysOther)
        print(data)
        return render_template('system/getOther.html',data=data)
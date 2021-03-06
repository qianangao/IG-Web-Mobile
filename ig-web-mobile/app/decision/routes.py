from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.decision import decision
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data

#感知分布
@decision.route('/getSensor')
def getSensor():
    data=acquire_data(dataPort.part_sensor)
    if(data!=None):
        return render_template('decision/getSensor.html',data=data)
    else:
        return redirect(url_for('auth.login'))
    

#人力整体趋势
@decision.route('/getUserTrend')
def getUserTrend():
    data=acquire_data(dataPort.part_userTrend)
    if(data!=None):
        return render_template('decision/getUserTrend.html',data=data)
    else:
        return redirect(url_for('auth.login'))

#人力整体分布
@decision.route('/getUserDis')
def getUserDis():
    data=acquire_data(dataPort.part_userDis)
    if(data!=None):
        datas=data['result']['list']
        parkName =[]
        parkUser= []
        for data in datas:
            parkName.append(data['parkName'])
            parkUser.append(data['parkUser'])
        return render_template('decision/getUserDis.html',parkName=parkName,parkUser=parkUser)
    else:
        return redirect(url_for('auth.login'))

#智慧园区出勤人数
@decision.route('/getCampus')
def getCampus():
    data=acquire_data(dataPort.part_safe)
    if(data!=None):
        datas=data['result']['list']
        parkAttendance =[]
        parkName= []
        workTime=[]
        for data in datas:
            parkAttendance.append(data['parkAttendance'])
            parkName.append(data['parkName'])
            workTime.append(data['workTime'])
        return render_template('decision/getCampus.html',parkAttendance=parkAttendance,parkName=parkName,workTime=workTime)
    else:
        return redirect(url_for('auth.login'))
#智慧园区平均工时
@decision.route('/getworkTime')
def getworkTime():
    data=acquire_data(dataPort.part_safe)
    if(data!=None):
        datas=data['result']['list']
        print(len(datas))
        parkAttendance =[]
        parkName= []
        workTime=[]
        for data in datas:
            parkAttendance.append(data['parkAttendance'])
            parkName.append(data['parkName'])
            workTime.append(data['workTime'])
        print(data)
        return render_template('decision/getWorkTime.html',parkAttendance=parkAttendance,parkName=parkName,workTime=workTime)
    else:
        return redirect(url_for('auth.login'))


#安全分布
@decision.route('/getSafe')
def getSafe():
    data=acquire_data(dataPort.part_safe)
    if(data!=None):
        datas=data['result']['list']
        parkName= []
        safeDay = []
        safeDayZt= []
        safeIndex = []
        safeIndexZt = []
        for data in datas:
            parkName.append(data['parkName'])
            safeDay.append(data['safeDay'])
            safeDayZt.append(data['safeDayZt'])
            safeIndex.append(data['safeIndex'])
            safeIndexZt.append(data['safeIndexZt'])
        return render_template('decision/getSafe.html',safeDay=safeDay,safeDayZt=safeDayZt,parkName=parkName,safeIndex=safeIndex,safeIndexZt=safeIndexZt)         
    else:
        return redirect(url_for('auth.login'))

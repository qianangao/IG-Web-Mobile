from flask import render_template,redirect,request,url_for,flash,session,json,jsonify,current_app
from app.decision import decision
import requests
from ..dataPort import dataPort
from ..auth.routes import acquire_data
#感知分布
@decision.route('/getSensor')
def getSensor():
    if session['token']:
        data=acquire_data(dataPort.part_sensor)
        return render_template('decision/getSensor.html',data=data)

#人力整体趋势
@decision.route('/getUserTrend')
def getUserTrend():
    if session['token']:
        data=acquire_data(dataPort.part_userTrend)
        return render_template('decision/getUserTrend.html',data=data)

# #人力整体趋势
# @decision.route('/getDuty')
# def getDuty():
#     if session['token']:
#         data = acquire_data(dataPort.part_onduty)
#         return render_template('decision/getDuty.html',datas=data)

#人力整体分布
@decision.route('/getUserDis')
def getUserDis():
    if session['token']:
        data=acquire_data(dataPort.part_userDis)
        # r=requests.get(dataPort.part_userDis)
        datas=data['result']['list']
        parkName =[]
        parkUser= []
        for data in datas:
            parkName.append(data['parkName'])
            parkUser.append(data['parkUser'])
        return render_template('decision/getUserDis.html',parkName=parkName,parkUser=parkUser)
        # return render_template('decision/getUserDis.html',data=data)

#智慧园区出勤人数
@decision.route('/getCampus')
def getCampus():
    if session['token']:
        # r=requests.get(dataPort.part_safe)
        data=acquire_data(dataPort.part_safe)
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
        return render_template('decision/getCampus.html',parkAttendance=parkAttendance,parkName=parkName,workTime=workTime) 
#智慧园区平均工时
@decision.route('/getworkTime')
def getworkTime():
    if session['token']:
        data=acquire_data(dataPort.part_safe)
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


#安全分布
@decision.route('/getSafe')
def getSafe():
    if session['token']:
        data=acquire_data(dataPort.part_safe)
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


class dataPort():
    page_dataport="http://10.132.166.121:5813";
    part_login=page_dataport+"/web/sys/login";
    #安防主题  
    part_doorlog = page_dataport + "/safety/doorLog/userList";#一线门岗人流
    part_doorlogT = page_dataport + "/safety/statistics/userListHour";#一线门岗人流-时间
    part_facepic = page_dataport + "/safety/device/getDeviceCount";#设备抓拍
    # 人資视图
    part_protitle = page_dataport + "/safety/humancapital/zcList";#职称分布
    part_staff = page_dataport + "/safety/humancapital/ygList";#用工类型
    # 綜合人流視圖
    part_secutrend = page_dataport + "/safety/alarm/countList"#園區安防告警趨勢
    part_index=page_dataport+"/safety/comprehensive/index"#园区基本信息
    part_devicestat = page_dataport + "/safety/device/getCountByType"#设备在线状态展示

    #决策者主题
    part_sensor = page_dataport + "/safety/boss/yesWork" #感知分布
    part_userTrend = page_dataport + "/safety/boss/userNum" #人力整体趋势
    part_userDis = page_dataport + "/safety/boss/userDis" #人力整体分布
    part_safe = page_dataport + "/safety/boss/safe" #安全分布
    part_onduty = page_dataport + "/safety/humancapital/index" #考勤
    part_personTrack =  page_dataport + "/others/track/appToAbility/getEmployTrackList/1/40"
    # 地图接口
    part_persontrail =  page_dataport + "/others/employs/getEmploysInfos" #人员详情
    part_doorDetail =  page_dataport + "/others/employs/getGatesInOut" #人员详情
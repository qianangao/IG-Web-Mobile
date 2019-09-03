class dataPort():
    page_dataport="http://10.132.166.121:5813";
    part_login=page_dataport+"/web/sys/login";
    # part_login=page_dataport+"/safety/user/login";
    # part_login=page_dataport+"/track/account/checkLoginAccount";
    #安防主题  
    part_doorlog = page_dataport + "/safety/doorLog/userList";#一线门岗人流
    part_doorlogT = page_dataport + "/safety/statistics/userListHour";#一线门岗人流-时间
    part_cardoorlog = page_dataport + "/safety/doorLog/carList";#一线门岗车流
    part_cardoorlogT = page_dataport + "/safety/statistics/carListHour";#一线门岗车流-时间
    part_facepic = page_dataport + "/safety/device/getDeviceCount";#设备抓拍
    part_carType = page_dataport + "/safety/statistics/carTypeList";#车辆类型数据
    part_security_warning = page_dataport + "/safety/alarm/list";#安防警告
    part_secuindex = page_dataport + "/safety/statistics/index";#安全指数
    # part_deviceDetail = page_dataport + "/safety/device/detail";#安防设备详情
    # 人資视图
    part_user = page_dataport + "/safety/humancapital/userList";#最近12個月人力分布
    part_protitle = page_dataport + "/safety/humancapital/zcList"#职称分布
    part_staff = page_dataport + "/safety/humancapital/ygList"#用工类型
    # 綜合人流視圖
    part_secutrend = page_dataport + "/safety/alarm/countList"#園區安防告警趨勢
    part_index=page_dataport+"/safety/comprehensive/index"#园区基本信息
    part_devicestat = page_dataport + "/safety/device/getCountByType"#设备在线状态展示

    #决策者主题
    part_sensor = page_dataport + "/safety/boss/yesWork" #感知分布
    part_userTrend = page_dataport + "/safety/boss/userNum" #人力整体趋势
    part_userDis = page_dataport + "/safety/boss/userDis" #人力整体分布
    part_safe = page_dataport + "/safety/boss/safe" #安全分布
    part_onduty = page_dataport + '/safety/humancapital/index' #考勤
    # part_iBrain = page_dataport + "/safety/boss/head" #园区智脑

    #运维主题
    part_sysStatus = page_dataport + "/safety/oper/status" #平台状态
    part_sysAccess = page_dataport + "/safety/oper/accessStatus" #接入层状态
    part_sysLog = page_dataport + "/safety/oper/log" #运维日志
    part_sysdataStatus = page_dataport + "/safety/oper/dataStatus" #数据状态
    part_sysdataCount = page_dataport + "/safety/oper/dataCount" #数据统计
    # part_sysdeviceStatus = page_dataport + "/safety/oper/deviceStatus" #设备状态
    part_sysmicroStatus = page_dataport + "/safety/oper/wStatus" #微服务调用情况
    part_sysOther = page_dataport + "/safety/oper/otherData" #其他服务
    # 地图接口
    part_persontrail = "http://10.132.166.121:5814/employs" #人员详情
    # part_persontrail = page_dataport + "/safety/person/getEmployDetail"#人员详情
    part_persontimetrail = page_dataport + "/safety/person/getTrail"#人员轨迹
    part_deviceList = page_dataport + "/safety/device/list" #设备信息接口

    part_attentionTrail=page_dataport+"/web/trail/getMyFollowPerson"
    # part_attentionTrail=page_dataport + "/safety/appUser/getMyFollow"

    
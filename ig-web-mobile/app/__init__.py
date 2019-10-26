from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_cors import *
import os
from py_eureka_client import eureka_client

from .util.common_util import logger


# app变量被定义为 init .py脚本中的Flask类的一个实例
bootstrap=Bootstrap()

def create_app():
    app = Flask(__name__)
    # CORS(app,resources=r'/*')
    app.secret_key = os.urandom(24) #生成一串随机24位的字符
    bootstrap.init_app(app)

    if not os.path.exists('log'):
        os.mkdir('log')

    log = logger('flask')
    app.log = log

    """拦截器
        对每个请求结束后做其他处理
    """
    @app.after_request
    def after_request(response):
        ip = request.remote_addr
        url = request.url
        app.log.info(str(response.status) + '-' + str(ip) + '-' + str(url))
        return response

    eureka_client.init(eureka_server="http://10.132.166.121:5012/eureka",
                       app_name="ig-web-mobile",
                       instance_host='10.132.166.122',
                       instance_port=8023,
                       ha_strategy=eureka_client.HA_STRATEGY_RANDOM)
    
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp,url_prefix='/auth')
    from app.security import security as security_bp
    app.register_blueprint(security_bp,url_prefix='/security')
    from app.hr import hr as hr_bp
    app.register_blueprint(hr_bp,url_prefix='/hr')
    from app.pageStream import stream as stream_bp
    app.register_blueprint(stream_bp,url_prefix='/stream')
    from app.decision import decision as decision_bp
    app.register_blueprint(decision_bp,url_prefix='/decision')
    return app

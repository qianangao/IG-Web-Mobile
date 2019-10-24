from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import *
import os
# app变量被定义为 init .py脚本中的Flask类的一个实例
bootstrap=Bootstrap()

def create_app():
    app = Flask(__name__)
    # CORS(app,resources=r'/*')
    app.secret_key = os.urandom(24) #生成一串随机24位的字符
    bootstrap.init_app(app)


    
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
    from app.system import system as system_bp
    app.register_blueprint(system_bp,url_prefix='/system')
    return app
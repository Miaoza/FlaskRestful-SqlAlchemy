# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-01-18 17:15:11
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:41:00+08:00

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

app = Flask(__name__)
app.config.from_object(config['development'])  # 获取相应的配置类
CORS(app)
db = SQLAlchemy(app)

from upload.upload import up_bp as up_api
from admin.admin import admin_bp as adm_api
from user.user import user_bp as u_api
from cartoon.cartoon import car_bp as cart_api
from message.message import msg_bp as m_api

app.register_blueprint(up_api, url_prefix="/api") #注册蓝图
app.register_blueprint(adm_api, url_prefix="/api")
app.register_blueprint(u_api, url_prefix="/api")
app.register_blueprint(cart_api, url_prefix="/api")
app.register_blueprint(m_api, url_prefix="/api")

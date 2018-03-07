# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-18 17:15:11
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-06 11:04:17
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

app = Flask(__name__)
app.config.from_object(config['development'])  # 获取相应的配置类
CORS(app)
db = SQLAlchemy(app)

from upload.upload import up_bp as up_api
from user.user import user_bp as u_api
from organ.organ import organ_bp as or_api
from purchase.material import pro_bp as pu_api

app.register_blueprint(up_api, url_prefix="/api")
app.register_blueprint(u_api, url_prefix="/api")
app.register_blueprint(or_api, url_prefix="/api")
app.register_blueprint(pu_api, url_prefix="/api")


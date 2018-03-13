# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-19 17:39:47
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-26 17:13:08

from app.user.model import User
# from app.organ.model import Organ
# from app.purchase.model import *

from flask_sqlalchemy import SQLAlchemy
from app import db


# print(s)
db.drop_all()
db.create_all()

user = User(uname="nianko33", password="123456", role="admin")
db.session.add(user)
db.session.commit()
db.session.close()

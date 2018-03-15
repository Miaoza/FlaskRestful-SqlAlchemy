# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T12:22:04+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:59:20+08:00


from app.admin.model import AdminUser
# from app.cartoon.model import Cartoon
# from app.message.model import Message
# from app.user.model import *

# from flask_sqlalchemy import SQLAlchemy
from app import db

db.drop_all()
db.create_all()

admin_user = AdminUser(uname="nianko33", password="123456", role="admin")
db.session.add(admin_user)
db.session.commit()
db.session.close()

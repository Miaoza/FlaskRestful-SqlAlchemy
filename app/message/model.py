# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T17:06:21+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T15:14:52+08:00

from app import db

class Message(db.Model):
    __tablename__="message"
    __table_args__={
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.Text)
    reply_id = db.Column(db.Integer, nullable=False, default=0)
    user = db.Column(db.Integer, nullable=False)
    cartoon = db.Column(db.Integer)
    created_at = db.Column(db.String(125))
    status = db.Column(db.Integer, default=1) #1 显示 0 隐藏

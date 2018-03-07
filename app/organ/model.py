# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-22 15:23:03
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-22 16:39:59

from app import app, db

class Organ(db.Model):
    __tablename__ = "organ"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    intro = db.Column(db.Text)
    address = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    tel = db.Column(db.String(20), nullable=False)
    remark = db.Column(db.String(320))

    def __repr__(self):
        return '<Organ %r>' % self.id
# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-23 17:29:09
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-30 17:51:10

from app import app, db

requires = db.Table('requires',
    db.Column('material_id', db.Integer, db.ForeignKey('material.id'), primary_key=True),
    db.Column('purchase_id', db.Integer, db.ForeignKey('purchase.id'), primary_key=True),
)

class Category(db.Model):
    __tablename__ = 'category'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    def __repr__(self):
        return '<User %r>' % self.id

class Material(db.Model):
    __tablename__ = 'material'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    store = db.Column(db.Integer, default=0)
    counts = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer)
    def __repr__(self):
        return '<Material %r>' % self.id

class Purchase(db.Model):
    __tablename__ = 'purchase'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255), nullable=False)
    create_date = db.Column(db.String(255), nullable=False)
    update_date = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer)
    remark = db.Column(db.Text)
    materials = db.relationship('Material', secondary=requires, backref=db.backref('purchases', lazy='dynamic'))
    def __repr__(self):
        return '<Purchase %r>' % self.id

class Plan(db.Model):
    __tablename__ = "plan"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }

    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.String(255), nullable=False, unique=True)
    purchase_id = db.Column(db.Integer, unique=True)
    create_date = db.Column(db.String(255), nullable=False)
    update_date = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)



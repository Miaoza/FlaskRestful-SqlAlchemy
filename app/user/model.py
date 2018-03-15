# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T12:14:14+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T17:08:59+08:00


from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash,check_password_hash#转换密码用到的库
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import app, db
# from app.cartoon.model import *

app.config['SECRET_KEY'] = 'secret key'
auth = HTTPTokenAuth(scheme='Token')

collect = db.Table(
    'collected',
    db.Column('cartoon_id', db.Integer, db.ForeignKey('cartoon.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

visited = db.Table(
    'visited',
    db.Column('cartoon_id', db.Integer, db.ForeignKey('cartoon.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

recommend = db.Table(
    'recommend',
    db.Column('cartoon_id', db.Integer, db.ForeignKey('cartoon.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(225), unique=True)
    pwd_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(125), nullable=False, default='user')
    avatar = db.Column(db.String(255))
    tel = db.Column(db.String(20), unique=True, nullable=False)
    exp = db.Column(db.Integer, default=0)
    # relationship 第一个参数是关联类的名字
    collected = db.relationship('Cartoon', secondary=collect, backref=db.backref('collect', lazy='dynamic'))
    visited = db.relationship('Cartoon', secondary=visited, backref=db.backref('visite', lazy='dynamic'))
    recommend = db.relationship('Cartoon', secondary=recommend, backref=db.backref('recommend', lazy='dynamic'))
    # secondary 在多对多关系中指定要使用的关联的表名称
    # backref 在关系的其他模型中添加一个反向引用
    # dynamic 返回另一个查询对象，可以加载这些条目时进一步提取
    created_at = db.Column(db.String(225))
    status = db.Column(db.Integer, default=1) #1 正常 0 禁止评论 -1 禁止登录

    def __repr__(self):
        return '<User %r>' % self.id

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    #转换密码为hash存入数据库
    @password.setter
    def password(self, password):
        self.pwd_hash = generate_password_hash(password)

    #检查密码
    def check_password(self, password):
        return check_password_hash(self.pwd_hash, password)

    #实例化一个签名序列化对象 serializer，有效期 100 分钟
    def generate_auth_token(self, expiration=6000):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({"id": self.id})

    # 回调函数，对 token 进行验证
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None # invalid token
        user = User.query.get(data['id'])
        return user


class Exp(db.Model):
    __tablename__ = 'exp'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }
    lev = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, unique=True, default=0)    #unique=True 值唯一

    def __repr__(self):
        return '<Exp %r>' % self.lev

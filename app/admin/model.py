# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T15:58:17+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:51:34+08:00

from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash,check_password_hash#转换密码用到的库
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import app, db

app.config['ADMIN_SECRET_KEY'] = 'secret key'
auth = HTTPTokenAuth(scheme='Token')

class AdminUser(db.Model):
    __tablename__ = "admin_user"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8"
    }
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(255), unique=True)
    pwd_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(125), nullable=False, default='admin')
    avatar = db.Column(db.String(255))

    def __repr__(self):
        return '<AdminUser %r>' % self.id

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
        s = Serializer(app.config['ADMIN_SECRET_KEY'], expires_in=expiration)
        return s.dumps({"id": self.id})

    # 回调函数，对 token 进行验证
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['ADMIN_SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None # invalid token
        admin_user = AdminUser.query.get(data['id'])
        return admin_user

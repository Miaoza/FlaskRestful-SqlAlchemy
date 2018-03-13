# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-19 11:58:29
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-06 11:08:24

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, marshal

from app import db
from app.auth.auth import *
from model import User
from fields import *

user_bp = Blueprint('user', __name__)
user_api = Api(user_bp)

class Login(Resource):
    def post(self):
        args = login_parser.parse_args()
        uname = args['uname']
        pwd = args['pwd']
        user = User.query.filter(User.uname==uname).first()
        if user and user.check_password(pwd):
            user.token = user.generate_auth_token() #token
            user = marshal(user, user_fields)
            return jsonify({"code": 1, "data": user})
        else:
            return jsonify({"code": -1, "message": "账号或密码错误"})

class Users(Resource):
    @required_auth
    def get(self):
        args = list_parser.parse_args()
        limit = args["limit"]
        offset = args["offset"]
        users = User.query.order_by(User.id.desc()).offset(offset).limit(limit).all()
        for user in users:
            user.token = user.generate_auth_token()
        users = marshal(users, user_fields)
        return jsonify({"code": 1, "data": users})

    @required_auth
    def post(self):
        args = user_parser.parse_args()
        uname = args['uname']
        pwd = '123456'
        avatar = args['avatar']
        role = args['role']
        query = User.query.filter(User.uname==uname).first()
        if query:
            return jsonify({"code": -1, "message": "用户已存在"})
        user = User(uname=uname, password=pwd, avatar=avatar, role=role)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "添加失败"})
        else:
            return jsonify({"code": 1, "message": "添加成功"})

class UserView(Resource):
    @required_auth
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"code": -1, "message": "用户不存在"})
        user.token = user.generate_auth_token() #token
        user = marshal(user, user_fields)
        return jsonify({"code": 1, "data": user})

    @required_auth
    def put(self, user_id):
        args = user_parser.parse_args()
        uname = args['uname']
        avatar = args['avatar']
        role = args['role']

        user = User.query.get(user_id)
        if not user:
            return jsonify({"code": -1, "message": "用户不存在"})
        user.uname = uname
        user.avatar = avatar
        user.role = role
        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "修改失败"})
        else:
            return jsonify({"code": 1, "message": "已修改"})

    @required_auth
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"code": -1, "message": "用户不存在"})
        try:
            db.session.delete(user)
            db.session.commit
        except:
            return jsonify({"code": -1, "message": "删除失败"})
        else:
            return jsonify({"code": 1, "message": "已删除"})

class Me(Resource):
    @required_auth
    def get(self):
        auth = request.authorization
        me = User.verify_auth_token(auth.username)
        me.token = me.generate_auth_token() #token
        me = marshal(me, user_fields)
        return jsonify({"code": 1, "data": me})

    @required_auth
    def put(self):
        auth = request.authorization
        me = User.verify_auth_token(auth.username)
        args = me_parser.parse_args()
        pwd = args['pwd']
        avatar = args['avatar']
        if not pwd and not avatar:
            return jsonify({"code": -1, "message": "not modify"})
        if pwd:
            me.password = pwd
        if avatar:
            me.avatar = avatar
        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "修改失败"})
        else:
            me = User.verify_auth_token(auth.username)
            me.token = me.generate_auth_token() #token
            me = marshal(me, user_fields)
            return jsonify({"code": 1, "data": me})

class OrganUsers(Resource):
    @required_auth
    def get(self):
        user = User.query.filter(User.role=='organ').all()
        user = marshal(user, user_fields)
        return jsonify({"code": 1, "data": user})

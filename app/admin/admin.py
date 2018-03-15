# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T15:59:20+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:38:57+08:00
from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, marshal

from app import db
from app.auth.admin_auth import *
from model import AdminUser
from fields import *

admin_bp = Blueprint('admin', __name__)
admin_api = Api(admin_bp)

class AdminLogin(Resource):
    def post(self):
        args = admin_login_parser.parse_args()
        uname = args['uname']
        pwd = args['pwd']
        admin_user = AdminUser.query.filter(AdminUser.uname==uname).first()
        if admin_user and admin_user.check_password(pwd):
            admin_user.token = admin_user.generate_auth_token() #token
            admin_user = marshal(admin_user, admin_user_fields)
            return jsonify({"code": 1, "data": admin_user})
        else:
            return jsonify({"code": -1, "message": "账号或密码错误"})

class AdminUsers(Resource):
    @required_admin_auth
    def get(self):
        args = list_parser.parse_args()
        limit = args["limit"]
        offset = args["offset"]
        admin_users = AdminUser.query.order_by(AdminUser.id.desc()).offset(offset).limit(limit).all()
        for admin_user in admin_users:
            admin_user.token = admin_user.generate_auth_token()
        admin_users = marshal(admin_users, admin_user_fields)
        return jsonify({"code": 1, "data": admin_users})

    @required_admin_auth
    def post(self):
        args = admin_user_parser.parse_args()
        uname = args['uname']
        pwd = '123456'
        avatar = args['avatar']
        role = args['role']
        query = AdminUser.query.filter(AdminUser.uname==uname).first()
        if query:
            return jsonify({"code": -1, "message": "用户已存在"})
        admin_user = AdminUser(uname=uname, password=pwd, avatar=avatar, role=role)
        try:
            db.session.add(admin_user)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "添加失败"})
        else:
            return jsonify({"code": 1, "message": "添加成功"})

class AdminUserView(Resource):
    @required_admin_auth
    def get(self, user_id):
        admin_user = AdminUser.query.get(user_id)
        if not admin_user:
            return jsonify({"code": -1, "message": "用户不存在"})
        admin_user.token = admin_user.generate_auth_token() #token
        admin_user = marshal(admin_user, admin_user_fields)
        return jsonify({"code": 1, "data": admin_user})

    @required_admin_auth
    def put(self, user_id):
        args = admin_user_parser.parse_args()
        uname = args['uname']
        avatar = args['avatar']
        role = args['role']

        admin_user = AdminUser.query.get(user_id)
        if not admin_user:
            return jsonify({"code": -1, "message": "用户不存在"})
        admin_user.uname = uname
        admin_user.avatar = avatar
        admin_user.role = role
        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "修改失败"})
        else:
            return jsonify({"code": 1, "message": "已修改"})

    @required_admin_auth
    def delete(self, user_id):
        admin_user = AdminUser.query.get(user_id)
        if not admin_user:
            return jsonify({"code": -1, "message": "用户不存在"})
        try:
            db.session.delete(admin_user)
            db.session.commit
        except:
            return jsonify({"code": -1, "message": "删除失败"})
        else:
            return jsonify({"code": 1, "message": "已删除"})

class AdminMe(Resource):
    @required_admin_auth
    def get(self):
        auth = request.authorization
        me = AdminUser.verify_auth_token(auth.username)
        me.token = me.generate_auth_token() #token
        me = marshal(me, admin_user_fields)
        return jsonify({"code": 1, "data": me})

    @required_admin_auth
    def put(self):
        auth = request.authorization
        me = AdminUser.verify_auth_token(auth.username)
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
            me = AdminUser.verify_auth_token(auth.username)
            me.token = me.generate_auth_token() #token
            me = marshal(me, admin_user_fields)
            return jsonify({"code": 1, "data": me})

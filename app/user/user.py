# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T12:17:46+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:38:49+08:00


from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, marshal

from app import db
from model import User
from fields import *
from app.auth.auth import *
from app.auth.admin_auth import *

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

class UsersTable(Resource):
    @required_admin_auth
    def get(self):
        pass

class UsersTableView(Resource):
    @required_admin_auth
    def get(self, user_id):
        pass

    @required_admin_auth
    def put(self, user_id):
        pass

class Users(Resource):
    @required_auth
    def get(self):
        pass

    def post(self):
        pass

class UserView(Resource):
    @required_auth
    def get(self, user_id):
        pass

    @required_auth
    def put(self, user_id):
        pass

    @required_auth
    def delete(self, user_id):
        pass

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
        pass

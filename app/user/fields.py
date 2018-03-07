# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-19 11:58:21
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-31 18:20:36

from flask_restful import fields,reqparse

user_fields = {
    'id': fields.Integer,
    'uname': fields.String,
    'avatar': fields.String,
    'role': fields.String,
    'token': fields.String
}

user_parser = reqparse.RequestParser()
user_parser.add_argument('uname', type=unicode, required=True)
user_parser.add_argument('avatar', type=unicode)
user_parser.add_argument('role', type=unicode, required=True)

login_parser = reqparse.RequestParser()
login_parser.add_argument('uname', type=unicode, required=True)
login_parser.add_argument('pwd', type=unicode, required=True)

me_parser = reqparse.RequestParser()
me_parser.add_argument('pwd', type=unicode)
me_parser.add_argument('avatar', type=unicode)

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode, required=True)
list_parser.add_argument('offset', type=unicode, required=True)


# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T12:14:06+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T12:25:52+08:00


from flask_restful import fields,reqparse

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode, required=True)
list_parser.add_argument('offset', type=unicode, required=True)

cartoon_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'intro': fields.String,
    'pub_date': fields.String,
    'icon': fields.String,
    'video_url': fields.String,
    'count': fields.Integer,
    'status': fields.Integer
}

user_fields = {
    'id': fields.Integer,
    'uname': fields.String,
    'avatar': fields.String,
    'role': fields.String,
    'token': fields.String,
    'created_at': fields.String,
    'exp': fields.Integer,
    'lev': fields.Integer,
    'collected': fields.Nested(cartoon_fields),
    'visited': fields.Nested(cartoon_fields),
    'status': fields.Integer
}

user_parser = reqparse.RequestParser()
user_parser.add_argument('uname', type=unicode, required=True)
user_parser.add_argument('avatar', type=unicode)
user_parser.add_argument('tel', type=unicode, required=True)

login_parser = reqparse.RequestParser()
login_parser.add_argument('uname', type=unicode, required=True)
login_parser.add_argument('pwd', type=unicode, required=True)

me_parser = reqparse.RequestParser()
me_parser.add_argument('pwd', type=unicode)
me_parser.add_argument('avatar', type=unicode)

exp_fields = {
    'lev': fields.Integer,
    'value': fields.Integer
}

# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T15:58:33+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-14T18:22:46+08:00

from flask_restful import fields,reqparse

admin_user_fields = {
    'id': fields.Integer,
    'uname': fields.String,
    'avatar': fields.String,
    'role': fields.String,
    'token': fields.String
}

admin_user_parser = reqparse.RequestParser()
admin_user_parser.add_argument('uname', type=unicode, required=True)
admin_user_parser.add_argument('avatar', type=unicode)
admin_user_parser.add_argument('role', type=unicode, required=True)

admin_login_parser = reqparse.RequestParser()
admin_login_parser.add_argument('uname', type=unicode, required=True)
admin_login_parser.add_argument('pwd', type=unicode, required=True)

admin_me_parser = reqparse.RequestParser()
admin_me_parser.add_argument('pwd', type=unicode)
admin_me_parser.add_argument('avatar', type=unicode)

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode, required=True)
list_parser.add_argument('offset', type=unicode, required=True)

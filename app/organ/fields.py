# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-22 15:22:55
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-25 14:57:03

from flask_restful import fields,reqparse

user_field = {
    'id': fields.Integer,
    'uname': fields.String,
    'avatar': fields.String,
    'role': fields.String,
}

organ_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'intro': fields.String,
    'address': fields.String,
    'principal': fields.Nested(user_field),
    'tel': fields.String,
    'remark': fields.String
}

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode)
list_parser.add_argument('offset', type=unicode)

organ_parser = reqparse.RequestParser()
organ_parser.add_argument('name', type=unicode, required=True)
organ_parser.add_argument('intro', type=unicode)
organ_parser.add_argument('address', type=unicode, required=True)
organ_parser.add_argument('user_id', type=unicode, required=True)
organ_parser.add_argument('tel', type=unicode, required=True)
organ_parser.add_argument('remark', type=unicode)
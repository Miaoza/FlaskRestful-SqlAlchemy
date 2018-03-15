# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T17:06:29+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T12:07:47+08:00

from flask_restful import fields,reqparse

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode, required=True)
list_parser.add_argument('offset', type=unicode, required=True)

user_fileds = {
    'id': fields.Integer,
    'uname': fields.String,
    'avatar': fields.String,
    'lev': fields.Integer,
    'status': fields.Integer
}
cartoon_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'intro': fields.String,
    'pub_date': fields.String,
    'icon': fields.String,
}
msg_fields = {
    'id': fields.Integer,
    'context': fields.String,
    'user': fields.Nested(user_fileds),
    'reply_id': fields.Integer,
    'cartoon': fields.Nested(cartoon_fields),
    'created_at': fields.Integer,
    'status': fields.Integer
}

msg_status_parser = reqparse.RequestParser()
msg_status_parser.add_argument('status', type=int, required=True)

add_msg_parser = reqparse.RequestParser()
add_msg_parser.add_argument('cartoon', type=unicode, required=True)
add_msg_parser.add_argument('context', type=unicode, required=True)
add_msg_parser.add_argument('user', type=unicode, required=True)
add_msg_parser.add_argument('reply_id', type=unicode, required=True)
add_msg_parser.add_argument('cartoon', type=unicode, required=True)

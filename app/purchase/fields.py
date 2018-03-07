# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-23 17:30:47
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-02 15:15:17

from flask_restful import fields,reqparse

from app.user.fields import user_fields

cate_fields = {
    'id': fields.Integer,
    'name': fields.String,
}
cate_parser = reqparse.RequestParser()
cate_parser.add_argument('name', type=unicode, required=True)

mate_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'store': fields.Integer,
    'counts': fields.Integer,
    'category': fields.Nested(cate_fields)
}

mate_parser = reqparse.RequestParser()
mate_parser.add_argument('name', type=unicode, required=True)
mate_parser.add_argument('store', type=unicode, required=True)
mate_parser.add_argument('category_id', type=unicode, required=True)

mate_options_parser = reqparse.RequestParser()
mate_options_parser.add_argument('material_ids', type=unicode, action='append')

pur_fields = {
    'id': fields.Integer,
    'user': fields.Nested(user_fields),
    'status': fields.String,
    'materials': fields.List(fields.Nested(mate_fields)),
    'create_date': fields.String,
    'update_date': fields.String,
    'remark': fields.String
}

pur_parser = reqparse.RequestParser()
pur_parser.add_argument('materials', type=dict, action='append', required=True)
pur_parser.add_argument('remark', type=unicode)

plan_fields = {
    "id": fields.Integer,
    "order": fields.String,
    'create_date': fields.String,
    'update_date': fields.String,
    'purchase': fields.Nested(pur_fields)
}

plan_parser = reqparse.RequestParser()
plan_parser.add_argument('purchase_id', type=unicode, required=True)
plan_parser.add_argument('status', type=unicode, default='pass', required=True)

put_plan_parser = reqparse.RequestParser()
put_plan_parser.add_argument('status', type=unicode, default='pass', required=True)

list_parser = reqparse.RequestParser()
list_parser.add_argument('limit', type=unicode)
list_parser.add_argument('offset', type=unicode)
# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T15:02:29+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-14T18:42:19+08:00

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
    'created_at': fields.String,
    'is_collected': fields.Boolean(default=False),
    'is_visited': fields.Boolean(default=False),
    'is_recommend': fields.Boolean(default=False),
    'status': fields.Integer
}

admin_cartoon_parser = reqparse.RequestParser()
admin_cartoon_parser.add_argument('name', type=unicode, required=True)
admin_cartoon_parser.add_argument('intro', type=unicode)
admin_cartoon_parser.add_argument('pub_date', type=unicode)
admin_cartoon_parser.add_argument('icon', type=unicode, required=True)
admin_cartoon_parser.add_argument('video_url', type=unicode, required=True)

admin_put_cartoon_parser = reqparse.RequestParser()
admin_put_cartoon_parser.add_argument('name', type=unicode)
admin_put_cartoon_parser.add_argument('intro', type=unicode)
admin_put_cartoon_parser.add_argument('pub_date', type=unicode)
admin_put_cartoon_parser.add_argument('icon', type=unicode)
admin_put_cartoon_parser.add_argument('video_url', type=unicode)
admin_put_cartoon_parser.add_argument('status', type=unicode)

cartoon_parser = reqparse.RequestParser()
cartoon_parser.add_argument('count', type=int)
cartoon_parser.add_argument('recommend', type=bool)
cartoon_parser.add_argument('visited', type=bool)
cartoon_parser.add_argument('collect', type=bool)

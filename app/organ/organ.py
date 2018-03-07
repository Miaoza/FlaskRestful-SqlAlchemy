# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-22 15:23:17
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-06 11:06:06
from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, marshal

from app import db
from app.auth.auth import *
from model import Organ
from app.user.model import User
from fields import *

organ_bp = Blueprint('organ', __name__)
organ_api = Api(organ_bp)

class Organs(Resource):
    @required_auth
    def get(self):
        args = list_parser.parse_args()
        limit = args["limit"]
        offset = args["offset"]
        organs = Organ.query.order_by(Organ.id.desc()).offset(offset).limit(limit).all()
        for organ in organs:
            user = User.query.get(organ.user_id)
            organ.principal = user
        organs = marshal(organs, organ_fields)
        return jsonify({"code": 0, "data": organs})

    @required_auth
    def post(self):
        args = organ_parser.parse_args()
        name = args['name']
        intro = args['intro']
        address = args['address']
        user_id = args['user_id']
        tel = args['tel']
        remark = args['remark']
        query = Organ.query.filter(Organ.name==name).first()
        if query:
            return jsonify({"code": -1, "message": "机构已存在"})
        query = Organ.query.filter(Organ.user_id==user_id).first()
        if query:
            return jsonify({"code": -1, "message": "该用户已有负责机构"})
        organ = Organ(name=name,intro=intro,address=address,user_id=user_id,tel=tel,remark=remark)
        try:
            db.session.add(organ)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "提交失败"})
        return jsonify({"code": 0, "message": "提交成功"})


class OrganView(Resource):
    @required_auth
    def get(self, organ_id):
        organ = Organ.query.get(organ_id)
        if not organ:
            return jsonify({"code": -1, "message": "获取失败"})
        user = User.query.get(organ.user_id)
        organ.principal = user
        organ = marshal(organ, organ_fields)
        return jsonify({"code": 0, "data": organ})

    def put(self, organ_id):
        args = organ_parser.parse_args()
        name = args['name']
        intro = args['intro']
        address = args['address']
        user_id = args['user_id']
        tel = args['tel']
        remark = args['remark']

        organ = Organ.query.get(organ_id)
        if not organ: 
            return jsonify({"code": -1, "message": "该机构不存在"})
        organ.name = name
        organ.intro = intro
        organ.address = address
        organ.user_id = user_id
        organ.tel = tel
        organ.remark = remark

        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "修改失败"})
        else:
            return jsonify({"code": 0, "message": "修改成功"})

    def delete(self, organ_id):
        organ = Organ.query.get(organ_id)
        if not organ: 
            return jsonify({"code": -1, "message": "该机构不存在"})
        try:
            db.session.delete(organ)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "删除失败"})
        else:
            return jsonify({"code": 0, "message": "删除成功"})

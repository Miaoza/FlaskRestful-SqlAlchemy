# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-23 17:30:40
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-06 11:07:12
from flask import Blueprint, request, jsonify, json
from flask_restful import Resource, Api, marshal
import time
import uuid

from app import db
from app.auth.auth import *
from model import Category,Material,Purchase,Plan
from fields import *
from app.user.model import User

pro_bp = Blueprint('procure', __name__)
pro_api = Api(pro_bp)

class Categorys(Resource):
    @required_auth
    def get(self):
        args = list_parser.parse_args()
        limit = args['limit']
        offset = args['offset']
        cates = Category.query.order_by(Category.id.desc()).offset(offset).limit(limit).all()
        cates = marshal(cates, cate_fields)
        return jsonify({"code": 0, "data": cates})

    @required_auth
    def post(self):
        args = cate_parser.parse_args()
        name = args['name']
        cate = Category(name = name)
        try:
            db.session.add(cate)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "提交失败"})
        else:
            return jsonify({"code": 0, "message": "提交成功"})

class CategroyView(Resource):
    @required_auth
    def put(self, category_id):
        args = cate_parser.parse_args()
        name = args['name']
        cate = Category.query.get(category_id)
        cate.name = name
        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "修改失败"})
        else:
            return jsonify({"code": 0, "message": "修改成功"})

    @required_auth
    def delete(self, category_id):
        cate = Category.query.get(category_id)
        try:
            db.session.delete(cate)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "删除失败"})
        else:
            return jsonify({"code": 0, "message": "删除成功"})

class Materials(Resource):
    @required_auth
    def get(self):
        args = list_parser.parse_args()
        limit = args['limit']
        offset = args['offset']
        mates = Material.query.order_by(Material.id.desc()).limit(limit).offset(offset).all()
        for mate in mates:
            cate = Category.query.get(mate.category_id)
            mate.category = cate
        mates = marshal(mates, mate_fields)
        return jsonify({"code": 0, "data": mates})

    @required_auth
    def post(self):
        args = mate_parser.parse_args()
        name = args['name']
        store = args['store']
        category_id = args['category_id']

        mate = Material(name=name, store=store, category_id=category_id, counts=0)
        try:
            db.session.add(mate)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "添加失败"})
        else:
            return jsonify({"code": 0, "message": "添加成功"})
        

class MaterialView(Resource):
    @required_auth
    def get(self, material_id):
        mate = Material.query.get(material_id)
        category = Category.query.get(mate.category_id)
        mate.category = category

        mate = marshal(mate, mate_fields)
        return jsonify({"code": 0, "data": mate})

    @required_auth
    def put(self, material_id):
        args = mate_parser.parse_args()
        name = args['name']
        store = args['store']
        category_id = args['category_id']
        mate = Material.query.get(material_id)
        if name:
            mate.name = name
        if store or store==0:
            mate.store = store
        if category_id:
            mate.category_id = category_id
        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "修改失败"})
        else:
            return jsonify({"code": 0, "message": "修改成功"})

    @required_auth
    def delete(self, material_id):
        mate = Material.query.get(material_id)
        try:
            db.session.delete(mate)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "删除失败"})
        else:
            return jsonify({"code": 0, "message": "删除成功"})

class Purchases(Resource):
    @required_auth
    def get(self):
        auth = request.authorization
        me = User.verify_auth_token(auth.username)

        args = list_parser.parse_args()
        limit = args['limit']
        offset = args['offset']
        if me.role != 'organ':
            purs = Purchase.query.order_by(Purchase.id.desc()).offset(offset).limit(limit).all()
        else:
            purs = Purchase.query.filter(Purchase.user_id==me.id).order_by(Purchase.id.desc()).offset(offset).limit(limit).all()
        for pur in purs:
            user = User.query.get(pur.user_id)
            pur.user = user
            for mate in pur.materials:
                cate = Category.query.get(mate.category_id)
                mate.category = cate
        purs = marshal(purs, pur_fields)
        return jsonify({"code": 0, "data": purs})

    @required_auth
    def  post(self):
        auth = request.authorization
        me = User.verify_auth_token(auth.username)

        args = pur_parser.parse_args()
        mates = args['materials']
        remark = args['remark']
        create = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        update = create

        pur = Purchase(status='new', create_date=create, update_date=update, remark=remark, user_id=me.id)
        for ma in mates:
            mate = Material.query.get(ma[u'id'])
            mate.counts += int(ma[u'count'])
            pur.materials.append(mate)
        try:
            db.session.add(pur)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "添加失败"})
        else: 
            return jsonify({"code": 0, "message": "添加成功"})


class PurchaseView(Resource):
    @required_auth
    def get(self, purchase_id):
        pur = Purchase.query.get(purchase_id)
        user = User.query.get(pur.user_id)
        pur.user = user
        for mate in pur.materials:
            cate = Category.query.get(mate.category_id)
            mate.category = cate
        pur = marshal(pur, pur_fields)
        return jsonify({"code": 0, "data": pur})

    @required_auth
    def put(self, purchase_id):
        args = pur_parser.parse_args()
        mates = args['materials']
        remark = args['remark']
        update = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        pur = Purchase.query.get(purchase_id)
        pur.materials = mates
        pur.remark = remark
        pur.update = update

        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "修改失败"})
        else:
            return jsonify({"code": 0, "message": "修改成功"})

    @required_auth
    def delete(self, purchase_id):
        pur = Purchase.query.get(purchase_id)
        try:
            db.session.delete(pur)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "删除失败"})
        else:
            return jsonify({"code": 0, "message": "删除成功"})


class Plans(Resource):
    @required_auth
    def get(self):
        args = list_parser.parse_args()
        limit = args['limit']
        offset = args['offset']

        plans = Plan.query.order_by(Plan.id.desc()).limit(limit).offset(offset).all()
        for plan in plans:
            pur = Purchase.query.get(plan.purchase_id)
            user = User.query.get(pur.user_id)
            pur.user = user
            for mate in pur.materials:
                cate = Category.query.get(mate.category_id)
                mate.category = cate
            plan.purchase = pur
        plans = marshal(plans, plan_fields)
        return jsonify({"code": 0, "data": plans})

    @required_auth
    def post(self):
        args = plan_parser.parse_args()
        purchase_id = args['purchase_id']
        create = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        update = create
        status = args['status']
        order = uuid.uuid1()

        purchase = Purchase.query.get(purchase_id)
        purchase.status = status
        purchase.update = update
        plan = Plan(purchase_id=purchase_id, create_date=create, update_date=update, status=status, order=str(order))
        try:
            db.session.add(plan)
            db.session.commit()
        except Exception , e:
            return jsonify({"code": -1, "message": "失败"})
        else:
            return jsonify({"code": 0, "message": "成功"})



class PlanView(Resource):
    @required_auth
    def get(self, plan_id):
        plan = Plan.query.get(plan_id)
        purchase = Purchase.query.get(plan.purchase_id)
        user = User.query.get(purchase.user_id)
        purchase.user = user
        for mate in purchase.materials:
            cate = Category.query.get(mate.category_id)
            mate.category = cate
        plan.purchase = purchase
        plan = marshal(plan, plan_fields)
        return jsonify({"code": 0, "data": plan})

    @required_auth
    def put(self, plan_id):
        args = put_plan_parser.parse_args()
        status = args['status']
        plan = Plan.query.get(plan_id)
        plan.status = status
        try:
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "失败"})
        else:
            return jsonify({"code": 0, "message": "成功"})

    @required_auth
    def delete(self, plan_id):
        plan = Plan.query.get(plan_id)
        try:
            db.session.delete(plan)
            db.session.commit()
        except:
            return jsonify({"code": -1, "message": "删除失败"})
        else:
            return jsonify({"code": 0, "message": "已删除"})


class MaterialsOptions(Resource):
    @required_auth
    def get(self):
        args = mate_options_parser.parse_args()
        material_ids = args['material_ids']
        ids = material_ids[0].split(',')
        mates = []
        for _id in ids:
            mate = Material.query.get(int(_id))
            category = Category.query.get(mate.category_id)
            mate.category = category
            mates.append(mate)
        mates = marshal(mates, mate_fields)
        return jsonify({"code": 0, "data": mates})
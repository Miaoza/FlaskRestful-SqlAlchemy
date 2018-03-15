# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T15:02:57+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:20:49+08:00

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, marshal

from app import db
from app.auth.auth import *
from app.auth.admin_auth import *
from model import Cartoon
from fields import *
# from app.user.model import User

car_bp = Blueprint('cartoon', __name__)
car_api = Api(car_bp)

class AdminCartoons(Resource):
    @required_admin_auth
    def get(self):
        pass

    @required_admin_auth
    def post(self):
        pass

class AdminCartoonView(Resource):
    @required_admin_auth
    def get(self, cartoon_id):
        pass

    @required_admin_auth
    def put(self, cartoon_id):
        pass

    @required_admin_auth
    def delete(self, cartoon_id):
        pass

class Cartoons(Resource):
    @required_auth
    def get(self):
        pass


class CartoonView(Resource):
    @required_auth
    def get(self, cartoon_id):
        pass

    @required_auth
    def put(self, cartoon_id):
        pass

# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T17:06:36+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:40:05+08:00

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, marshal

from app import db
from model import Message
from fields import *
from app.auth.auth import *
from app.auth.admin_auth import *

msg_bp = Blueprint('message', __name__)
msg_api = Api(msg_bp)

class AdminMessages(Resource):
    @required_admin_auth
    def get(self):
        pass

class AdminMessageView(Resource):
    @required_admin_auth
    def delete(self, msg_id):
        pass

class Messages(Resource):
    @required_auth
    def get(self):
        pass

    @required_auth
    def post(self):
        pass

class MessageView(Resource):
    @required_auth
    def get(self, msg_id):
        pass

    @required_auth
    def delete(self, msg_id):
        pass

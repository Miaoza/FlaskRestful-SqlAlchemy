# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T16:18:57+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:20:21+08:00

from flask import request, jsonify
from functools import wraps

from app.admin.model import AdminUser

def required_admin_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username:
            return jsonify({"code": -1, "message": "token错误"})
        me = AdminUser.verify_auth_token(auth.username)
        if not me:
            return jsonify({"code": -1, "message": "token错误"})
        return f(*args, **kwargs)
    return decorated

# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-22 16:19:35
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-22 17:23:48

from flask import request, jsonify
from functools import wraps

from app.user.model import User

def required_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username:
            return jsonify({"code": -1, "message": "token错误"})
        me = User.verify_auth_token(auth.username)
        if not me:
            return jsonify({"code": -1, "message": "token过期"})
        return f(*args, **kwargs)
    return decorated
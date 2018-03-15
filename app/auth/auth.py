# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T16:18:57+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:38:42+08:00

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
            return jsonify({"code": -1, "message": "token错误"})
        return f(*args, **kwargs)
    return decorated

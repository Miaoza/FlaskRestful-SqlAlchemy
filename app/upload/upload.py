# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-07T11:46:32+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T12:26:19+08:00


import os
import uuid
from flask_restful import  Resource, Api
from flask import Blueprint, request, jsonify, url_for, send_file
from werkzeug import SharedDataMiddleware

from app import app

up_bp= Blueprint('upload', __name__)
up_api = Api(up_bp)

UPLOAD_FOLDER = 'uploads/'

app.add_url_rule('/uploads/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  UPLOAD_FOLDER
})

class GetFile(Resource):
    def get(self, filename):
        path = os.path.abspath(os.path.join(UPLOAD_FOLDER, filename))
        return send_file(path)

class Uploads(Resource):
    def post(self):
        file = request.files.get('img')

        if file:
            filename = str(uuid.uuid1())
            try:
                os.makedirs(UPLOAD_FOLDER)
            except OSError:
                if not os.path.isdir(UPLOAD_FOLDER):
                    return jsonify({"code": -1, "message": "上传失败"})
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            path = url_for('uploaded_file', filename=filename)
            return jsonify({"code": 0, "data": {"image_url":path}})

        return jsonify({"code": -1, "message": "上传失败"})

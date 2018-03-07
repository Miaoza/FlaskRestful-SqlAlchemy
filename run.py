# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-18 17:06:26
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-19 16:02:31

from flask_script import Manager

from app import app, db

manager = Manager(app)


if __name__ == '__main__':
    app.debug =True
    app.run()
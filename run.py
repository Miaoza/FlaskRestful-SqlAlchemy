# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T12:15:37+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T12:25:07+08:00


from flask_script import Manager

from app import app, db

manager = Manager(app)


if __name__ == '__main__':
    app.debug =True
    app.run()

# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-18 18:44:19
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-06 11:10:35

from user import *

user_api.add_resource(Login, '/auth/login')
user_api.add_resource(Users, '/users')
user_api.add_resource(UserView, '/users/<int:user_id>')
user_api.add_resource(Me, '/auth/me')
user_api.add_resource(OrganUsers, '/organ/users')

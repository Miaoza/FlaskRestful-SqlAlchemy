# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T12:14:01+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:36:14+08:00


from user import *

user_api.add_resource(Login, '/login')
user_api.add_resource(UsersTable, '/admin/users')
user_api.add_resource(UsersTableView, '/admin/users/<int:user_id>')
user_api.add_resource(Users, '/users')
user_api.add_resource(UserView, '/users/<int:user_id>')
user_api.add_resource(Me, '/me')

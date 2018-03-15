# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T15:58:26+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T16:31:22+08:00

from admin import *

admin_api.add_resource(AdminLogin, '/admin/login')
admin_api.add_resource(AdminUsers, '/admin/admin_users')
admin_api.add_resource(AdminUserView, '/admin/admin_users/<int:user_id>')
admin_api.add_resource(AdminMe, '/admin/me')

# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T11:06:31+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-14T18:23:00+08:00

from cartoon import *

car_api.add_resource(AdminCartoons, '/admin/cartoons')
car_api.add_resource(AdminCartoonView, '/admin/cartoon/<int:cartoon_id>')
car_api.add_resource(Cartoons, '/cartoons')
car_api.add_resource(CartoonView, '/cartoons/<int:cartoon_id>')

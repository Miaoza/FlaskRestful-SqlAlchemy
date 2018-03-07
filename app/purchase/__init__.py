# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-23 17:29:19
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-06 11:09:16

from material import *

pro_api.add_resource(Categorys, '/catalogs/categories')
pro_api.add_resource(CategroyView, '/catalogs/categories/<int:categroy_id>')
pro_api.add_resource(Materials, '/catalogs')
pro_api.add_resource(MaterialView, '/catalogs/<int:material_id>')
pro_api.add_resource(Purchases, '/purchases')
pro_api.add_resource(PurchaseView, '/purchases/<int:purchase_id>')
pro_api.add_resource(Plans, '/plans')
pro_api.add_resource(PlanView, '/plans/<int:plan_id>')

pro_api.add_resource(MaterialsOptions, '/materials/options')
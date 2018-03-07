# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-22 15:22:40
# @Last Modified by:   nianko
# @Last Modified time: 2018-02-06 11:05:26

from organ import *

organ_api.add_resource(Organs, '/orgs')
organ_api.add_resource(OrganView, '/orgs/<int:organ_id>')

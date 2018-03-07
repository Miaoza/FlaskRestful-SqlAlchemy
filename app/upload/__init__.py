# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-20 16:06:22
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-20 16:10:28
# 
from upload import *

up_api.add_resource(Uploads, '/uploads')
up_api.add_resource(GetFile, '/uploads/<filename>')
# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-07T11:46:32+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T12:26:32+08:00


from upload import *

up_api.add_resource(Uploads, '/uploads')
up_api.add_resource(GetFile, '/uploads/<filename>')

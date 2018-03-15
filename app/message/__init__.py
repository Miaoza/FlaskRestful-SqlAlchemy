# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T17:06:11+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T10:55:19+08:00

from message import *

msg_api.add_resource(AdminMessages, '/admin/messages')
msg_api.add_resource(AdminMessageView, '/admin/messages/<int:msg_id>')
msg_api.add_resource(Messages, '/messages')
msg_api.add_resource(MessageView, '/messages/<int:msg_id>')

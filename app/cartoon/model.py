# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-14T15:02:16+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T10:41:57+08:00

from app import db

class Cartoon(db.Model):
    __tablename__ = 'cartoon'
    __table_args__ = {
        "mysql_engine": "InnoDB", # 指定表的引擎,InnoDB（MySQL的数据库引擎之一）
        "mysql_charset": "utf8"   # 指定表的编码格式
    }
    id = db.Column(db.Integer, primary_key=True)          #int 类型
    name = db.Column(db.String(225), nullable=False)      #string类型
    intro = db.Column(db.Text)                            #文本类型
    pub_date = db.Column(db.String(225))
    icon = db.Column(db.String(250))
    video_url = db.Column(db.String(250))
    count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.String(225))
    status = db.Column(db.Integer, default=1) #1 正常 0 禁止播放 -1 不显示

    #repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<Cartoon %r>' % self.id

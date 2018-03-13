# -*- coding: utf-8 -*-
# @Author: nianko
# @Date:   2018-01-18 17:06:35
# @Last Modified by:   nianko
# @Last Modified time: 2018-01-18 18:35:27

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woshiwo@127.0.0.1/dva_db?charset=utf8'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woshiwo@127.0.0.1/dva_db?charset=utf8'

class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woshiwo@127.0.0.1/dva_db?charset=utf8'


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': ProductionConfig,
}

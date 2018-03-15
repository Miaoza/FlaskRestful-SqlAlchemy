# -*- coding: utf-8 -*-
# @Author: Nianko <nianko>
# @Date:   2018-03-15T12:14:57+08:00
# @Last modified by:   nianko
# @Last modified time: 2018-03-15T12:24:31+08:00


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

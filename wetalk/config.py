"""
    wetalk.config
    ~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""


class BaseConfig(object):
    """ 配置基类 """
    DEBUG = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """ 开发环境配置 """
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/development.db'


class ProductionConfig(BaseConfig):
    """ 成产环境配置 """
    DEBUG = False


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/testing.db'


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

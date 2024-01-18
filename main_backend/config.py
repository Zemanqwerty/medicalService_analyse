import os
from starlette.config import Config as Cfg


basedir = os.path.abspath(os.path.dirname('app.py'))
config = Cfg('.env')


class Config(object):

    DEBUG = False
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.urandom(32)
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI', cast=str, default='')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Sergey:1234@195.140.147.111:5432/med'
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'somesecretkey-jwt'


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
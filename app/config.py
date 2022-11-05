import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://newUser:vasiaVasile2020@35.192.103.217/leszcz_base'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

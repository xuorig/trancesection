import os
_basepath = os.path.dirname(__file__)

# configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basepath, 'trancesection.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

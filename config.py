import os
_basepath = os.path.dirname(__file__)

# configuration
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'trancesection.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
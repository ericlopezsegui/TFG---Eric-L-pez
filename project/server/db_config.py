import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY' or 'MY_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:root@localhost:3306/Database_torneig')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:root@localhost:3306/Database_torneig')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:root@localhost:3306/Database_torneig')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:root@localhost:3306/Database_torneig')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
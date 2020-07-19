class Config:
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False

import os


class ProductionConfig:
    ENV = "production"
    DEBUG = False
    SECRET_KEY = os.urandom(24)    

class DevelopmentConfig(ProductionConfig):
    ENV = "development"
    DEBUG = True

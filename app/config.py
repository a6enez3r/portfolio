import os

class ProductionConfig:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(256)

class DevelopmentConfig:
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False
    SECRET_KEY = os.urandom(256)

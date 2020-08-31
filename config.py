
class ProductionConfig:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'This is secret'

class DevelopmentConfig:
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False
    SECRET_KEY = 'This is secret'

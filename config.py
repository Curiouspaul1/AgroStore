import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(24)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = 'true'.lower()
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_URI') or f"mysql://root:{'dbpassword'}@localhost/farmspace_dev"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_URI') or f"mysql://root:{'dbpassword'}@localhost/farmspace_test"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_URI') or f"mysql://root:{'dbpassword'}@localhost/farmspace"

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default' : DevelopmentConfig
}
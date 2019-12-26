from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_mail import Mail,Message
from flask_script import Manager
from config import config

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
manager = Manager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
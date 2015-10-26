from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('../instance/config.py')

    config[config_name].init_app(app)
    
    mail.init_app(app)
    db.init_app(app)
    
    from main import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    return app

from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)

    # loafd config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # setup db
    db.init_app(app)

    # import blueprints
    from home.views import home_app
    from pet.views import pet_app

    # register blueprints
    app.register_blueprint(home_app)
    app.register_blueprint(pet_app)

    return app

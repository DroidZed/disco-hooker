from flask import Flask
from src.config.env import Env

from werkzeug.utils import import_string


api_blueprints = ["hook_bp"]


def create_app():
    app = Flask(__name__)

    # Register blueprints
    for bp_name in api_blueprints:
        print("Registering bp: %s" % bp_name)
        bp = import_string("src.routes.%s:bp" % (bp_name))
        app.register_blueprint(bp)

    return app

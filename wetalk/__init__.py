# flake8: noqa
"""
    wetalk
    ~~~~~~

    :copyright: (c) 2017 by protream.
"""
import os
import json

from flask_migrate import Migrate, MigrateCommand
from werkzeug import import_string

from .app import Flask
from .config import configs
from .models import db


APP_DIR = os.path.dirname(__file__)


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)


def register_bluprints(app):
    blueprints = [
        'wetalk.api.base.bp',
        'wetalk.handlers.front.bp'
    ]
    for bp in blueprints:
        app.register_blueprint(import_string(bp))


def register_error_hanlers(app):
    pass


def register_context_processors(app):

    @app.context_processor
    def manifest():
        manifest = {}
        try:
            with open(APP_DIR + '/static/dist/manifest.json', 'r') as f:
                manifest = json.load(f)
        except Exception:
            print(
                'no manifest file found at ' + APP_DIR + '/static/dist/manifest.json'
            )
        return dict(manifest=manifest)


def create_app(config):
    app = Flask(__name__)

    if isinstance(config, dict):
        app.config.update(config)
    else:
        app.config.from_object(configs.get(config, None))

    register_extensions(app)
    register_bluprints(app)
    register_error_hanlers(app)
    register_context_processors(app)

    return app

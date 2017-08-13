# flake8: noqa
"""
    wetalk
    ~~~~~~

    :copyright: (c) 2017 by protream.
"""
import os
import json

from flask import jsonify
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
    # 原来的方式会导致循环引用
    from .handlers import front
    from .api import api
    app.register_blueprint(front)
    app.register_blueprint(api)


def register_error_hanlers(app):
    """ 因为使用接口通信，出错时也返回 JSON 数据
    """

    @app.errorhandler(404)
    def not_found(error):
        return jsonify('Not Found'), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify('Server Error'), 500



def register_context_processors(app):

    @app.context_processor
    def manifest():
        """ minifest 文件就是 webpack 打包正常的一个依赖清单，
            原文件是 JSON 格式的，这里将它加载为 dict 并注入
            到 Jinja 环境中
        """
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
    """ App 工厂"""
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

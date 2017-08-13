"""
    wetalk.api
    ~~~~~~~~~~~~~~~

    :license: LICENSE_NAME, see LICENSE for more details.
"""

from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from . import front  # noqa

"""
    wetalk.api.base
    ~~~~~~~~~~~~~~~

    :license: LICENSE_NAME, see LICENSE for more details.
"""

from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

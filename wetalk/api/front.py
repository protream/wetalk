"""
    wetalk.api.front
    ~~~~~~~~~~~~~~~~

    :license: LICENSE_NAME, see LICENSE for more details.
"""

from flask import jsonify

from .base import bp


@bp.route('/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello Vue!')

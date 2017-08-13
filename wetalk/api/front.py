"""
    wetalk.api.front
    ~~~~~~~~~~~~~~~~

    :license: LICENSE_NAME, see LICENSE for more details.
"""

from flask import jsonify

from . import api


@api.route('/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello Vue!')

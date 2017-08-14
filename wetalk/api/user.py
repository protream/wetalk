from flask import jsonify, session

from wetalk.models import User
from wetalk.forms import RegisterForm, LoginForm
from . import api


@api.route('/user', methods=['POST'])
def register():
    form = RegisterForm.create_from_json()
    if not form.validate():
        return jsonify(form.errors), 422
    user = form.create_user()
    return jsonify(user.to_dict()), 201


@api.route('/user/session', methods=['POST'])
def login():
    form = LoginForm.create_from_json()
    if not form.validate():
        return jsonify(form.errors), 422
    user = User.query.filter_by(email=form.email.data).first()
    session['id'] = user.id
    return jsonify(user.to_dict())


@api.route('/user/session', methods=['DELETE'])
def logout():
    uid = session.pop('id', None)
    if not uid:
        return jsonify('error'), 400
    return jsonify({}), 204


@api.route('/user/me', methods=['GET'])
def current_user():
    uid = session.get('id', None)
    if not uid:
        return jsonify({})
    user = User.query.get(uid)
    return jsonify(user.to_dict())

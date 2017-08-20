from flask import jsonify, session, request
from wetalk.models import Post
from wetalk.forms import PostForm
from . import api

@api.route('/posts', methods=['POST'])
def create_post():
	if not session.get('id', ''):
		return jsonify(message='未登录'), 403
	form = PostForm.create_from_json()
	if not form.validate():
		return jsonify(form.errors), 422
	post = form.create_post()
	return jsonify(post.to_dict()), 201
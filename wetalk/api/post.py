from flask import jsonify, session, request
from wetalk.models import Post, Topic
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


@api.route('/posts', methods=['GET'])
def get_posts():
    print(request.args)
    offset = request.args.get('offset', 0, type=int)
    topic = request.args.get('topic', '全部话题')
    limit = 5
    q = Post.query
    if topic != '全部话题':
        topic = Topic.query.filter_by(name=topic).first()
        if topic:
            print('topic')
            q = q.filter(Post.topic_id == topic.id)
    q = q.order_by(Post.created_at.desc())
    posts = q.offset(offset).limit(limit)
    data = [post.to_dict() for post in posts]
    if len(data) < limit:
        offset = 0
    else:
        offset = offset + limit
    return jsonify(data=data, offset=offset)

from flask import jsonify
from wetalk.models import Topic
from . import api


@api.route('/topics', methods=['GET'])
def all_topics():
	topics = Topic.query.all()
	return jsonify([topic.to_dict() for topic in topics])
#!/usr/bin/env python3

from flask import Flask, request
from flask_restful import Api, Resource, marshal_with, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"

#This only needs enable for populate the sql schema 
# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name the video is required.", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required.", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required.", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument('name', type=str)
video_update_args.add_argument('views', type=str)
video_update_args.add_argument('likes', type=str)

# videos = {}
# def abort_if_video_id_doesnt_exist(video_id):
# 	if video_id not in videos:
# 		abort(404, mesage="Could not find the video.")

# def abort_if_video_id_does_exist(video_id):
# 	if video_id in videos:
# 		abort(409, message="Video ID is existing.")

resource_fields = {
	'id' : fields.Integer,
	'name': fields.String,
	'view': fields.Integer,
	'likes': fields.Integer
}

class Video(Resource):
	@marshal_with(resource_fields)
	def get(self, video_id):
		# abort_if_video_id_doesnt_exist(video_id)
		result = VideoModel.query.filter_by(id=video_id).first( )
		if not result:
			abort(404, message=f"Could not find the video with {video_id}")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message=f"Video id {video_id} is already exists.")
		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(video)
		db.session.commit()
		return video, 201
	
	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		
		print(result)
		if not result:
			abort(404, message=f"Video id {video_id} doesn't exist, cannot update.")
		
		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()
		return result

	@marshal_with(resource_fields)
	def delete(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			VideoModel.query.filter_by(id=video_id).delete()
		db.session.commit()
		return '', 204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)

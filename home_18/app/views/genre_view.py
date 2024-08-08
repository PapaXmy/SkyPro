from flask_restx import Resource, Namespace
from app.dao.model.genre import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_genres()
        return genres_schema.dump(all_genres), 200


@genre_ns.route("/<int:uid>")
class GenreView(Resource):
    def get(self, uid: int):
        genre = genre_service.get_genre(uid)
        return genre_schema.dump(genre), 200

from flask_restx import Resource, Namespace
from flask import request
from app.dao.model.movie import MovieSchema
from app.implemented import movie_service


movie_ns = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        filters = {"director_id": director, "genre_id": genre, "year": year}
        all_movies = movie_service.get_movies(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        movie_json = request.json
        movie_service.create_movie(movie_json)
        return "", 201


@movie_ns.route("/<int:uid>")
class MovieView(Resource):
    def get(self, uid: int):
        movie = movie_service.get_movie(uid)
        return movie_schema.dump(movie), 200

    def put(self, uid: int):
        movie_json = request.json
        movie_json["id"] = uid

        movie_service.update_movie(movie_json)
        return "", 204

    def delete(self, uid: int):
        movie = movie_service.delete_movie(uid)
        return "", 204

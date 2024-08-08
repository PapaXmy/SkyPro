from flask_restx import Resource, Namespace
from app.dao.model.director import DirectorSchema
from app.implemented import director_service

director_ns = Namespace("directors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_directors()
        return directors_schema.dump(all_directors), 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid: int):
        director = director_service.get_director(uid)
        return director_schema.dump(director), 200

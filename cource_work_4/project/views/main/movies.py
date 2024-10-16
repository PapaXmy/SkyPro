from flask_restx import Namespace, Resource
from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser, status_parser

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.doc('get_movie')
    @api.expect(page_parser, status_parser)
    @api.expect(movie)
    @api.marshal_with(movie, as_list=True, code=200, description='ok')
    def get(self):
        """
        Получение всех фильмов.
        """
        args = {**page_parser.parse_args(), **status_parser.parse_args()}
        return movie_service.get_all(**args)


@api.route('/<int:movie_id>')
class MovieView(Resource):
    @api.response(404, 'Не найден')
    @api.marshal_with(movie, code=200, description='ok')
    def get(self, movie_id: int):
        """
        Получение фильма по id.
        """
        return movie_service.get_item(movie_id)

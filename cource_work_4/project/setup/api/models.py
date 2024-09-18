from flask_restx import fields, Model
from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100)
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'trailer': fields.String(requored=True),
    'year': fields.Integer(required=True),
    'rating': fields.Integer(required=True),
    'genre_id': fields.Integer(required=True),
    'director_id': fields.Integer(required=True)
})

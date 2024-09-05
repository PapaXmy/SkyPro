from flask import request
from flask_restx import Resource, Namespace
from ..implemented import user_service

user_ns = Namespace("users")

@user_ns.route('/')
class UsersView(Resource):

    def post(self):
        user_json = request.json
        user_service.create_user(user_json)
        return "Пользователь добавлен!", 201
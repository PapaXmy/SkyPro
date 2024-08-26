import requests
from flask_restx import Resource, Namespace
from ..implemented import user_service

user_ns = Namespace("users")

@user_ns.route('/')
class UsersView(Resource):

    def post(self):
        user_json = requests.json
        user_service.create_user(user_json)
        return "", 201
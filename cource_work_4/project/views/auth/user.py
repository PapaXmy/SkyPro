from flask_restx import Namespace, Resource
from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser
from flask import request
from project.exceptions import ItemNotFound
from project.decorators import auth_required

api = Namespace('users')


@api.route('/')
class UsersView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(user, as_list=True, code=200, description='ok')
    @auth_required
    def get(self):
        """
        Получение всех пользователей.
        """
        args = {**page_parser.parse_args()}
        return user_service.get_all(**args)


@api.route('/<int:user_id>')
class UserView(Resource):
    @api.response(404, 'Не найден')
    @api.marshal_with(user, code=200, description='ok')
    @auth_required
    def get(self, user_id: int):
        """
        Получение пользователя по id.
        """
        return user_service.get_item(user_id)

    @api.response(404, 'Не найден')
    @api.marshal_with(user, code=200, description='ok')
    @auth_required
    def patch(self, user_id):
        """
        Изменение информации пользователя.
        """
        user_json = request.json
        user_json['id'] = user_id

        return user_service.update_user(user_json)

    @api.response(404, 'Не найден')
    @api.marshal_with(user, code=200, description='ok')
    @auth_required
    def put(self, user_id):
        """
        Изменение пароля пользователя.
        """
        user_json = request.json
        user_json['id'] = user_id

        password_1 = user_json.get('password_1')
        password_2 = user_json.get('password_2')

        if not password_1 or password_2:
            raise ItemNotFound('Обязательно ввести два пароля для обновления!')

        if password_1 != password_2:
            return {'message': 'Пароли не совпадают.'}, 400

        return user_service.update_user(user_id, password_1)

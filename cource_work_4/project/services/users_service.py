from typing import Optional
from project.exceptions import ItemNotFound
from project.models import User
from project.dao.main import UsersDAO
# import base64
# import hashlib
# from project.config import BaseConfig
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(
            f'Пользователь с порядковым номером {pk} не существует!')

    def get_all(
            self, page: Optional[int] = None, status: Optional[str] = None
    ) -> list[User]:
        return self.dao.get_all(status=status, page=page)

    # def get_hash_password(self, password: str):
    #     return base64.b64decode(hashlib.pbkdf2_hmac(
    #         'sha256',
    #         password.encode('utf-8'),
    #         BaseConfig.PWD_HASH_SALT,
    #         BaseConfig.PWD_HASH_ITERATIONS
    #     ))

    def create_user(self, data):
        password = data.get('password')
        if password:
            data['password'] = generate_password_hash(data.get('password'))
        else:
            raise ItemNotFound(
                'При создании пользователя нужно обязательно указать пароль!')
        return self.dao.create_user(data)

    def update_user(self, user_data, new_password=None):
        uid = user_data.get('id')
        user = self.get_item(uid)

        if user:
            if new_password is None:
                user.email = user_data.get('email')
                user.password = generate_password_hash(
                    user_data.get('password'))
                user.name = user_data.get('name')
                user.surname = user_data.get('surname')
                user.favorite_genre = user_data.get('favorite_genre')

                self.dao.update_user(user)
            else:
                user.password = generate_password_hash(new_password)
                self.dao.update_user(user)

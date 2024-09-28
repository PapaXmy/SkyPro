from flask import request, abort
from project.config import BaseConfig
import jwt
from project.exceptions import Unauthorized


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        user_data = request.headers['Authorization']
        token = user_data.split('Bearer ')[-1]

        if not token:
            raise Unauthorized('Токен не найден!')

        try:
            jwt.decode(
                token, BaseConfig.SECRET_KEY, algorithms=[
                    BaseConfig.JWT_ALGORITHM])

        except jwt.ExpiredSignatureError:
            raise Unauthorized('Токен истек!')
        except jwt.InvalidTokenError:
            raise Unauthorized('Неверный токен!')

        return func(*args, **kwargs)

    return wrapper

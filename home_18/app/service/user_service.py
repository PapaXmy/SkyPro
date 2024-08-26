from app.dao.user_dao import UserDAO
from app.config import Config
import hashlib
import hmac
import base64


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_users(self):
        return self.user_dao.get_all_users()

    def get_one_user(self, uid):
        return self.user_dao.get_user(uid)

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            Config.PWD_HASH_SALT,
            Config.PDW_HASH_ITERATIONS,
        ).decode("utf-8", "ignore")

    def check_password(self, hashed_password, password) -> bool:
        return hmac.compare_digest(
            base64.b64encode(
                hashlib.pbkdf2_hmac(
                    "sha256",
                    password.encode(),
                    Config.PWD_HASH_SALT,
                    Config.PWD_HASH_ITERATIONS,
                )
            )
        )

    def create_user(self, data):
        data["password"] = self.get_hash(data.get("password"))
        return self.user_dao.create_user(data)

    def update_user(self, data):
        uid = data.get("id")
        user = self.get_one_user(uid)

        if user:
            user.username = data.get("username")
            user.password = data.get("password")
            user.role = data.get("role")

            self.user_dao.update_user()
        else:
            print(f"Пользователь с id {uid} не найден!")

    def delete_user(self, uid):
        user = self.get_one_user(uid)

        if user:
            self.user_dao.delete_user(uid)
        else:
            print(f"Пользователь с id {uid} не найден!")

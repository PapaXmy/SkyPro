from flask_restx import Resource, Namespace
from flask import request, abort
from app.dao.model.user import UserSchema
from app.dao.model.user import Users
from ..setup_db import db
from ..constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, secret, algo
import hashlib
import datetime
import calendar
import jwt

auth_ns = Namespace("auth")
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        auth_json = request.json
        username = auth_json.get("username", None)
        password = auth_json.get("password", None)

        if None in [username, password]:
            abort(400)

        user = db.session.query(Users).filter(Users.username == username).first()

        if user is None:
            return {"error": "Неверные учетные данные"}, 401

        hashed_password = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"),PWD_HASH_SALT, PWD_HASH_ITERATIONS
        )

        if hashed_password != user.password:
            return {"error": "Неверные учетные данные"}, 401

        user_data = {"username": user.username, "role": user.role}
        min30 = datetime.detetime.utcnow() + datetime.timedelta(minutes=30)
        user_data["exp"] = calendar.timemg(min30.timetuple())
        access_token = jwt.encode(user_data, secret, algorithm=algo)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        user_data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(user_data, secret, algorithm=algo)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def put(self):
        auth_json = request.json
        refresh_token = auth_json.get("refresh_token")

        if refresh_token is None:
            abort(400)

        try:
            user_data = jwt.decode(jwt=refresh_token, key=secret, algorithm=[algo])
        except Exception as e:
            abort(400)

        username = user_data.get("username")

        user = db.session.query(Users).filter(Users.username == username).first()

        user_data = {"username": user.username, "role": user.role}
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        user_data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(user_data, secret, algorithm=algo)

        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        user_data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(user_data, secret, algorithm=algo)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens
# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from ..dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self):
        return self.movie_dao.get_all_movies()

    def get_movie(self, mid):
        return self.movie_dao.get_movie(mid)

    def create_movie(self, data):
        return self.movie_dao.create_movie(data)

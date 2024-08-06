from ..dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genre(self, gid):
        return self.genre_dao.get_one_genre(gid)

    def get_genres(self):
        return self.genre_dao.get_all_genres()

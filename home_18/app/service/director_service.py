from ..dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_director(self, did):
        return self.director_dao.get_director(did)

    def get_directors(self):
        return self.director_dao.get_all_diretors()

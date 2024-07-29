from .model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genress(self):
        return self.session.query(Genre).all()

    def get_director(self, gid):
        return self.session.query(Genre).get(gid)

from .model.director import Director

# from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_diretors(self):
        return self.session.query(Director).all()

    def get_director(self, did):
        return self.session.query(Director).get(did)

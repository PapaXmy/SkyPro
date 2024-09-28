from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User
from werkzeug.exceptions import NotFound
# from sqlalchemy.orm import Query
from typing import List, Optional, TypeVar
from project.setup.db.models import Base
from sqlalchemy import desc

T = TypeVar('T', bound=Base)


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(
            self, page: Optional[int] = None, status: Optional[str] = None
    ) -> List[T]:
        stmt = self._db_session.query(self.__model__)
        if status == 'new':
            try:
                stmt = stmt.order_by(desc(self.__model__.year))
            except NotFound:
                return []

        if page:
            try:
                return stmt.paginate(
                    page=page, per_page=self._items_per_page, error_out=False
                ).items
            except NotFound:
                return []
        return stmt.all()


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create_user(self, user_data):
        user = User(**user_data)

        self._db_session.add(user)
        self._db_session.commit()

        return user

    def update_user(self, user):

        self._db_session.add(user)
        self._db_session.commit()

        return user

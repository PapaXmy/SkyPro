from typing import Generic, List, Optional, TypeVar

from flask import current_app
# from sqlalchemy.orm import Query
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        # return self._db_session.query(self.__model__).get(pk)
        return self._db_session.get(self.__model__, pk)

    def get_all(self, page: Optional[int] = None) -> List[T]:
        stmt = self._db_session.query(self.__model__)
        if page:
            try:
                return stmt.paginate(
                    page=page, per_page=self._items_per_page, error_out=False
                ).items
            except NotFound:
                return []
        return stmt.all()

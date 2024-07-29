# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from .model.movie import Movies
from .model.director import Director
from .model.genre import Genre


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movies).all()

    def get_movie(self, mid):
        return self.session.query(Movies).get(mid)

    def get_all_movie_by_director(self, director):
        return (
            self.session.query(Movies.title)
            .join(Director)
            .filter(Director.name == director)
        ).all()

    def get_all_movie_by_genre(self, genre):
        return (
            self.session.query(Movies.title)
            .join(Genre)
            .filter(Genre.name == genre)
            .all()
        )

    def get_all_movie_by_year(self, year):
        return self.session.query(Movies).filter(Movies.year == year).all()

    def create_movie(self, data):
        movie = Movies(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_movie(self, mid):
        movie = self.get_movie(mid)

        self.session.delete(movie)
        self.commit()

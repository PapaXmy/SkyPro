from sqlalchemy import Column, String, Integer

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    description = Column(String())
    trailer = Column(String())
    year = Column(Integer())
    rating = Column(Integer())
    genre_id = Column(Integer())
    director_id = Column(Integer())


class User(models.Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(), unique=True, nullable=False)
    password = Column(String())
    name = Column(String())
    surname = Column(String())
    favorite_genre = Column(String())

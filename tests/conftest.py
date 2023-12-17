import pytest
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO
from dao.model.genre import Genre
from dao.genre import GenreDAO


@pytest.fixture()
def director_dao_fixture():
    director_dao = DirectorDAO(None)
    director = Director(id=1, name='Adam First')
    another_director = Director(id=2, name='Donald Love')
    director_dao.get_one = MagicMock(return_value=director)
    director_dao.get_all = MagicMock(return_value=[director, another_director])
    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.delete = MagicMock(return_value='Deleted')
    director_dao.update = MagicMock(return_value='Updated')
    return director_dao


# noinspection DuplicatedCode
@pytest.fixture()
def genre_dao_fixture():
    genre_dao = GenreDAO(None)
    genre = Genre(id=1, name='Comedy')
    another_genre = Director(id=2, name='Drama')
    genre_dao.get_one = MagicMock(return_value=genre)
    genre_dao.get_all = MagicMock(return_value=[genre, another_genre])
    genre_dao.create = MagicMock(return_value=Genre(id=2))
    genre_dao.delete = MagicMock(return_value='Deleted')
    genre_dao.update = MagicMock(return_value='Updated')
    return genre_dao

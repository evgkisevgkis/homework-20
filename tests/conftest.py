import pytest
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO


@pytest.fixture()
def director_dao_fixture():
    director_dao = DirectorDAO(None)
    director = Director(id=1, name='Adam First')
    another_director = Director(id=2, name='Donald Love')
    director_dao.get_one = MagicMock(return_value=director)
    director_dao.get_all = MagicMock(return_value=[director, another_director])
    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.delete = MagicMock(return_value='Deleted')
    director_dao.update = MagicMock(return_value='Created')
    return director_dao

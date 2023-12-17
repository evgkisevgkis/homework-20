import pytest
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        assert self.director_service.get_one(1).id == 1
        assert self.director_service.get_one(1).name == 'Adam First'

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) == 2

    def test_create(self):
        assert self.director_service.create(2).id == 2

    def test_delete(self):
        assert self.director_service.delete(2) is None

    def test_update(self):
        assert self.director_service.update(2) is 'Updated'

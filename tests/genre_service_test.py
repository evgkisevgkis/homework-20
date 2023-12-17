import pytest
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao_fixture):
        self.genre_service = GenreService(dao=genre_dao_fixture)

    def test_get_one(self):
        assert self.genre_service.get_one(1).id == 1
        assert self.genre_service.get_one(1).name == 'Comedy'

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) == 2

    def test_create(self):
        assert self.genre_service.create(2).id == 2

    def test_delete(self):
        assert self.genre_service.delete(2) is None

    def test_update(self):
        assert self.genre_service.update(2) is 'Updated'

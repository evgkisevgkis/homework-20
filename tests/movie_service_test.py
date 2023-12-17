import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_get_one(self):
        assert self.movie_service.get_one(1).id == 1
        assert self.movie_service.get_one(1).title == 'Max Payne'
        assert self.movie_service.get_one(1).description == 'About policeman'
        assert self.movie_service.get_one(1).year == 2010
        assert self.movie_service.get_one(1).rating == 4.9

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) == 2

    def test_create(self):
        assert self.movie_service.create(2).id == 2

    def test_delete(self):
        assert self.movie_service.delete(2) is None

    def test_update(self):
        assert self.movie_service.update(2) is 'Updated'

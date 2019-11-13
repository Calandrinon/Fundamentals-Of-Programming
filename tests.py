from service import MovieService
from repository import MovieRepository
from validation import *
from domain import Movie

class TestMovieService:
    
    def __init__(self):
        self.repository = MovieRepository()
        self.validator = MovieValidator()
        self.service = MovieService(self.repository, self.validator)
        
    def __assert_movies(self, movie1, movie2):
        assert(movie1.get_movieID() == movie2.get_movieID())
        assert(movie1.get_title() == movie2.get_title())
        assert(movie1.get_description() == movie2.get_description())
        assert(movie1.get_genre() == movie2.get_genre())
        
        
    def __test_add_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        expected_result = [Movie(185, "Shining", "A good movie", "horror")]
        movies = self.repository.get_list_of_movies()
        assert(len(expected_result) == len(movies))
        self.__assert_movies(expected_result[0], movies[0])
        
    def run_tests(self):
        self.__test_add_movie()
        
class Tests:
    def __init__(self):
        self.test1 = TestMovieService()
        
    
    def run_tests(self):
        self.test1.run_tests()
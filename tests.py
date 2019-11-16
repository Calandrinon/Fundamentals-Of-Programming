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
        
        
    def __test_add_movie__valid_movie__list_with_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        expected_result = [Movie(185, "Shining", "A good movie", "horror")]
        movies = self.repository.get_list_of_movies()
        assert(len(expected_result) == len(movies))
        self.__assert_movies(expected_result[-1], movies[-1])
    
    
    def __test_remove_by_id__valid_movie__list_without_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        self.service.remove_movie_by_id(185)
        assert(len(self.repository.get_list_of_movies()) == 0)
        
        
    def __test_remove_by_genre__valid_movies__list_without_movies(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        self.service.remove_movies_by_genre("horror")
        assert(len(self.repository.get_list_of_movies()) == 0)
        
        
    def __test_update_movie_id__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        self.service.update_movie_id(185, 247)
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_movieID() == 247)
    
    
    def __test_update_movie_title__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        self.service.update_movie_title(185, "Cool")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_title() == "Cool")
    
    
    def __test_update_movie_description__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        self.service.update_movie_description(185, "A nice movie")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_description() == "A nice movie")
        
        
    def __test_update_movie_genre__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        self.service.update_movie_genre(185, "Haw roar")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_genre() == "Haw roar")
        
    
    def run_tests(self):
        self.__test_add_movie__valid_movie__list_with_movie()
        self.__test_remove_by_id__valid_movie__list_without_movie()
        self.__test_remove_by_genre__valid_movies__list_without_movies()
        self.__test_update_movie_id__valid_movie__list_with_updated_movie()
        self.__test_update_movie_title__valid_movie__list_with_updated_movie()
        self.__test_update_movie_description__valid_movie__list_with_updated_movie()
        self.__test_update_movie_genre__valid_movie__list_with_updated_movie()
        
        
class Tests:
    def __init__(self):
        self.test_movie_service = TestMovieService()
        
    
    def run_tests(self):
        self.test_movie_service.run_tests()
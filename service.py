from domain import *
from repository import MovieRepository
from validation import MovieValidator

class MovieService:

    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    
    def add_movie(self, movieID, title, description, genre):
        """
        Adds a movie to the movie repository.
        
        Input:
            - movieID: a unique integer
            - title: a string
            - description: a string
            - genre: a string
        """
        
        movie = Movie(movieID, title, description, genre)
        self.__validator.validate_movie(movie)
        
        self.__repository.add_to_list(movie)
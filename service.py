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
    
        
    def get_list_of_movies(self):
        """
        Gets the list of movies from the repository.
        """
        
        return self.__repository.get_list_of_movies()
    
    
    def remove_movie_by_id(self, ID):
        """
        Removes the movie with the id "ID"
        """
        
        list_of_movies = self.__repository.get_list_of_movies()
        new_list_of_movies = []
        
        for movie in list_of_movies:
            if movie.get_movieID() != ID:
                new_list_of_movies.append(movie)
                
        self.__repository.set_list_of_movies(new_list_of_movies)
        
        
    def remove_movies_by_genre(self, genre):
        """
        Removes all movies of a specific genre
        """
        
        list_of_movies = self.__repository.get_list_of_movies()
        new_list_of_movies = []
        
        for movie in list_of_movies:
            if movie.get_genre() != genre:
                new_list_of_movies.append(movie)
                
        self.__repository.set_list_of_movies(new_list_of_movies)
        
        
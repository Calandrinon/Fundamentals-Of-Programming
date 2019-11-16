from exceptions import *

class MovieValidator:
    def __init__(self):
        pass

    def validate_movie(self, movie):
        """
        Validates the ID and checks if there is already an equal ID in the list
        
        Input:
            - movie - an instance of the Movie class
            
        """
        
        ID = movie.get_movieID()
        if not (isinstance(ID, int) and ID >= 0):
            raise MovieError("The movie ID should be a positive integer")
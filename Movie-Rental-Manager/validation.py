from exceptions import *

class MovieValidator:
    def __init__(self):
        pass

    def validate_movie(self, movie):
        """
        Validates the ID of a movie
        
        Input:
            - movie - an instance of the Movie class
            
        """
        
        ID = movie.get_movieID()
        if not (isinstance(ID, int) and ID >= 0):
            raise MovieError("The movie ID should be a positive integer")
        
        
class ClientValidator:
    def __init__(self):
        pass

    def validate_client(self, client):
        """
        Validates the ID of a client
        
        Input:
            - client - an instance of the Client class
            
        """
        
        ID = client.get_clientID()
        if not (isinstance(ID, int) and ID >= 0):
            raise ClientError("The client ID should be a positive integer")
        
        
class RentalValidator:
    def __init__(self):
        pass
    
    def validate_rental(self, rental):
        ID = rental.get_rentalID()
        if not (isinstance(ID, int) and ID >= 0):
            raise RentalError("The rental ID should be a positive integer")
    
        
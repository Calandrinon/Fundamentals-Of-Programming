class Movie:

    def __init__(self, movieID, title, description, genre):
        self.__movieID = movieID
        self.__title = title
        self.__description = description
        self.__genre = genre
        self.rented = False


    def get_movieID(self):
        return self.__movieID


    def set_movieID(self, new_movieID):
        self.__movieID = new_movieID


    def get_title(self):
        return self.__title


    def set_title(self, new_title):
        self.__title = new_title


    def get_description(self):
        return self.__description


    def set_description(self, new_description):
        self.__description = new_description


    def get_genre(self):
        return self.__genre


    def set_genre(self, new_genre):
        self.__genre = new_genre


    def __eq__(self, other_movie):
        if not isinstance(other_movie, Movie):
            raise MovieError("Can't compare a Movie instance with an instance of {}", type(other_movie).__name__)
        
        return self.get_movieID() == other_movie.get_movieID() and self.get_title() == other_movie.get_title() and self.get_description() == other_movie.get_description() and self.get_genre() == other_movie.get_genre()
    
    
    def __str__(self):
        return self.get_title()
    

    def print_movie(self):
        print("[", self.__movieID, ",", self.__title, ",", self.__description, ",", self.__genre, "]")


class Client:

    def __init__(self, clientID, name):
        self.__clientID = clientID
        self.__name = name
        self.can_rent = True
        

    def get_clientID(self):
        return self.__clientID
        

    def set_clientID(self, new_clientID):
        self.__clientID = new_clientID


    def get_name(self):
        return self.__name


    def set_name(self, new_name):
        self.__name = new_name


    def __eq__(self, other_client):
        if not isinstance(other_client, Client):
            raise ClientError("Can't compare a Client instance with an instance of {}", type(other_client).__name__)
        
        return self.get_clientID() == other_client.get_clientID() and self.get_name() == other_client.get_name()
    
    
    def __str__(self):
        return self.get_name()

    def print_client(self):
        print("[", self.__clientID, ",", self.__name, "]")


class Rental:

    def __init__(self, rentalID, movieID, clientID, rented_date, due_date, returned_date):
        self.__rentalID = rentalID
        self.__movieID = movieID
        self.__clientID = clientID
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date

    def get_rentalID(self):
        return self.__rentalID

    def set_rentalID(self, new_rentalID):
        self.__rentalID = new_rentalID

    def get_movieID(self):
        return self.__movieID

    def set_movieID(self, new_movieID):
        self.__movieID = new_movieID

    def get_clientID(self):
        return self.__clientID

    def set_clientID(self, new_clientID):
        self.__clientID = new_clientID

    def get_rented_date(self):
        return self.__rented_date

    def set_rented_date(self, new_rented_date):
        self.__rented_date = new_rented_date

    def get_due_date(self):
        return self.__due_date

    def set_due_date(self, new_due_date):
        self.__due_date = new_due_date

    def get_returned_date(self):
        return self.__returned_date

    def set_returned_date(self, new_returned_date):
        self.__returned_date = new_returned_date

    def __eq__(self, other_rental):
        if not isinstance(other_rental, Rental):
            raise RentalError("Can't compare a Rental instance with an instance of {}", type(other_rental).__name__)
        
        return self.get_rentalID() == other_rental.get_rentalID() and self.get_movieID() == other_rental.get_movieID() and self.get_clientID() == other_rental.get_clientID() and self.get_rented_date() == other_rental.get_rented_date() and self.get_due_date() == other_rental.get_due_date() and self.get_returned_date() == other_rental.get_returned_date()
        

    def print_rental(self):
        print("[", self.__rentalID, ",", self.__movieID, ",", self.__clientID,
              ",", self.__rented_date, ",", self.__due_date, ",", 
              self.__returned_date, "]")
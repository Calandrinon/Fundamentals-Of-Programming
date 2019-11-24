from domain import *
from repository import *
from validation import *
import random
import string
from datetime import date

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
        
        if self.__repository.is_id_used(movieID):
            return
        
        movie = Movie(movieID, title, description, genre)
        self.__validator.validate_movie(movie)
        self.__repository.rented_id_dictionary[movieID] = 0
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
                
        self.__repository.delete_id(ID)
                
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
            else:
                self.__repository.delete_id(movie.get_movieID())
                  
        self.__repository.set_list_of_movies(new_list_of_movies)
        
        
    def update_movie_id(self, old_id, new_id):
        """
        Updates the id of the movie with the id "old_id".
        """
        
        list_of_movies = self.__repository.get_list_of_movies()
        new_list_of_movies = []
        
        for movie in list_of_movies:
            if movie.get_movieID() == old_id:
                self.__repository.delete_id(old_id)
                movie.set_movieID(new_id)
                self.__repository.create_id(new_id)
            new_list_of_movies.append(movie)
                
        self.__repository.set_list_of_movies(new_list_of_movies)
        
        
    def update_movie_title(self, id, new_title):
        """
        Updates the title of the movie with the id "id".
        """
        
        list_of_movies = self.__repository.get_list_of_movies()
        new_list_of_movies = []
        
        for movie in list_of_movies:
            if movie.get_movieID() == id:
                movie.set_title(new_title)
            new_list_of_movies.append(movie)
                
        self.__repository.set_list_of_movies(new_list_of_movies)
        
        
    def update_movie_description(self, id, new_description):
        """
        Updates the description of the movie with the id "id".
        """
        
        list_of_movies = self.__repository.get_list_of_movies()
        new_list_of_movies = []
        
        for movie in list_of_movies:
            if movie.get_movieID() == id:
                movie.set_description(new_description)
            new_list_of_movies.append(movie)
                
        self.__repository.set_list_of_movies(new_list_of_movies)
        
        
    def update_movie_genre(self, id, new_genre):
        """
        Updates the genre of the movie with the id "id".
        """
        
        list_of_movies = self.__repository.get_list_of_movies()
        new_list_of_movies = []
        
        for movie in list_of_movies:
            if movie.get_movieID() == id:
                movie.set_genre(new_genre)
            new_list_of_movies.append(movie)
                
        self.__repository.set_list_of_movies(new_list_of_movies)
        
        
    def search_movie_by_id(self, id):
        """
        Searches for the movie with the id "id" and returns it.
        """
        list_of_movies = self.__repository.get_list_of_movies()
        
        for movie in list_of_movies:
            if movie.get_movieID() == id:
                return movie
            
        raise MovieError("The movie with the ID {} has not been found!".format(id))
        
        
    def search_movie_by_title(self, title):
        """
        Searches for the movies with the title pattern "title" and returns them
        as a list.
        """
        
        list_of_movies = self.__repository.get_list_of_movies()
        result = []
        title = str(title)
        title = title.lower()
        
        for movie in list_of_movies:
            other_title = movie.get_title().lower()
            
            if title in other_title:
                result.append(movie)
                
        if len(result) == 0:
            raise MovieError("The movie with the title {} has not been found!".format(title))
        
        return result
        
        
    def search_movie_by_description(self, description):
        """
        Searches for the movies with the description pattern "description" and returns them
        as a list.
        """
        list_of_movies = self.__repository.get_list_of_movies()
        result = []
        description = str(description)
        description = description.lower()
        
        for movie in list_of_movies:
            other_description = movie.get_description().lower() 
            
            if description in other_description:
                result.append(movie)
                   
        if len(result) == 0:
            raise MovieError("The movie with the description {} has not been found!".format(description))    
        
        return result
        
        
    def search_movie_by_genre(self, genre):
        """
        Searches for the movies with the genre pattern "genre" and returns them
        as a list.
        """

        list_of_movies = self.__repository.get_list_of_movies()
        result = []
        genre = str(genre)
        genre = genre.lower()
        
        for movie in list_of_movies:
            other_genre = movie.get_genre().lower()
            
            if genre in other_genre:
                result.append(movie)
                
        if len(result) == 0:
            raise MovieError("The movie with the genre {} has not been found!".format(genre))
        
        return result
        
        
    def generate_entries(self, number_of_entries):
        def generate_string():
            length = random.randint(5, 12)
            random_string = ""
            
            for generated_character in range(0, length):
                random_string += random.choice(string.ascii_letters)
            
            return random_string
        
        for entry in range(0, number_of_entries):
            random_title = generate_string()
            random_description = generate_string()
            random_genre = generate_string()
            random_movie = Movie(entry, random_title, random_description, random_genre)
            self.__repository.add_to_list(random_movie)
            
            
class ClientService:

    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator
    
    def add_client(self, clientID, name):
        """
        Adds a client to the client repository.
        
        Input:
            - clientID: a unique integer
            - name: a string
        """
        
        if self.__repository.is_id_used(clientID):
            return
        
        client = Client(clientID, name)
        self.__validator.validate_client(client)
        self.__repository.can_id_rent[clientID] = True
        self.__repository.add_to_list(client)
    
        
    def get_list_of_clients(self):
        """
        Gets the list of clients from the repository.
        """
        
        return self.__repository.get_list_of_clients()
    
    
    def remove_client_by_id(self, ID):
        """
        Removes the client with the id "ID"
        """
        
        list_of_clients = self.__repository.get_list_of_clients()
        new_list_of_clients = []
        
        for client in list_of_clients:
            if client.get_clientID() != ID:
                new_list_of_clients.append(client)
                
        self.__repository.delete_id(ID)
                
        self.__repository.set_list_of_clients(new_list_of_clients)
        
        
    def update_client_id(self, old_id, new_id):
        """
        Updates the id of the client with the id "old_id".
        """
        
        list_of_clients = self.__repository.get_list_of_clients()
        new_list_of_clients = []
        
        for client in list_of_clients:
            if client.get_clientID() == old_id:
                self.__repository.delete_id(old_id)
                client.set_clientID(new_id)
                self.__repository.create_id(new_id)
            new_list_of_clients.append(client)
                
        self.__repository.set_list_of_clients(new_list_of_clients)
        
        
    def update_client_name(self, id, new_name):
        """
        Updates the name of the client with the id "id".
        """
        
        list_of_clients = self.__repository.get_list_of_clients()
        new_list_of_clients = []
        
        for client in list_of_clients:
            if client.get_clientID() == id:
                client.set_name(new_name)
            new_list_of_clients.append(client)
                
        self.__repository.set_list_of_clients(new_list_of_clients)
        
        
    def search_client_by_name(self, name):
        """
        Searches for the clients with the name pattern "name" and returns them
        as a list.
        """
        
        list_of_clients = self.__repository.get_list_of_clients()
        result = []
        name = str(name)
        name = name.lower()
        
        for client in list_of_clients:
            other_name = client.get_name().lower()
            
            if name in other_name:
                result.append(client)
                
        if len(result) == 0:
            raise ClientError("The client with the name {} has not been found!".format(name))
        
        return result
    
    
    def search_client_by_id(self, id):
        """
        Searches for the client with the id "id" and returns it.
        """
        list_of_clients = self.__repository.get_list_of_clients()
        
        for client in list_of_clients:
            if client.get_clientID() == id:
                return client
            
        raise ClientError("The client with the ID {} has not been found!".format(id))
        
        
    def generate_entries(self):    
        number_of_entries = random.randint(10, 20)
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown",
        "Davis", "Miller", "Wilson", "Moore", "Taylor"]

        first_names = ["Oliver", "George", "Harry", "Noah", "Jack", "Charlie",
        "Leo", "Jacob", "Freddie", "Alfie", "Olivia", "Amelia", "Isla", "Ava",
        "Emily", "Sophia", "Grace", "Mia", "Poppy", "Ella"]
        
        for entry in range(0, number_of_entries):
            random_name = first_names[random.randint(0, len(first_names) - 1)] + " " + last_names[random.randint(0, len(last_names) - 1)]
            random_client = Client(entry, random_name)
            self.__repository.add_to_list(random_client)
            

class RentalService:
    
    def __init__(self, rental_repository, validator, client_repository, movie_repository):
        self.__repository = rental_repository
        self.__validator = validator
        self.__client_repository = client_repository
        self.__client_service = ClientService(self.__client_repository, ClientValidator())
        self.__movie_repository = movie_repository
        self.__movie_service = MovieService(movie_repository, MovieValidator())
        
    def create_rental(self, rentalID, movieID, clientID, rented_date, due_date): 
        
        """
        Adds a new rental to the rental repository.
        """
        
        rental = Rental(rentalID, movieID, clientID, rented_date, due_date, date(1, 1, 1))
        self.__validator.validate_rental(rental)
        
        try:
            if self.__movie_repository.rented_id_dictionary[movieID] == 1:
                raise RentalError("The movie has already been rented!")
        except KeyError:
            self.__movie_repository.rented_id_dictionary[movieID] = 0
        
        can_rent = True
        client_list = self.__client_repository.get_list_of_clients()
        for client in client_list:
            if client.get_clientID() == clientID:
                try:
                    can_rent = self.__client_repository.can_id_rent[clientID]
                except:
                    self.__client_repository.can_id_rent[clientID] = True
                break
        
        if can_rent == True:
            self.__repository.add_to_list(rental)
            self.__movie_repository.rented_id_dictionary[movieID] = 1
        else:
            raise RentalError("The client has passed the due date for past rentals!")
        
        
    def delete_rental(self, rentalID):
        
        """
        Deletes the rental with the ID "rentalID" from the rental repository.
        """
        
        rental_list = self.__repository.get_list_of_rentals()
        new_rental_list = []
        
        for rental in rental_list:
            if rental.get_rentalID() == rentalID:
                rental.set_returned_date(date.today())
                d0 = rental.get_due_date()
                d1 = date.today()
                
                if (d0.year < d1.year) or (d0.month < d1.month) or (d0.day < d1.day):
                    self.__client_repository.can_id_rent[rental.get_clientID()] = False
            else:
                new_rental_list.append(rental)
                
        self.__repository.set_list_of_rentals(new_rental_list)
        
    
    def get_list_of_rentals(self):
        """
        Gets the list of rentals from the repository.
        """
        
        return self.__repository.get_list_of_rentals()
    
    
    def create_rented_movies_statistics(self):
        """
        Iterates through the list of rentals, computes the number of days they were rented
        and returns a list with the movies sorted in descending order of the number of days
        they were rented.
        """
        
        rentals = self.get_list_of_rentals()
        movie_statistics = {} 
        result = []
        
        for rental in rentals:
            movie_statistics[rental.get_movieID()] = 0
        
        for rental in rentals:
            d0 = rental.get_rented_date()
            d1 = date.today()
            days = (d1 - d0).days
            movie_statistics[rental.get_movieID()] += days  
            
        for movie_id in movie_statistics:
            result.append([movie_id, movie_statistics[movie_id]])
            
        result.sort(key=lambda movie: movie[1], reverse = True)
        
        movies = []
        for movie in result:
            movies.append([self.__movie_service.search_movie_by_id(movie[0]), movie[1]])
        
        return movies
        
    
    def create_active_clients_statistics(self):
        """
        Provides the list of clients, sorted in descending order of the number
        of movie rental days they have (e.g. having 2 rented movies for 3 days 
        each counts as 2 x 3 = 6 days).
        """
        
        rentals = self.get_list_of_rentals()
        client_statistics = {} 
        result = []
        
        for rental in rentals:
            client_statistics[rental.get_clientID()] = 0
        
        for rental in rentals:
            d0 = rental.get_rented_date()
            d1 = date.today()
            days = (d1 - d0).days
            client_statistics[rental.get_clientID()] += days  
            
        for client_id in client_statistics:
            result.append([client_id, client_statistics[client_id]])
            
        result.sort(key=lambda client: client[1], reverse = True)
        
        clients = []
        for client in result:
            clients.append([self.__client_service.search_client_by_id(client[0]), client[1]])
        
        return clients
    
    
    def create_late_rentals_statistics(self):
        """
        Provides all the movies that are currently rented, for which the due date for return has
        passed, sorted in descending order of the number of days of delay.
        """
        
        rentals = self.get_list_of_rentals()
        movie_statistics = {} 
        result = []
        
        for rental in rentals:
            movie_statistics[rental.get_movieID()] = 0
        
        for rental in rentals:
            d1 = rental.get_due_date()
            d0 = date.today()
            days = (d1 - d0).days
            
            if days < 0:
                movie_statistics[rental.get_movieID()] += days  
            
            
        for movie_id in movie_statistics:
            if movie_statistics[movie_id] != 0:
                result.append([movie_id, movie_statistics[movie_id]])
            
        result.sort(key=lambda movie: movie[1], reverse = True)
        
        movies = []
        for movie in result:
            movies.append([self.__movie_service.search_movie_by_id(movie[0]), movie[1]])
        
        return movies
    
    
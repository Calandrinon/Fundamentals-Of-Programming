from domain import *
from repository import *
from validation import *
import random
import string

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
                movie.set_movieID(new_id)
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
                client.set_clientID(new_id)
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
        
        
    def generate_entries(self):    
        number_of_entries = random.randint(5, 20)
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown",
        "Davis", "Miller", "Wilson", "Moore", "Taylor"]

        first_names = ["Oliver", "George", "Harry", "Noah", "Jack", "Charlie",
        "Leo", "Jacob", "Freddie", "Alfie", "Olivia", "Amelia", "Isla", "Ava",
        "Emily", "Sophia", "Grace", "Mia", "Poppy", "Ella"]
        
        for entry in range(0, number_of_entries):
            random_name = first_names[random.randint(0, len(first_names) - 1)] + " " + last_names[random.randint(0, len(last_names) - 1)]
            random_client = Client(entry, random_name)
            self.__repository.add_to_list(random_client)
            
            
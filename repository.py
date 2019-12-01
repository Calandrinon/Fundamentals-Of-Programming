from exceptions import *

class MovieRepository:
    def __init__(self):
        self.__list_of_movies = []
        self.__id_dictionary = {}
        self.rented_id_dictionary = {}
        
    
    def set_as_rented(self, id):
        self.rented_id_dictionary[id] = 1
    
    
    def set_as_available(self, id):    
        self.rented_id_dictionary[id] = 0
        
        
    def delete_id(self, id):
        self.__id_dictionary[id] = 0
    
    
    def create_id(self, id):
        self.__id_dictionary[id] = 1
    
    
    def is_id_used(self, id):
        try:
            if self.__id_dictionary[id] == 0:
                return False
            raise MovieError("There is already a movie with that ID!")
        except KeyError:
            return False
        
        
    def add_to_list(self, movie):
        self.__list_of_movies.append(movie)
        self.create_id(movie.get_movieID())
        
        
    def get_list_of_movies(self):
        return self.__list_of_movies
    
    
    def set_list_of_movies(self, new_list):
        self.__list_of_movies[:] = new_list 

        
class ClientRepository:
    def __init__(self):
        self.__list_of_clients = []
        self.__id_dictionary = {}
        self.can_id_rent = {}
    
    
    def delete_id(self, id):
        self.__id_dictionary[id] = 0
    
    
    def create_id(self, id):
        self.__id_dictionary[id] = 1
    
    
    def is_id_used(self, id):
        try:
            if self.__id_dictionary[id] == 0:
                return False
            raise ClientError("There is already a client with that ID!")
        except KeyError:
            return False
    
        
    def add_to_list(self, client):
        self.__list_of_clients.append(client)
        self.create_id(client.get_clientID())
    
        
    def get_list_of_clients(self):
        return self.__list_of_clients
    
    
    def set_list_of_clients(self, new_list):
        self.__list_of_clients[:] = new_list 
      
        
class RentalRepository:
    def __init__(self):
        self.__list_of_rentals = []
        self.__movie_rented_days = {}
    
    
    def add_to_list(self, rental):
        self.__list_of_rentals.append(rental)
        
        
    def get_list_of_rentals(self):
        return self.__list_of_rentals
    
    
    def set_list_of_rentals(self, new_list):
        self.__list_of_rentals[:] = new_list
        
        
class UndoRepository:
    def __init__(self):
        self.__list_of_operations = []
        self.__redo_stack = []
        self.__pointer = 0
        self.__redo_pointer = 0
    
    
    def get_pointer(self):
        return self.__pointer
    
    
    def get_redo_pointer(self):
        return self.__redo_pointer
    
    
    def decrement_pointer(self):
        self.__pointer -= 1
    
    
    def add_to_list(self, operation):
        self.__list_of_operations.append(operation)
        self.__pointer += 1
        
    
    def add_to_redo_stack(self, operation):    
        self.__redo_stack.append(operation)
        self.__redo_pointer += 1
        
        
    def get_list(self):
        return self.__list_of_operations
    
    
    def get_redo_stack(self):
        return self.__redo_stack
        
        
    def get_last_operation(self):
        if self.__pointer == 0:
            raise UndoError("All the operations have been undone!")
            return None
            
        return self.__list_of_operations[self.__pointer - 1]
        self.__pointer -= 1
        
        
    def get_redo_operation(self):
        if self.__redo_pointer == 0:
            raise UndoError("Can't redo!")
            return None
            
        return self.__redo_stack[self.__redo_pointer - 1]
        self.__redo_pointer -= 1
        

    def remove_last_operation_from_stack(self):
        if len(self.__list_of_operations) > 0:
            del self.__list_of_operations[self.__pointer - 1]
            self.__pointer -= 1
            
    
    def remove_last_operation_from_redo_stack(self):
        if len(self.__redo_stack) > 0:
            del self.__redo_stack[self.__redo_pointer - 1]
            self.__redo_pointer -= 1
        
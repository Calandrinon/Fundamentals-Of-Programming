from service import MovieService
from exceptions import MovieError

class UI:
    def __init__(self, movie_service, client_service):
        self.__movie_service = movie_service
        self.__client_service = client_service
        

    def __print_menu(self):
        print("0. Exit")
        print("1. Add a movie")
        print("2. List movies")
        print("3. Remove a movie by ID")
        print("4. Remove a movie by genre")
        print("5. Update the ID of a movie")
        print("6. Update the title of a movie")
        print("7. Update the description of a movie")
        print("8. Update the genre of a movie")
        print("9. Add a client")
        print("10. List clients")
        print("11. Remove a client by ID")
        print("12. Update the ID of a client")
        print("13. Update the name of a client")
        print("\n"*5)

        
    def __check_movie_list(func):
        def wrapper(self, *args):
            if len(self.__movie_service.get_list_of_movies()) == 0:
                print("There are no movies in the list!\n")
                return
                
            func(self, *args)
                
        return wrapper
        
    
    def __add_movie(self):
        id = int(input("Enter the ID: "))
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        genre = input("Enter the genre: ")

        self.__movie_service.add_movie(id, title, description, genre)


    @__check_movie_list
    def __list_movies(self):
        list_of_movies = self.__movie_service.get_list_of_movies()
        
        for movie in list_of_movies:
            movie.print_movie()
            
        print("\n")


    @__check_movie_list
    def __remove_movie_by_id(self):
        id = int(input("Enter the ID: "))
        self.__movie_service.remove_movie_by_id(id)


    @__check_movie_list
    def __remove_movies_by_genre(self):
        genre = input("Enter the genre: ")
        self.__movie_service.remove_movies_by_genre(genre) 


    @__check_movie_list
    def __update_movie_id(self):
        old_id = int(input("Enter the old ID: "))
        new_id = int(input("Enter the new ID: "))
        self.__movie_service.update_movie_id(old_id, new_id)


    @__check_movie_list
    def __update_movie_title(self):
        id = int(input("Enter the ID: "))
        new_title = input("Enter the title: ")
        self.__movie_service.update_movie_title(id, new_title)


    @__check_movie_list
    def __update_movie_description(self):
        id = int(input("Enter the ID: "))
        new_description = input("Enter the description: ")
        self.__movie_service.update_movie_description(id, new_description)


    @__check_movie_list
    def __update_movie_genre(self):
        id = int(input("Enter the ID: "))
        new_genre = input("Enter the genre: ")
        self.__movie_service.update_movie_genre(id, new_genre)


    def __check_client_list(func):
        def wrapper(self, *args):
            if len(self.__client_service.get_list_of_clients()) == 0:
                print("There are no clients in the list!\n")
                return
                
            func(self, *args)
                
        return wrapper
        
    
    def __add_client(self):
        id = int(input("Enter the ID: "))
        name = input("Enter the name: ")

        self.__client_service.add_client(id, name)


    @__check_client_list
    def __list_clients(self):
        list_of_clients = self.__client_service.get_list_of_clients()
        
        for client in list_of_clients:
            client.print_client()
            
        print("\n")


    @__check_client_list
    def __remove_client_by_id(self):
        id = int(input("Enter the ID: "))
        self.__client_service.remove_client_by_id(id)


    @__check_client_list
    def __update_client_id(self):
        old_id = int(input("Enter the old ID: "))
        new_id = int(input("Enter the new ID: "))
        self.__client_service.update_client_id(old_id, new_id)


    @__check_client_list
    def __update_client_name(self):
        id = int(input("Enter the ID: "))
        new_name = input("Enter the name: ")
        self.__client_service.update_client_name(id, new_name)


    def clear_screen(self):
        print("\n"*100)
        

    def main(self):

        functions = [self.__add_movie, self.__list_movies, 
                     self.__remove_movie_by_id, self.__remove_movies_by_genre,
                     self.__update_movie_id, self.__update_movie_title,
                     self.__update_movie_description, self.__update_movie_genre, 
                     self.__add_client, self.__list_clients, 
                     self.__remove_client_by_id, self.__update_client_id,
                     self.__update_client_name]
        
        self.__movie_service.generate_entries(10)
        self.__client_service.generate_entries()
        self.clear_screen()
        
        while True:
            self.__print_menu()
            option = input("Enter an option: ")
            self.clear_screen()
            
            try:
                option = int(option)
            except ValueError as v:
                print("ValueError: "+str(v))
                continue
            
            if option < 1 or option > len(functions):
                if option == 0:
                    return
                print("The option should be a number between 1 and {}".format(len(functions)))
                continue
            
            try:
                functions[option-1]()
            except ValueError as e:
                print("ValueError: " + str(e))
            except MovieError as me:
                print("MovieError: " + str(me))
            except ClientError as ce:
                print("ClientError: " + str(ce))
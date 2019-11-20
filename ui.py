from service import *
from exceptions import *
from datetime import date 

class UI:
    def __init__(self, movie_service, client_service, rental_service):
        self.__movie_service = movie_service
        self.__client_service = client_service
        self.__rental_service = rental_service
        

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
        print("14. Create a rental")
        print("15. List rentals")
        print("16. Return a rented movie")
        print("17. Search a movie by ID")
        print("18. Search a movie by title")
        print("19. Search a movie by description")
        print("20. Search a movie by genre")
        print("21. Search a client by ID")
        print("22. Search a client by name")
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
        
        
    def __create_rental(self):
        rentalID = len(self.__rental_service.get_list_of_rentals())
        movieID = int(input("Enter the ID of the movie: "))
        clientID = int(input("Enter the ID of the client: "))
        
        rented_date = date.today()
        due_day = int(input("Enter the day of the rental's due date: "))
        due_month = int(input("Enter the month of the rental's due date: "))
        due_year = int(input("Enter the year of the rental's due date: "))
        due_date = date(due_year, due_month, due_day)
        
        self.__rental_service.create_rental(rentalID, movieID, clientID, 
                                            rented_date, due_date)
    
    
    def __list_rentals(self):
        if len(self.__rental_service.get_list_of_rentals()) == 0:
            print("There are no rentals in the list!")
            return
        
        rentals = self.__rental_service.get_list_of_rentals()
        
        for rental in rentals:
            rental.print_rental()

        print("\n"*5)
 
    
    def __delete_rental(self):
        if len(self.__rental_service.get_list_of_rentals()) == 0:
            print("There are no rentals in the list!")
            return
        
        rentalID = int(input("Enter the ID of the rental that will be deleted: "))
        self.__rental_service.delete_rental(rentalID)
    
    
    def __search_movie_by_id(self):
        id = int(input("Enter the ID of the movie: "))
        
        movie = self.__movie_service.search_movie_by_id(id)
        movie.print_movie()


    def __search_movie_by_title(self):
        title = input("Enter the title of the movie: ")
        
        movies = self.__movie_service.search_movie_by_title(title)
        
        for movie in movies:
            movie.print_movie()
        

    def __search_movie_by_description(self):
        description = input("Enter the description of the movie: ")
        
        movies = self.__movie_service.search_movie_by_description(description)
        
        for movie in movies:
            movie.print_movie()


    def __search_movie_by_genre(self):
        genre = input("Enter the genre of the movie: ")
        
        movies = self.__movie_service.search_movie_by_genre(genre)
        
        for movie in movies:
            movie.print_movie()


    def __search_client_by_id(self):
        id = int(input("Enter the ID of the client: "))
        
        client = self.__client_service.search_client_by_id(id)
        client.print_client()


    def __search_client_by_name(self):
        name = input("Enter the name of the client: ")
        
        clients = self.__client_service.search_client_by_name(name)
        
        for client in clients:
            client.print_client()


    def main(self):

        functions = [self.__add_movie, self.__list_movies, 
                     self.__remove_movie_by_id, self.__remove_movies_by_genre,
                     self.__update_movie_id, self.__update_movie_title,
                     self.__update_movie_description, self.__update_movie_genre, 
                     self.__add_client, self.__list_clients, 
                     self.__remove_client_by_id, self.__update_client_id,
                     self.__update_client_name, self.__create_rental,
                     self.__list_rentals, self.__delete_rental,
                     self.__search_movie_by_id, self.__search_movie_by_title,
                     self.__search_movie_by_description, 
                     self.__search_movie_by_genre, self.__search_client_by_id,
                     self.__search_client_by_name]
        
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
            except RentalError as re:
                print("RentalError: " + str(re))
            
                
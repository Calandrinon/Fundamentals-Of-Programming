from service import MovieService
from exceptions import MovieError

class UI:
    def __init__(self, movie_service):
        self.__movie_service = movie_service


    def __print_menu(self):
        print("1. Add a movie")
        print("2. List movies")
        print("3. Remove a movie by ID")
        print("4. Remove a movie by genre")
        """
        print("4. Remove a client")
        print("5. Update a movie")
        print("6. Update a client")
        print("7. List movies")
        print("8. List clients")
        """
        print("\n"*5)


    def __add_movie(self):
        id = int(input("Enter the ID: "))
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        genre = input("Enter the genre: ")

        self.__movie_service.add_movie(id, title, description, genre)


    def __list_movies(self):
        list_of_movies = self.__movie_service.get_list_of_movies()
        
        if len(list_of_movies) == 0:
            print("There are no movies in the list!\n")
            return
        
        for movie in list_of_movies:
            movie.print_movie()
            
        print("\n")


    def __remove_movie_by_id(self):
        if len(self.__movie_service.get_list_of_movies()) == 0:
            print("There are no movies in the list!\n")
            return
        
        id = int(input("Enter the ID: "))
        
        self.__movie_service.remove_movie_by_id(id)


    def __remove_movies_by_genre(self):
        if len(self.__movie_service.get_list_of_movies()) == 0:
            print("There are no movies in the list!\n")
            return
        
        genre = input("Enter the genre: ")
        
        self.__movie_service.remove_movies_by_genre(genre) 


    def main(self):

        functions = [self.__add_movie, self.__list_movies, 
                     self.__remove_movie_by_id, self.__remove_movies_by_genre]
        
        while True:
            self.__print_menu()
            option = input("Enter an option: ")
            
            try:
                option = int(option)
            except ValueError as v:
                print("ValueError: "+str(v))
                continue
            
            if option < 1 or option > len(functions):
                print("The option should be a number between 1 and {}".format(len(functions)))
                continue
            
            try:
                functions[option-1]()
            except ValueError as e:
                print("ValueError: " + str(e))
            except MovieError as me:
                print("MovieError: " + str(me))
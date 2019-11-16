class MovieRepository:
    def __init__(self):
        self.__list_of_movies = []
        
    def add_to_list(self, movie):
        self.__list_of_movies.append(movie)
        
    def get_list_of_movies(self):
        return self.__list_of_movies
    
    def set_list_of_movies(self, new_list):
        self.__list_of_movies[:] = new_list 
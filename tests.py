from service import *
from repository import *
from validation import *
from domain import Movie

class TestMovieService:
    
    def __init__(self):
        self.repository = MovieRepository()
        self.validator = MovieValidator()
        self.service = MovieService(self.repository, self.validator)
    
        
    def __assert_movies(self, movie1, movie2):
        assert(movie1.get_movieID() == movie2.get_movieID())
        assert(movie1.get_title() == movie2.get_title())
        assert(movie1.get_description() == movie2.get_description())
        assert(movie1.get_genre() == movie2.get_genre())
        
        
    def __test_add_movie__valid_movie__list_with_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
        expected_result = [Movie(185, "Shining", "A good movie", "horror")]
        movies = self.repository.get_list_of_movies()
        assert(len(expected_result) == len(movies))
        self.__assert_movies(expected_result[-1], movies[-1])
    
    
    def __test_remove_by_id__valid_movie__list_without_movie(self):
        self.repository.set_list_of_movies([])
        self.service.add_movie(186, "Shining", "A good movie", "horror")
        self.service.remove_movie_by_id(186)
        assert(len(self.repository.get_list_of_movies()) == 0)
        
        
    def __test_remove_by_genre__valid_movies__list_without_movies(self):
        self.repository.set_list_of_movies([])
        self.service.add_movie(156, "Shining", "A good movie", "horror")
        self.service.remove_movies_by_genre("horror")
        assert(len(self.repository.get_list_of_movies()) == 0)
        
        
    def __test_update_movie_id__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(166, "Shining", "A good movie", "horror")
        self.service.update_movie_id(166, 247)
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_movieID() == 247)
    
    
    def __test_update_movie_title__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(182, "Shining", "A good movie", "horror")
        self.service.update_movie_title(182, "Cool")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_title() == "Cool")
    
    
    def __test_update_movie_description__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(181, "Shining", "A good movie", "horror")
        self.service.update_movie_description(181, "A nice movie")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_description() == "A nice movie")
        
        
    def __test_update_movie_genre__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(180, "Shining", "A good movie", "horror")
        self.service.update_movie_genre(180, "Haw roar")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_genre() == "Haw roar")
        
    
    def run_tests(self):
        self.__test_add_movie__valid_movie__list_with_movie()
        self.__test_remove_by_id__valid_movie__list_without_movie()
        self.__test_remove_by_genre__valid_movies__list_without_movies()
        self.__test_update_movie_id__valid_movie__list_with_updated_movie()
        self.__test_update_movie_title__valid_movie__list_with_updated_movie()
        self.__test_update_movie_description__valid_movie__list_with_updated_movie()
        self.__test_update_movie_genre__valid_movie__list_with_updated_movie()


class TestClientService:
    
    def __init__(self):
        self.repository = ClientRepository()
        self.validator = ClientValidator()
        self.service = ClientService(self.repository, self.validator)
    
        
    def __assert_clients(self, client1, client2):
        assert(client1.get_clientID() == client2.get_clientID())
        assert(client1.get_name() == client2.get_name())

        
    def __test_add_client__valid_client__list_with_client(self):
        self.service.add_client(12, "John")
        expected_result = [Client(12, "John")]
        clients = self.repository.get_list_of_clients()
        assert(len(expected_result) == len(clients))
        self.__assert_clients(expected_result[-1], clients[-1])
    
    
    def __test_remove_by_id__valid_client__list_without_client(self):
        self.repository.set_list_of_clients([])
        self.service.add_client(13, "John")
        self.service.remove_client_by_id(13)
        assert(len(self.repository.get_list_of_clients()) == 0)
        
        
    def __test_update_client_id__valid_client__list_with_updated_client(self):
        self.service.add_client(14, "John")
        self.service.update_client_id(14, 24)
        clients = self.repository.get_list_of_clients() 
        assert(clients[-1].get_clientID() == 24)
    
    
    def __test_update_client_name__valid_client__list_with_updated_client(self):
        self.service.add_client(13, "James")
        self.service.update_client_name(13, "Jack")
        clients = self.repository.get_list_of_clients() 
        assert(clients[-1].get_name() == "Jack")
    
    
    def run_tests(self):
        self.__test_add_client__valid_client__list_with_client()
        self.__test_remove_by_id__valid_client__list_without_client()
        self.__test_update_client_id__valid_client__list_with_updated_client()
        self.__test_update_client_name__valid_client__list_with_updated_client()
        
        
class TestRentalService:
    
    def __init__(self):
        self.movie_repository = MovieRepository()
        self.client_repository = ClientRepository()
        self.client_repository.add_to_list(Client(5, "John"))
        self.repository = RentalRepository()
        self.validator = RentalValidator()
        self.service = RentalService(self.repository, self.validator, 
                                     self.client_repository, self.movie_repository)    
    
    
    def __assert_rentals(self, rental1, rental2):
        assert(rental1.get_rentalID() == rental2.get_rentalID())
        assert(rental1.get_movieID() == rental2.get_movieID())
        assert(rental1.get_clientID() == rental2.get_clientID())
        assert(rental1.get_rented_date() == rental2.get_rented_date())
        assert(rental1.get_due_date() == rental2.get_due_date())
        assert(rental1.get_returned_date() == rental2.get_returned_date())
    
    
    def __test_create_rental__valid_rental__list_with_rentals(self):
        self.service.create_rental(5, 1, 10, date.today(), date(2019, 12, 22))
        expected_result = [Rental(5, 1, 10, date.today(), date(2019, 12, 22), date(1, 1, 1))]
        rentals = self.repository.get_list_of_rentals()
        assert(len(expected_result) == len(rentals))
        rentals[-1].print_rental()
        expected_result[-1].print_rental()
        self.__assert_rentals(expected_result[-1], rentals[-1])
        
        
    def __test_delete_rental__valid_rental__list_with_rentals(self):
        self.service.delete_rental(5)
        rentals = self.repository.get_list_of_rentals()
        assert(len(rentals) == 0)
    
    
    def run_tests(self):
        self.__test_create_rental__valid_rental__list_with_rentals()
        self.__test_delete_rental__valid_rental__list_with_rentals()
        
        
class Tests:
    
    def __init__(self):
        self.test_movie_service = TestMovieService()
        self.test_client_service = TestClientService()
        self.test_rental_service = TestRentalService()
        
        
    def run_tests(self):
        self.test_movie_service.run_tests()
        self.test_client_service.run_tests()
        self.test_rental_service.run_tests()
        
        
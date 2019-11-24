from service import *
from repository import *
from validation import *
from domain import Movie
import unittest

class TestMovieService(unittest.TestCase):
    
    def __init__(self):
        self.repository = MovieRepository()
        self.validator = MovieValidator()
        self.service = MovieService(self.repository, self.validator)
    
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.repository = MovieRepository()
        self.validator = MovieValidator()
        self.service = MovieService(self.repository, self.validator)
        
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
        
    def test_add_movie__valid_movie__list_with_movie(self):
        self.service.add_movie(185, "Shining", "A good movie", "horror")
      
        expected_result = [Movie(185, "Shining", "A good movie", "horror")]
        movies = self.repository.get_list_of_movies()
        
        assert(len(expected_result) == len(movies))
        assert(expected_result[-1] == movies[-1])
      
    
    def test_remove_by_id__valid_movie__list_without_movie(self):
        self.repository.set_list_of_movies([])
        self.service.add_movie(186, "Shining", "A good movie", "horror")
        self.service.remove_movie_by_id(186)
        assert(len(self.repository.get_list_of_movies()) == 0)
        
        
    def test_remove_by_genre__valid_movies__list_without_movies(self):
        self.repository.set_list_of_movies([])
        self.service.add_movie(156, "Shining", "A good movie", "horror")
        self.service.remove_movies_by_genre("horror")
        assert(len(self.repository.get_list_of_movies()) == 0)
        
        
    def test_update_movie_id__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(166, "Shining", "A good movie", "horror")
        self.service.update_movie_id(166, 247)
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_movieID() == 247)
    
    
    def test_update_movie_title__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(182, "Shining", "A good movie", "horror")
        self.service.update_movie_title(182, "Cool")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_title() == "Cool")
    
    
    def test_update_movie_description__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(181, "Shining", "A good movie", "horror")
        self.service.update_movie_description(181, "A nice movie")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_description() == "A nice movie")
        
        
    def test_update_movie_genre__valid_movie__list_with_updated_movie(self):
        self.service.add_movie(180, "Shining", "A good movie", "horror")
        self.service.update_movie_genre(180, "Haw roar")
        movies = self.repository.get_list_of_movies() 
        assert(movies[-1].get_genre() == "Haw roar")
        
        
    def test_search_movie_by_id(self):
        test_id = 10
        self.service.add_movie(test_id, "movie", "cool movie", "comedy")
        movie = self.service.search_movie_by_id(test_id)
        assert(movie.get_movieID() == test_id)
    
    
    def test_search_movie_by_title(self):
        test_title = "some movie"
        self.service.add_movie(15, test_title, "cool movie", "comedy")
        movies = self.service.search_movie_by_title(test_title)
        assert(movies[-1].get_title() == test_title)
    
    
    def test_search_movie_by_description(self):
        test_description = "abcd"
        self.service.add_movie(17, "another movie", test_description, "comedy")
        movies = self.service.search_movie_by_description(test_description)
        assert(movies[-1].get_description() == test_description)
        
        
    def test_search_movie_by_genre(self):
        test_genre = "abd"
        self.service.add_movie(20, "another movie", "neat", test_genre)
        movies = self.service.search_movie_by_genre(test_genre)
        assert(movies[-1].get_genre() == test_genre)
        
    
    def run_tests(self):
        self.test_add_movie__valid_movie__list_with_movie()
        self.test_remove_by_id__valid_movie__list_without_movie()
        self.test_remove_by_genre__valid_movies__list_without_movies()
        self.test_update_movie_id__valid_movie__list_with_updated_movie()
        self.test_update_movie_title__valid_movie__list_with_updated_movie()
        self.test_update_movie_description__valid_movie__list_with_updated_movie()
        self.test_update_movie_genre__valid_movie__list_with_updated_movie()
        self.test_search_movie_by_id()
        self.test_search_movie_by_title()
        self.test_search_movie_by_description()
        self.test_search_movie_by_genre()


class TestClientService(unittest.TestCase):
    
    def __init__(self):
        self.repository = ClientRepository()
        self.validator = ClientValidator()
        self.service = ClientService(self.repository, self.validator)
    
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.repository = ClientRepository()
        self.validator = ClientValidator()
        self.service = ClientService(self.repository, self.validator)

    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
        
    def test_add_client__valid_client__list_with_client(self):
        self.service.add_client(12, "John")
        expected_result = [Client(12, "John")]
        clients = self.repository.get_list_of_clients()
        assert(len(expected_result) == len(clients))
        assert(expected_result[-1] == clients[-1])
        
        
    def test_remove_by_id__valid_client__list_without_client(self):
        self.repository.set_list_of_clients([])
        self.service.add_client(13, "John")
        self.service.remove_client_by_id(13)
        assert(len(self.repository.get_list_of_clients()) == 0)
        
        
    def test_update_client_id__valid_client__list_with_updated_client(self):
        self.service.add_client(14, "John")
        self.service.update_client_id(14, 24)
        clients = self.repository.get_list_of_clients() 
        assert(clients[-1].get_clientID() == 24)
    
    
    def test_update_client_name__valid_client__list_with_updated_client(self):
        self.service.add_client(13, "James")
        self.service.update_client_name(13, "Jack")
        clients = self.repository.get_list_of_clients() 
        assert(clients[-1].get_name() == "Jack")
    
    
    def test_search_client_by_id(self):
        test_id = 10
        self.service.add_client(test_id, "some_client")
        client = self.service.search_client_by_id(test_id)
        assert(client.get_clientID() == test_id)
        
        
    def test_search_client_by_name(self):
        test_name = "cool client"
        self.service.add_client(26, test_name)
        clients = self.service.search_client_by_name(test_name)
        assert(clients[-1].get_name() == test_name)
    
    
    def run_tests(self):
        self.test_add_client__valid_client__list_with_client()
        self.test_remove_by_id__valid_client__list_without_client()
        self.test_update_client_id__valid_client__list_with_updated_client()
        self.test_update_client_name__valid_client__list_with_updated_client()
        self.test_search_client_by_id()
        self.test_search_client_by_name()
        
        
class TestRentalService(unittest.TestCase):
    
    def __init__(self):
        self.movie_repository = MovieRepository()
        self.movie_service = MovieService(self.movie_repository, MovieValidator())
        self.client_repository = ClientRepository()
        self.client_service = ClientService(self.client_repository, ClientValidator())
        self.client_repository.add_to_list(Client(5, "John"))
        self.repository = RentalRepository()
        self.validator = RentalValidator()
        self.service = RentalService(self.repository, self.validator, 
                                     self.client_repository, self.movie_repository)    
    
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.movie_repository = MovieRepository()
        self.movie_service = MovieService(self.movie_repository, MovieValidator())
        self.client_repository = ClientRepository()
        self.client_service = ClientService(self.client_repository, ClientValidator())
        self.client_repository.add_to_list(Client(5, "John"))
        self.repository = RentalRepository()
        self.validator = RentalValidator()
        self.service = RentalService(self.repository, self.validator, 
                                     self.client_repository, self.movie_repository)    
    
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_create_rental__valid_rental__list_with_rental(self):
        self.service.create_rental(5, 1, 10, date.today(), date(2019, 12, 22))
        expected_result = [Rental(5, 1, 10, date.today(), date(2019, 12, 22), date(1, 1, 1))]
        rentals = self.repository.get_list_of_rentals()
        assert(len(expected_result) == len(rentals))
        assert(expected_result[-1] == rentals[-1])
        self.repository.set_list_of_rentals([])
        
        
    def test_delete_rental__valid_rental__list_with_rental(self):
        self.service.delete_rental(5)
        rentals = self.repository.get_list_of_rentals()
        assert(len(rentals) == 0)
    
    
    def test_create_rented_movies_statistics(self):
        self.movie_repository.set_list_of_movies([])
        self.movie_service.add_movie(12, "abc", "def", "ghi")
        self.movie_service.add_movie(13, "aaa", "bbb", "ccc")
        self.service.create_rental(15, 12, 1, date(2019, 5, 5), date(2019, 12, 30))
        self.service.create_rental(13, 13, 2, date(2019, 1, 1), date(2019, 12, 30))
        statistic = self.service.create_rented_movies_statistics()
        
        for movie_index in range(0, len(statistic) - 1):
            assert(statistic[movie_index][1] > statistic[movie_index+1][1])
    
    
    def test_create_active_clients_statistics(self):
        self.movie_repository.set_list_of_movies([])
        self.client_repository.set_list_of_clients([])
        self.repository.set_list_of_rentals([])
        self.client_service.add_client(20, "client1")
        self.client_service.add_client(21, "client2")
        self.movie_service.add_movie(99, "abc", "def", "ghi")
        self.movie_service.add_movie(100, "aaa", "bbb", "ccc")
        self.movie_service.add_movie(101, "zzzzz", "zzzzzz", "zzzzzzz")
        self.service.create_rental(0, 99, 21, date(2019, 5, 5), date(2019, 12, 30))
        self.service.create_rental(1, 100, 20, date(2019, 1, 1), date(2019, 12, 30))
        self.service.create_rental(2, 101, 21, date(2019, 3, 3), date(2019, 12, 30))
        
        statistic = self.service.create_active_clients_statistics()
        
        for client_index in range(0, len(statistic) - 1):
            assert(statistic[client_index][1] > statistic[client_index+1][1])
        
        
    def test_create_late_rentals_statistics(self):
        self.movie_repository.set_list_of_movies([])
        self.client_repository.set_list_of_clients([])
        self.repository.set_list_of_rentals([])
        self.client_service.add_client(22, "client1")
        self.client_service.add_client(23, "client2")
        self.movie_service.add_movie(102, "abc", "def", "ghi")
        self.movie_service.add_movie(103, "aaa", "bbb", "ccc")
        self.movie_service.add_movie(104, "zzzzz", "zzzzzz", "zzzzzzz")
        self.service.create_rental(55, 102, 22, date(2019, 5, 5), date(2000, 12, 30))
        self.service.create_rental(56, 103, 23, date(2019, 1, 1), date(2001, 12, 30))
        self.service.create_rental(57, 104, 22, date(2019, 3, 3), date(2002, 12, 30))
        
        statistic = self.service.create_late_rentals_statistics()
        
        for movie_index in range(0, len(statistic) - 1):
            assert(statistic[movie_index][1] > statistic[movie_index+1][1])
        
        
    def run_tests(self):
        self.test_create_rental__valid_rental__list_with_rental()
        self.test_delete_rental__valid_rental__list_with_rental()
        self.test_create_rented_movies_statistics()
        self.test_create_active_clients_statistics()
        self.test_create_late_rentals_statistics()
        
        
class Tests:
    
    def __init__(self):
        self.test_movie_service = TestMovieService()
        self.test_client_service = TestClientService()
        self.test_rental_service = TestRentalService()
        
        
    def run_tests(self):
        self.test_movie_service.run_tests()
        self.test_client_service.run_tests()
        self.test_rental_service.run_tests()
        
        
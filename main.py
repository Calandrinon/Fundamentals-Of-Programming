from tests import Tests
from ui import UI
from service import *
from repository import *
from validation import MovieValidator

"""
    TODO: For feature 4.1, print the rental date of each movie
"""

def main():
    tests = Tests()
    tests.run_tests()
    undo_repository = UndoRepository()
    undo_service = UndoService(undo_repository)
    movie_validator = MovieValidator()
    movie_repository = MovieRepository()
    movie_service = MovieService(movie_repository, movie_validator, undo_repository)
    client_validator = ClientValidator()
    client_repository = ClientRepository()
    client_service = ClientService(client_repository, client_validator, undo_repository)
    rental_validator = RentalValidator()
    rental_repository = RentalRepository()
    rental_service = RentalService(rental_repository, rental_validator, client_repository, movie_repository, undo_repository)
    ui = UI(movie_service, client_service, rental_service, undo_service)
    ui.main()


main()

from tests import Tests
from ui import UI
from service import *
from repository import *
from validation import MovieValidator

"""
    TODO: Write validation functions for removal and update features.
"""


def main():
    tests = Tests()
    tests.run_tests()
    movie_validator = MovieValidator()
    movie_repository = MovieRepository()
    movie_service = MovieService(movie_repository, movie_validator)
    client_validator = ClientValidator()
    client_repository = ClientRepository()
    client_service = ClientService(client_repository, client_validator)
    ui = UI(movie_service, client_service)
    ui.main()


main()

from tests import *
from ui import UI
from service import *
from repository import *
from validation import MovieValidator

"""
    TODO: Check if there's already a movie with the same ID in the repo.
    TODO: Write validation functions for removal and update features.
"""

def main():
    tests = Tests()
    tests.run_tests()
    movie_validator = MovieValidator()
    movie_repository = MovieRepository()
    movie_service = MovieService(movie_repository, movie_validator)
    ui = UI(movie_service)
    ui.main()
    print("Process killed successfully")

main()

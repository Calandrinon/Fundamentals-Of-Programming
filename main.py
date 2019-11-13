from tests import *
from ui import UI
from service import *
from repository import *
from validation import MovieValidator

def main():
    tests = Tests()
    tests.run_tests()
    movie_validator = MovieValidator()
    movie_repository = MovieRepository()
    movie_service = MovieService(movie_repository, movie_validator)
    ui_instance = UI(movie_service)
    print("Process killed successfully")

main()

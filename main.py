from tests import Tests
from ui import UI
from service import *
from repository import *
from validation import MovieValidator
from domain import *
import os.path

def create_file(filename):
    if os.path.exists(filename) == False:
        f = open(filename, "w")
        f.close()
    

def read_txt_config_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    
    option = lines[0].split("=")
    option = option[1].strip()
    
    del lines[0]
    
    files = {}
    files[0] = option
    
    for line in lines:
        line = line.split("=")
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        files[line[0]] = line[1]
        
    for file in files:
        print(file)
        create_file(file)
        
    
    return files


def main():
    files = read_txt_config_file("settings.properties")
    movies_files = FileRepository(files["movies"], Movie.read_movie, Movie.write_movie, files[0])
    clients_files = FileRepository(files["clients"], Client.read_client, Client.write_client, files[0])
    rentals_files = FileRepository(files["rentals"], Rental.read_rental, Rental.write_rental, files[0])
    
    #tests = Tests()
    #tests.run_tests()
    undo_repository = UndoRepository()
    undo_service = UndoService(undo_repository)
    movie_validator = MovieValidator()
    movie_repository = MovieRepository(movies_files)
    movie_service = MovieService(movie_repository, movie_validator, undo_repository)
    client_validator = ClientValidator()
    client_repository = ClientRepository(clients_files)
    client_service = ClientService(client_repository, client_validator, undo_repository)
    rental_validator = RentalValidator()
    rental_repository = RentalRepository(rentals_files)
    rental_service = RentalService(rental_repository, rental_validator, client_repository, movie_repository, undo_repository)
    ui = UI(movie_service, client_service, rental_service, undo_service)
    ui.main()


main()

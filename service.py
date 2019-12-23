from domain import *

class PlaneService:
    
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator
        self.__board = Board()
    
    
    def add_plane(self, x_coordinate, y_coordinate, orientation):
        """
            Adds a plane to the repository of planes and draws it
            on the board.
            
            Input:
                - x_coordinatae - integer
                - y_coordinate - integer
                - orientation - ("up", "down", "left" or "right")
        """
        
        plane = Plane(x_coordinate, y_coordinate, orientation, self.__board)
        
        self.__validator.validate_plane(plane)
        self.__repository.add(plane)
        
        surface_positions = plane.get_surface_positions()
        
        for position in surface_positions:
            self.__board.set_value_of_position_x_y(position[0], position[1], '#')
        
        
    def get_board(self):
        return self.__board
        
        

class ComputerService(PlaneService):
    pass


class PlayerService(PlaneService):
    pass

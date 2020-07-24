from domain import *

class PlaneService:
    
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator
        self.__board = Board()
        self.__hits_board = Board()
        self.score = 0
        
        
    def set_opponent(self, opponent):
        self.__opponent = opponent
    
    
    def __create_plane(self, x_coordinate, y_coordinate, orientation, board):
        plane = Plane(x_coordinate, y_coordinate, orientation, board)
        
        self.__validator.validate_plane(plane)
        self.__repository.add(plane)
        
        return plane
        
    
    def add_plane(self, x_coordinate, y_coordinate, orientation):
        """
            Adds a plane to the repository of planes and draws it
            on the board.
            
            Input:
                - x_coordinatae - integer
                - y_coordinate - integer
                - orientation - ("up", "down", "left" or "right")
        """
        
        plane = self.__create_plane(x_coordinate, y_coordinate, orientation, self.__board)
        
        surface_positions = plane.get_surface_positions()
        
        for position in surface_positions:
            self.__board.set_value_of_position_x_y(position[0], position[1], '#')
        
    
    def get_repository(self):
        return self.__repository
        
        
    def get_board(self):
        return self.__board
        
        
    def reset_service(self):
        self.__repository.clear()
        self.__board = Board()
        self.__hits_board = Board()
        self.score = 0
        
        
    def get_hits_board(self):
        return self.__hits_board
        
        
    def attack_opponent(self, x_coordinate, y_coordinate):
        
        """
        Attacks the opponent. Checks if the coordinates of the position
        (x_coordinate, y_coordinate) contain a portion of the surface of an
        enemy plane.
        
        Input:
            x_coordinate - integer
            y_coordinate - integer
        
        """
        
        self.__validator.validate_position_coordinates((x_coordinate, y_coordinate), self.__board.get_size())
        
        opponent_planes = self.__opponent.get_repository().get_container()

        for enemy_plane in opponent_planes:
            enemy_plane_surface_positions = enemy_plane.get_surface_positions()
            for position in enemy_plane_surface_positions:
                if position[0] == x_coordinate and position[1] == y_coordinate:
                    value = "*"
                    
                    if len(position) > 2:
                        value = "X"
                        self.score += 1
                    
                    if isinstance(self.__opponent, PlayerService):
                        self.__opponent.get_board().set_value_of_position_x_y(x_coordinate, y_coordinate, value)
                        return
                    self.__hits_board.set_value_of_position_x_y(x_coordinate, y_coordinate, value)
                    return
                else:
                    if isinstance(self.__opponent, PlayerService):
                        self.__opponent.get_board().set_value_of_position_x_y(x_coordinate, y_coordinate, "?")
                        continue
                    self.__hits_board.set_value_of_position_x_y(x_coordinate, y_coordinate, "?")
    


class ComputerService(PlaneService):
    pass


class PlayerService(PlaneService):
    pass

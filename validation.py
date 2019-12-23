from domain import Plane
from errors import PlaneError

class PlaneValidator(object):
    
    def validate_plane(self, plane):
        if not isinstance(plane, Plane):
            raise ValueError("This is not a plane!")
        
        surface_positions = plane.get_surface_positions()
        
        plane_board = plane.get_board()
        
        for position in surface_positions:
            self.validate_position_coordinates(position, plane_board.get_size())
            
            if plane_board.get_value_of_position_x_y(position[0], position[1]) != ".":
                raise PlaneError("Can't place the plane on an occupied surface!")

    
    def validate_position_coordinates(self, position, plane_board_size):
        if position[0] < 0 or position[0] >= plane_board_size or position[1] < 0 or position[1] >= plane_board_size:
                raise PlaneError("The surface position with the coordinates (" + str(position[0]) + "," + str(position[1]) + ") goes beyond the boundaries of the board!")
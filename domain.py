
class Plane:
    
    def __init__(self, x_coordinate, y_coordinate, orientation, board):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__orientation = orientation
        self.__board = board
        self.__surface_positions = []
        
        if orientation == "up":
            for row in range(x_coordinate, x_coordinate + 4):
                self.__surface_positions.append((row, y_coordinate))
            
            self.__surface_positions[0] = (x_coordinate, y_coordinate, 1)
        
            self.__surface_positions.append((x_coordinate + 1, y_coordinate - 2))
            self.__surface_positions.append((x_coordinate + 1, y_coordinate - 1))
            self.__surface_positions.append((x_coordinate + 1, y_coordinate + 1))
            self.__surface_positions.append((x_coordinate + 1, y_coordinate + 2))
            
            self.__surface_positions.append((x_coordinate + 3, y_coordinate - 1))
            self.__surface_positions.append((x_coordinate + 3, y_coordinate + 1))
        elif orientation == "down":
            for row in range(x_coordinate, x_coordinate - 4, -1):
                self.__surface_positions.append((row, y_coordinate))
            
            self.__surface_positions[0] = (x_coordinate, y_coordinate, 1)
            
            self.__surface_positions.append((x_coordinate - 1, y_coordinate - 2))
            self.__surface_positions.append((x_coordinate - 1, y_coordinate - 1))
            self.__surface_positions.append((x_coordinate - 1, y_coordinate + 1))
            self.__surface_positions.append((x_coordinate - 1, y_coordinate + 2))
            
            self.__surface_positions.append((x_coordinate - 3, y_coordinate - 1))
            self.__surface_positions.append((x_coordinate - 3, y_coordinate + 1))
        elif orientation == "left":
            for column in range(y_coordinate, y_coordinate + 4):
                self.__surface_positions.append((x_coordinate, column))
            
            self.__surface_positions[0] = (x_coordinate, y_coordinate, 1)
            
            self.__surface_positions.append((x_coordinate - 1, y_coordinate + 1))
            self.__surface_positions.append((x_coordinate - 2, y_coordinate + 1))
            self.__surface_positions.append((x_coordinate + 1, y_coordinate + 1))
            self.__surface_positions.append((x_coordinate + 2, y_coordinate + 1))
            
            self.__surface_positions.append((x_coordinate - 1, y_coordinate + 3))
            self.__surface_positions.append((x_coordinate + 1, y_coordinate + 3))
        elif orientation == "right":
            for column in range(y_coordinate, y_coordinate - 4, -1):
                self.__surface_positions.append((x_coordinate, column))
            
            self.__surface_positions[0] = (x_coordinate, y_coordinate, 1)
            
            self.__surface_positions.append((x_coordinate - 1, y_coordinate - 1))
            self.__surface_positions.append((x_coordinate - 2, y_coordinate - 1))
            self.__surface_positions.append((x_coordinate + 1, y_coordinate - 1))
            self.__surface_positions.append((x_coordinate + 2, y_coordinate - 1))
            
            self.__surface_positions.append((x_coordinate - 1, y_coordinate - 3))
            self.__surface_positions.append((x_coordinate + 1, y_coordinate - 3))
        
    """
    def get_x_coordinate(self):
        return self.__x_coordinate


    def get_y_coordinate(self):
        return self.__y_coordinate


    def get_orientation(self):
        return self.__orientation
    """
    
    def get_board(self):
        return self.__board


    def get_surface_positions(self):
        return self.__surface_positions

        
        
class Board:
    
    def __init__(self, size=10):
        self.__size = size
        self.__matrix = [['.' for rows in range(0, size)] for columns in range(0, size)]
    
    
    def get_value_of_position_x_y(self, position_x, position_y):
        return self.__matrix[position_x][position_y]
    
    
    def set_value_of_position_x_y(self, position_x, position_y, value):
        self.__matrix[position_x][position_y] = value


    def get_size(self):
        return self.__size
    
    
    def __str__(self):
        result = "  "
        row_index = 0
        spaces = 2
        
        for column in range(0, self.__size):
            result += str(column+1) + "  "
        result += "\n\n"
        
        for row in self.__matrix:
            row_index += 1
            
            if row_index > 9:
                 spaces = 1
            result += str(row_index) + spaces * " "
            
            for column in row:
                result += column + "  "
            result += "\n\n"
            
        return result
    
    
    
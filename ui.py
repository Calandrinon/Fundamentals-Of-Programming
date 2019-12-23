from errors import PlaneError

class UI(object):
    
    
    def __init__(self, player_service, computer_service):
        self.__player_service = player_service
        self.__computer_service = computer_service


    def __draw_board(self):
        board = self.__player_service.get_board()
        print(board)

    
    def __add_plane(self):
        plane_x_coordinate = int(input("Enter the x coordinate of the plane: "))
        plane_y_coordinate = int(input("Enter the y coordinate of the plane: "))
        
        plane_orientation = input("Enter the orientation of the plane: ")
        
        self.__player_service.add_plane(plane_x_coordinate, plane_y_coordinate, plane_orientation)
    
        
    def __place_planes(self, number_of_planes):
        
        while number_of_planes > 0:
            self.__draw_board()
            
            try:
                self.__add_plane()
                number_of_planes -= 1
            except PlaneError as pe:
                print(pe)
            except ValueError as ve:
                print(ve)
                
    
    def run(self):
        
        self.__place_planes(2)
        self.__draw_board()
        
        #while True:
        #    pass
    
    
    




from errors import PlaneError
from random import randint

class UI(object):
    
    def __init__(self, player_service, computer_service):
        self.__player_service = player_service
        self.__computer_service = computer_service


    def __clear_screen(self):
        print(100*"\n")


    def __draw_board(self, service):
        board = service.get_board()
        
        if service != self.__computer_service:
            print("Board with your planes: ")
            
        print(board)
        print("\n"*2)
    
    
    def __add_plane(self, service):
        
        if service == self.__computer_service:
            orientations = ["up", "down", "left", "right"]
            plane_x_coordinate = randint(0, 9)
            plane_y_coordinate = randint(0, 9)
            plane_orientation = orientations[randint(0, 3)]
            service.add_plane(plane_x_coordinate, plane_y_coordinate, plane_orientation)
            return
        
        plane_x_coordinate = int(input("Enter the x coordinate of the plane: "))
        plane_y_coordinate = int(input("Enter the y coordinate of the plane: "))
        
        plane_orientation = 0
        
        while plane_orientation not in ["up", "down", "left", "right"]:
            plane_orientation = input("Enter the orientation of the plane (up, down, left or right): ")
        
        service.add_plane(plane_x_coordinate, plane_y_coordinate, plane_orientation)
    
        
    def __place_planes(self, service, number_of_planes):
        
        errors = []
        
        while number_of_planes > 0:
            if service == self.__player_service:
                self.__clear_screen()
                if len(errors) > 0:
                    for error in errors:
                        print(error)
                    del errors[:]
                self.__draw_board(service)
            
            try:
                self.__add_plane(service)
                number_of_planes -= 1
            except PlaneError as pe:
                errors.append(pe)
            except ValueError as ve:
                errors.append(ve)
                
        
    def __display_hits_board(self):        
        hits_board = self.__player_service.get_hits_board()
        print("Hits board: ")
        print(hits_board)
        print("\n"*2)
    
    
    def __attack_enemy(self, service):
        
        if service == self.__player_service:
            x_coordinate = int(input("Enter the x coordinate of the target point: "))
            y_coordinate = int(input("Enter the y coordinate of the target point: "))
        else:
            x_coordinate = randint(0,9)
            y_coordinate = randint(0,9)
            
        service.attack_opponent(x_coordinate, y_coordinate)
    
    
    def run(self):
        
        self.__place_planes(self.__computer_service, 2)
        self.__place_planes(self.__player_service, 2)
        self.__draw_board(self.__player_service)
        
        errors = []
        game_over_message = ""
        self.__clear_screen()
        
        while True:
            try:
                self.__clear_screen()
                
                if len(errors) > 0:
                    for error in errors:
                        print(error)
                    del errors[:]
                
                self.__draw_board(self.__player_service)
                self.__display_hits_board()
                self.__attack_enemy(self.__player_service)
                self.__attack_enemy(self.__computer_service)
                
                if self.__player_service.score == 2:
                    game_over_message = "You won!"
                    break 
                elif self.__computer_service.score == 2:
                    game_over_message = "You lost!"
                    break
                
            except ValueError as ve:
                errors.append(ve)
            except PlaneError as pe:
                errors.append(pe)
            
        self.__clear_screen()
        self.__draw_board(self.__player_service)
        self.__display_hits_board()
        print(game_over_message)


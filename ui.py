from errors import PlaneError
from random import randint
import pygame
from pygame.locals import *


class UI(object):

    cell_width = 40

    def __init__(self, player_service, computer_service):
        self.__player_service = player_service
        self.__computer_service = computer_service
        self.__interrupted_program = False
        self.__errors = []
        self.__game_over_message = ""
        self.__active_gui = False
        self.__cell_width = 40
        self.__multiplayer = False
        
        self.__menu_options = ["Singleplayer (0)", "Multiplayer (1)", "Quit (2)"]
        self.__font_size = 30
        self.__font_title = "Times New Roman"
        
        self.__plane_selection_row = 0
        self.__plane_selection_column = 0
        self.__plane_selection_orientation = 0
        self.__plane_selection_orientations = ["up", "left", "down", "right"]
        self.__initialization_finished = False
        

    def __clear_screen(self):
        if self.__active_gui:
            self.__screen.fill((255,255,255))
            ### pygame.display.flip() - unnecessary
            return
        print(100*"\n")
        
        
    def __cell_selector_event_move_to_left(self, event):
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if self.__plane_selection_column > 0:
                self.__plane_selection_column -= 1
        
        
    def __cell_selector_event_move_downwards(self, event):
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            if self.__plane_selection_row < self.__player_service.get_board().get_size() - 1:
                self.__plane_selection_row += 1
        
        
    def __cell_selector_event_move_to_right(self, event):
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if self.__plane_selection_column < self.__player_service.get_board().get_size() - 1:
                self.__plane_selection_column += 1


    def __cell_selector_event_move_upwards(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            if self.__plane_selection_row > 0:
                self.__plane_selection_row -= 1
    
    
    def __cell_selector_rotation_event(self, event):
        if event.key == pygame.K_r:
            self.__plane_selection_orientation += 1
            if self.__plane_selection_orientation > 3:
                self.__plane_selection_orientation = 0
    
    
    def __plane_attack_event(self, event):
        if event.key == pygame.K_RETURN:
            self.__player_service.add_plane(self.__plane_selection_row, self.__plane_selection_column, self.__plane_selection_orientations[self.__plane_selection_orientation])
            return -1
    

    def __add_plane_handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                self.__cell_selector_event_move_to_left(event)
                self.__cell_selector_event_move_downwards(event)
                self.__cell_selector_event_move_to_right(event)
                self.__cell_selector_event_move_upwards(event)
                self.__cell_selector_rotation_event(event)
                if self.__plane_attack_event(event) == -1:
                    return -1
                self.__update_display(plane_selection=True)
                
                
    def __draw_selected_cell(self, cell_x_coordinate_minimum=cell_width, cell_y_coordinate_minimum=cell_width):
        matrix_cell = pygame.Rect(cell_x_coordinate_minimum + self.__plane_selection_column * self.__cell_width, 
                                  cell_y_coordinate_minimum + self.__plane_selection_row * self.__cell_width, 
                                  self.__cell_width, self.__cell_width)
        pygame.draw.rect(self.__screen, (155, 0, 0), matrix_cell, 10)


    def __display_player_board_title(self):
        text_font = pygame.font.SysFont(self.__font_title, self.__font_size)
        message = text_font.render("Your board", False, (0, 0, 0))
        self.__screen.blit(message, (self.__cell_width * 12, self.__cell_width + 5 * self.__cell_width))


    def __display_hit_board_title(self):
        text_font = pygame.font.SysFont(self.__font_title, self.__font_size)
        message = text_font.render("Your shots", False, (0, 0, 0))
        self.__screen.blit(message, (self.__cell_width * 12, self.__cell_width + 15 * self.__cell_width))


    def __draw_graphical_board(self, board, board_type, service, position_x, position_y):
        self.__display_player_board_title()
        matrix_cell = pygame.Rect(position_x, position_y, self.__cell_width, self.__cell_width)
        cell_colors_for_various_characters = {'#':((100,100,100),0), '.':((0,0,0),2), '*':((255,0,0),0), 'X':((0,0,0),0), '?':((0,225,0),0)}

        for row_index in range(0, board.get_size()):  # @UnusedVariable
            matrix_cell.left = self.__cell_width
            for column_index in range(0, board.get_size()):  # @UnusedVariable
                cell_color, width = cell_colors_for_various_characters[board.get_value_of_position_x_y(row_index, column_index)]
                pygame.draw.rect(self.__screen, cell_color, matrix_cell, width)
                matrix_cell.left += self.__cell_width

            matrix_cell.top += self.__cell_width
        
        if board_type == "hit_board" and self.__initialization_finished:
            self.__display_hit_board_title()
            self.__draw_selected_cell(cell_y_coordinate_minimum=service.get_board().get_size()*self.__cell_width+2*self.__cell_width)
        elif not self.__initialization_finished:
            self.__draw_selected_cell()
        pygame.display.update()


    def __draw_board(self, service, board_type="plane_board", position_x=cell_width, position_y=cell_width):
        board = service.get_board()
        if board_type == "hit_board" and self.__initialization_finished:
            board = service.get_hits_board()

        if self.__active_gui:
            self.__draw_graphical_board(board, board_type, service, position_x, position_y)
            return

        if service != self.__computer_service:
            print("Board with your planes: ")
        print(board)
        print("\n"*2)
    

    def __add_plane_display_message(self):
        text_font = pygame.font.SysFont(self.__font_title, self.__font_size)
        message = text_font.render("Use the arrows to select the position of the plane", False, (0, 0, 0))
        self.__screen.blit(message, (self.__cell_width, self.__cell_width + 10 * self.__cell_width))
        message = text_font.render("To rotate the orientation of the plane, press R", False, (0, 0, 0))
        self.__screen.blit(message, (self.__cell_width, 2 * self.__cell_width + 10 * self.__cell_width))
        message = text_font.render("Press Enter to place the plane", False, (0, 0, 0))
        self.__screen.blit(message, (self.__cell_width, 3 * self.__cell_width + 10 * self.__cell_width))
        pygame.display.update()
        
        
    def __plane_position_selected(self):
        if self.__add_plane_handle_input() == -1:
            return True
        return False
        

    def __add_plane(self, service):

        if service == self.__computer_service:
            orientations = ["up", "down", "left", "right"]
            plane_x_coordinate = randint(0, 9)
            plane_y_coordinate = randint(0, 9)
            plane_orientation = orientations[randint(0, 3)]
            service.add_plane(plane_x_coordinate, plane_y_coordinate, plane_orientation)
            return

        if self.__active_gui:
            self.__add_plane_display_message()
            while not self.__plane_position_selected():
                pass
            return

        plane_x_coordinate = int(input("Enter the x coordinate of the plane: ")) - 1
        plane_y_coordinate = int(input("Enter the y coordinate of the plane: ")) - 1
        plane_orientation = 0

        while plane_orientation not in ["up", "down", "left", "right"]:
            plane_orientation = input("Enter the orientation of the plane (up, down, left or right): ")

        service.add_plane(plane_x_coordinate, plane_y_coordinate, plane_orientation)


    def __place_planes(self, service, number_of_planes):

        errors = []

        while number_of_planes > 0:
            if service == self.__player_service:
                self.__clear_screen()
                if not self.__active_gui and len(errors) > 0:
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
        if self.__active_gui and self.__initialization_finished:
            self.__draw_board(self.__player_service, "hit_board", position_y=2*self.__cell_width+self.__cell_width*self.__player_service.get_board().get_size())
            return
        hits_board = self.__player_service.get_hits_board()
        print("Hits board: ")
        print(hits_board)
        print("\n"*2)


    def __attack_enemy(self, service):
        
        if service == self.__player_service:
            if self.__active_gui:
                x_coordinate = self.__plane_selection_row
                y_coordinate = self.__plane_selection_column
            else:
                x_coordinate = int(input("Enter the x coordinate of the target point: ")) - 1
                y_coordinate = int(input("Enter the y coordinate of the target point: ")) - 1
                
        else:
            x_coordinate = randint(0,9)
            y_coordinate = randint(0,9)

        service.attack_opponent(x_coordinate, y_coordinate)


    def __initialize_planes(self):
        self.__update_display()

        try:
            self.__place_planes(self.__computer_service, 2)
            self.__place_planes(self.__player_service, 2)
            self.__initialization_finished = True
        except KeyboardInterrupt:
            print("\nGood bye!\n")
            return True


    def __display_error_list(self):
        if len(self.__errors) > 0:
            for error in self.__errors:
                print(error)
            del self.__errors[:]


    def __pygame_event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                self.__cell_selector_event_move_to_left(event)
                self.__cell_selector_event_move_downwards(event)
                self.__cell_selector_event_move_to_right(event)
                self.__cell_selector_event_move_upwards(event)
                if event.key == pygame.K_RETURN:
                    self.__attack_enemy(self.__player_service)
                    self.__attack_enemy(self.__computer_service)
                self.__update_display()
                

    def __update_display(self, plane_selection=False):
        self.__clear_screen()
        self.__draw_board(self.__player_service)
        if plane_selection:
            self.__draw_selected_cell()
        self.__display_hits_board()
        self.__display_error_list()
        if self.__active_gui:
            pygame.display.flip()


    def __display_game_over_message(self):
        text_font = pygame.font.SysFont(self.__font_title, self.__font_size)
        message = text_font.render(self.__game_over_message, False, (0, 0, 0))
        self.__screen.blit(message, (self.__cell_width * 12, self.__cell_width + self.__cell_width))
        message = text_font.render("Press ESC to exit to main menu", False, (0, 0, 0))
        self.__screen.blit(message, (self.__cell_width * 12, self.__cell_width + 3 * self.__cell_width))
        pygame.display.update()
        

    def __waiting_mode(self):
        if not self.__active_gui:
            return
        self.__display_game_over_message()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
    
    
    def __attacking_stage(self):
        if self.__active_gui and self.__pygame_event_handling():
            return -1
                
        if not self.__active_gui:
            self.__update_display()
            self.__attack_enemy(self.__player_service)
            self.__attack_enemy(self.__computer_service)
                    
        if self.__player_service.score == 2:
            self.__game_over_message = "You won!"
            self.__waiting_mode()
            return -1
        elif self.__computer_service.score == 2:
            self.__game_over_message = "You lost!"
            self.__waiting_mode()
            return -1
    

    def __catch_input_exceptions(self):
        try:
            if self.__attacking_stage() == -1:
                return -1
        except ValueError as ve:
            self.__errors.append(ve)
        except PlaneError as pe:
            self.__errors.append(pe)
        except KeyboardInterrupt:
            self.__interrupted_program = True
            print("\nGood bye!\n")
            return -1


    def __main_loop(self):
        self.__plane_selection_row = 0
        self.__plane_selection_column = 0
        self.__update_display()
        
        while True:
            if self.__catch_input_exceptions() == -1:
                return


    def __ui_selection(self):
        gui = ""
        self.__clear_screen()
        
        while gui.lower() not in ['y', 'n']:
            gui = input("Do you want to use the GUI? (y/n)")
            if gui.lower() == 'y':
                self.__active_gui = True
                pygame.init()
                self.__window_width = 1000
                self.__window_height = 1000
                self.__screen = pygame.display.set_mode((self.__window_width, self.__window_height), FULLSCREEN | DOUBLEBUF)
                self.__screen.set_alpha(None)
                pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
                
        self.__clear_screen()


    def __reset_services(self):
        self.__player_service.reset_service()
        self.__computer_service.reset_service()


    def __reset_game(self):
        self.__reset_services()
        self.__plane_selection_row = 0
        self.__plane_selection_column = 0
        self.__plane_selection_orientation = 0
        self.__initialization_finished = False
        

    def __singleplayer_mode(self):
        self.__reset_game()
        if self.__initialize_planes():
            return
        self.__clear_screen()
        self.__main_loop()
        self.__clear_screen()
        self.__draw_board(self.__player_service)
        print(self.__game_over_message)
        self.__display_hits_board()


    def __multiplayer_mode(self):
        self.__reset_game()
        if self.__initialize_planes():
            return
        self.__clear_screen()
        self.__main_loop()
        self.__clear_screen()
        self.__draw_board(self.__player_service)
        print(self.__game_over_message)
        self.__display_hits_board()


    def __print_options(self):
        index = 0
        for option in self.__menu_options:
            print(index, ": " + option)
            index += 1


    def __console_main_menu(self):
        if not self.__active_gui:
            while True:
                self.__print_options()

                try:
                    option = int(input("Enter an option: "))

                    if option < 0 or option > len(self.__menu_options) - 1:
                        print("Enter a number between 0 and {}".format(len(self.__menu_options) - 1))
                        continue
                    elif option == 0:
                        self.__singleplayer_mode()
                    elif option == 1:
                        self.__multiplayer_mode()
                    else:
                        self.__interrupted_program = True
                        return
                except ValueError:
                    print("Enter an integer between 1 and 3!")


    def __display_menu_option(self, font_size, option_title, option_index):
        text_font = pygame.font.SysFont(self.__font_title, font_size)
        option = text_font.render(option_title, False, (0, 0, 0))

        self.__screen.blit(option, (self.__window_width / font_size, self.__window_height / font_size + option_index * 2 * font_size))


    def __display_menu(self):
        self.__clear_screen()
        for option_index in range(0, len(self.__menu_options)):
                self.__display_menu_option(self.__font_size, self.__menu_options[option_index], option_index)
        pygame.display.update()

    
    def __graphical_main_menu(self):
        if self.__active_gui:
            self.__display_menu()

            while True:
                events = pygame.event.get()
                
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_0, pygame.K_s]:
                            self.__singleplayer_mode()
                        if event.key in [pygame.K_1, pygame.K_m]:
                            self.__multiplayer_mode()
                        if event.key in [pygame.K_ESCAPE, pygame.K_2]:
                            return
                    self.__display_menu()


    def __main_menu(self):
        self.__graphical_main_menu()
        self.__console_main_menu()


    def run(self):

        self.__ui_selection()
        self.__main_menu()

        if self.__interrupted_program == False and not self.__active_gui:
            self.__clear_screen()
            self.__draw_board(self.__player_service)
            self.__display_hits_board()
            if not self.__active_gui:
                print(self.__game_over_message)

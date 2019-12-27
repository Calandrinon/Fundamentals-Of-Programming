from errors import PlaneError
from random import randint
import pygame

class UI(object):

    def __init__(self, player_service, computer_service):
        self.__player_service = player_service
        self.__computer_service = computer_service
        self.__interrupted_program = False
        self.__errors = []
        self.__game_over_message = ""
        self.__active_gui = False
        self.__cell_width = 50
        self.__multiplayer = False
        self.__menu_options = ["Singleplayer (1)", "Multiplayer (2)", "Quit (0)"]
        self.__font_size = 40


    def __clear_screen(self):
        if self.__active_gui:
            self.__screen.fill((255,255,255))
            pygame.display.flip()
            return
        print(100*"\n")


    def __draw_board(self, service):
        board = service.get_board()

        if self.__active_gui:
            matrix_cell = pygame.Rect(0, 0, self.__cell_width, self.__cell_width)
            cell_colors_for_various_characters = {'#':((100,100,100),0), ### '#' is a plane surface on the board
                                                  '.':((0,0,0),2), ### '.' is a free surface
                                                  '*':((255,0,0),0), ### '*' is a plane surface that has been hit by the enemy
                                                  'X':((0,0,0),0),   ### 'X' is a pilot cabin that has been hit by the enemy
                                                  '?':((0,225,0),0)} ### '?' is a surface that has been unsuccessfully attacked by the enemy

            for row_index in range(0, board.get_size()):  # @UnusedVariable
                matrix_cell.left = 0
                for column_index in range(0, board.get_size()):  # @UnusedVariable
                    cell_color, width = cell_colors_for_various_characters[board.get_value_of_position_x_y(row_index, column_index)]
                    pygame.draw.rect(self.__screen, cell_color, matrix_cell, width)
                    matrix_cell.left += self.__cell_width

                matrix_cell.top += self.__cell_width

            pygame.display.update()

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

        #if self.__active_gui:
        #   pass

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


    def __initialize_planes(self):
        self.__draw_board(self.__player_service)


        try:
            self.__place_planes(self.__computer_service, 2)
            self.__place_planes(self.__player_service, 2)
            self.__draw_board(self.__player_service)
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
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return True


    def __update_display(self):
        self.__clear_screen()
        self.__draw_board(self.__player_service)
        self.__display_hits_board()
        self.__display_error_list()
        if self.__active_gui:
            pygame.display.flip()


    def __main_loop(self):
        while True:
            try:
                if self.__active_gui and self.__pygame_event_handling():
                    break

                self.__update_display()

                self.__attack_enemy(self.__player_service)
                self.__attack_enemy(self.__computer_service)

                if self.__player_service.score == 2:
                    self.__game_over_message = "You won!"
                    return
                elif self.__computer_service.score == 2:
                    self.__game_over_message = "You lost!"
                    return

            except ValueError as ve:
                self.__errors.append(ve)
            except PlaneError as pe:
                self.__errors.append(pe)
            except KeyboardInterrupt:
                self.__interrupted_program = True
                print("\nGood bye!\n")
                break


    def __ui_selection(self):
        gui = ""

        while gui.lower() not in ['y', 'n']:
            gui = input("Do you want to use the GUI? (y/n)")
            if gui.lower() == 'y':
                self.__active_gui = True
                pygame.init()
                self.__window_width = 800
                self.__window_height = 600
                self.__screen = pygame.display.set_mode((self.__window_width, self.__window_height))

        self.__clear_screen()


    def __display_menu_option(self, font_size, option_title, option_index):
        comic_sans_font = pygame.font.SysFont('Comic Sans MS', font_size)
        option = comic_sans_font.render(option_title, False, (0, 0, 0))

        self.__screen.blit(option, (self.__window_width / font_size, self.__window_height / font_size + option_index * 2 * font_size))


    def __reset_services(self):
        self.__player_service.reset_service()
        self.__computer_service.reset_service()


    def __singleplayer_mode(self):
        self.__reset_services()
        if self.__initialize_planes():
            return
        self.__clear_screen()
        self.__main_loop()
        self.__clear_screen()
        self.__draw_board(self.__player_service)
        self.__display_hits_board()
        print(self.__game_over_message)


    def __multiplayer_mode(self):
        self.__reset_services()
        if self.__initialize_planes():
            return
        self.__clear_screen()
        self.__main_loop()
        self.__clear_screen()
        self.__draw_board(self.__player_service)
        self.__display_hits_board()
        print(self.__game_over_message)


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


    def __graphical_main_menu(self):
        if self.__active_gui:
            for option_index in range(0, len(self.__menu_options)):
                self.__display_menu_option(self.__font_size, self.__menu_options[option_index], option_index)
            pygame.display.update()

            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_1, pygame.K_s]:
                            self.__singleplayer_mode()
                        if event.key in [pygame.K_2, pygame.K_m]:
                            self.__multiplayer_mode()
                        if event.key in [pygame.K_ESCAPE, pygame.K_0]:
                            return


    def __main_menu(self):
        self.__graphical_main_menu()
        self.__console_main_menu()


    def run(self):

        self.__ui_selection()
        self.__main_menu()

        if self.__interrupted_program == False:
            self.__clear_screen()
            self.__draw_board(self.__player_service)
            self.__display_hits_board()
            print(self.__game_over_message)

import unittest
from repository import Repository
from validation import PlaneValidator
from service import PlaneService
from errors import PlaneError

class TestPlaneService(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__repository = Repository()
        self.__validator = PlaneValidator()
        self.__enemy_plane_repository = Repository()
        self.__service = PlaneService(self.__repository, self.__validator)
        self.__enemy_service = PlaneService(self.__enemy_plane_repository, self.__validator)
        self.__service.set_opponent(self.__enemy_service)
        self.__enemy_service.set_opponent(self.__service)
        self.__enemy_service.add_plane(3, 3, "up")
        self.__enemy_service.add_plane(0, 7, "up")
        
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    
    def test_add_plane__valid_plane__repository_with_plane(self):
        x_coordinate = 3
        y_coordinate = 3
        orientation = "up"
        self.__service.add_plane(x_coordinate, y_coordinate, orientation)
        self.assertEqual(self.__repository.get_size(), 1)
        
        
    def test_add_plane__invalid_plane__plane_error(self):
        x_coordinate = -1
        y_coordinate = 11
        orientation = "up"
        with self.assertRaises(PlaneError):
            self.__service.add_plane(x_coordinate, y_coordinate, orientation)

    
    def test_attack_opponent__valid_target_coordinates__updated_hits_board(self):
        x_coordinate = 3
        y_coordinate = 3
        
        self.__service.attack_opponent(x_coordinate, y_coordinate)
        hits_board = self.__service.get_hits_board()
        
        self.assertEqual(hits_board.get_value_of_position_x_y(x_coordinate, y_coordinate), 'X')
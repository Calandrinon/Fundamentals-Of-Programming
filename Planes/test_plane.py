from domain import *

def test_plane(orientation):
    board = Board()
    some_plane = Plane(3, 3, orientation, board)

    surface_positions = some_plane.get_surface_positions()

    for position in surface_positions:
        board.set_value_of_position_x_y(position[0], position[1], '#')

    print(surface_positions)
    print(board) 
    print("\n"*3)

test_plane("up")
test_plane("down")
test_plane("left")
test_plane("right")

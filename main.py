from ui import UI
from service import PlayerService, ComputerService
from repository import Repository
from validation import PlaneValidator


def main():
    plane_validator = PlaneValidator()
    
    plane_repository_player = Repository()
    plane_repository_computer = Repository()
    
    player_service = PlayerService(plane_repository_player, plane_validator)
    computer_service = ComputerService(plane_repository_computer, plane_validator)
    
    player_service.set_opponent(computer_service)
    computer_service.set_opponent(player_service)
    
    ui = UI(player_service, computer_service)
    ui.run()
    
main()

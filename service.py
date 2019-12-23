from domain import Plane

class PlaneService:
    
    def __init__(self, repository, validator):
        self.repository = repository
        self.validator = validator
        
    
    def add_plane(self, position_x, position_y):
        """
            Adds a plane to the repository of planes.
            
            Input:
                - position_x - integer
                - position_y - integer
        """
        
        
        

class ComputerService(PlaneService):
    pass


class PlayerService(PlaneService):
    pass

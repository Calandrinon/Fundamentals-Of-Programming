from domain import Plane

class PlaneValidator(object):
    
    def validate_plane(self, plane):
        if not isinstance(plane, Plane):
            raise ValueError("This is not a plane!")
        
        
    
    




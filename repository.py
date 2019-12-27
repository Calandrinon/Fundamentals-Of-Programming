from errors import RepoError

class Repository:
    
    def __init__(self):
        self.__list = []
    
    
    def add(self, element):
        """
        if element in self.__list:
            raise RepoError("The object is already in the container!")
        """
        
        self.__list.append(element)
    
    """
    def delete(self, element):
        if element not in self.__list:
            raise RepoError("The object cannot be deleted because it is not in the list!")
        
        for index in range(0, len(self.__list)):
            if self.__list[index] == element:
                del self.__list[index]
                return
    """
    
    def get_container(self):
        return self.__list
    
    
    def get_size(self):
        return len(self.__list)
    
    
    def clear(self):
        self.__list.clear()
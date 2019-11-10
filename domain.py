class Movie:

    def __init__(self, movieID, title, description, genre):
        self.__movieID = movieID
        self.__title = title
        self.__description = description
        self.__genre = genre

    def get_movieID(self):
        return self.__movieID

    def set_movieID(self, new_movieID):
        self.__movieID = new_movieID

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title

    def get_description(self):
        return self.__description

    def set_description(self, new_description):
        self.__description = new_description

    def get_genre(self):
        return self.__genre

    def set_genre(self, new_genre):
        self.__genre = new_genre


class Client:
    def __init__(self, clientID, name):
        self.__clientID = clientID
        self.__name = name

    def get_clientID(self):
        return self.__clientID

    def set_clientID(self, new_clientID):
        self.__clientID = new_clientID

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

class Rental:
    pass

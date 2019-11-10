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
    pass

class Rental:
    pass

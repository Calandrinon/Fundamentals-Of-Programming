class Student:

    def __init__(self, id, name, group):
        self.id = id
        self.name = name
        self.group = group

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_name(self):
        return self.name

    def get_group(self):
        return self.group

    def set_group(self, new_group):
        self.group = new_group

    def print(self):
        print("[Name: {}, ID: {}, Group: {}]".format(self.name, self.id, self.group))

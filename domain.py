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
        print("Name: {}".format(self.name))
        print("ID: {}".format(self.id))
        print("Group: {}".format(self.group))
        print("\n")

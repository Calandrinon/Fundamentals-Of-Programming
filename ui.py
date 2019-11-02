from services import *

class UI:
    def add(list_of_students):
        Validation.check_list_of_students(list_of_students)
        id = input("Enter the student's ID: ")
        Validation.check_id(id)
        name = input("Enter the student's name: ")
        group = input("Enter the student's group number: ")
        Validation.check_group(group)

        Services.add_student_to_list(list_of_students, id, name, group)

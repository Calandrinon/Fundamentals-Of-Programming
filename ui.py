from services import *

class UI:
    def clear_screen():
        print("\n"*200)

    def print_options():
        print("\n")
        print("0.Exit the program.\n")
        print("1.Add a new student to the list. Student data is read from the console.\n")
        print("2.Show the list of students on the console.\n")
        print("3.Filter the list so that students in a given group are deleted from the list.\n")
        print("4.Undo the last operation that modified program data. This step can be repeated.\n")
        print("\n\n")

    def add(list_of_students):
        Validation.check_list_of_students(list_of_students)

        id = input("Enter the student's ID: ")

        try:
            id = int(id)
        except Exception as e:
            print(e)

        Validation.check_id(id)

        name = input("Enter the student's name: ")

        group = input("Enter the student's group number: ")

        try:
            group = int(group)
        except Exception as e:
            print(e)

        Validation.check_group(group)

        Services.add_student_to_list(list_of_students, id, name, group)

    def list_students(list_of_students):
        Validation.check_list_of_students(list_of_students)

        if len(list_of_students) == 0:
            print("The list of students is empty!\n")
            return

        for student in list_of_students:
            student.print()

        print("\n")

    def filter(list_of_students):
        Validation.check_list_of_students(list_of_students)

        if len(list_of_students) == 0:
            print("The list of students is empty!\n")
            return

        group = input("Choose the student group that will be deleted: ")

        try:
            group = int(group)
        except:
            pass

        Validation.check_group(group)

        Services.filter_student_list(list_of_students, group)

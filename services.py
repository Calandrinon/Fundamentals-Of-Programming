from domain import Student
from random import randint

class Services:

    def add_student_to_list(list_of_students, id, name, group, operation_history):
        """
        Adds a new student to the list of students with the given parameters
        as information.

        Input:
            - list_of_students - A list which only contains instances of the
                                 class Student
            - id - An integer
            - name - A string which contains the name of the student
            - group - An integer which represents the group number of the student
        """

        new_student = Student(id, name, group)
        list_of_students.append(new_student)
        operation_history.append(("add", new_student))

    def filter_student_list(list_of_students, group, operation_history):
        """
        Removes all students from the group "group"

        Input:
            - list_of_students - A list which only contains instances of the
                                 class Student
            - group - An integer which represents the number of a group of students
            - buffer_filter_operations - A list which contains lists of tuples with elements
            that have been removed and their position before they were removed.
        """

        new_list_of_students = []
        new_list_in_history = []
        student_index = 0

        for student in list_of_students:
            if student.get_group() != group:
                new_list_of_students.append(student)
            else:
                new_list_in_history.append((student_index, student))
            student_index += 1

        list_of_students[:] = new_list_of_students
        operation_history.append(("filter", new_list_in_history))

    def undo_add(list_of_students, operation_history):
        list_of_students.pop()

    def undo_filter(list_of_students, operation_history):
        for student in operation_history[-1][1]:
            list_of_students.insert(student[0], student[1])

    def generate_entries(list_of_students, number_of_entries):
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown",
        "Davis", "Miller", "Wilson", "Moore", "Taylor"]

        first_names = ["Oliver", "George", "Harry", "Noah", "Jack", "Charlie",
        "Leo", "Jacob", "Freddie", "Alfie", "Olivia", "Amelia", "Isla", "Ava",
        "Emily", "Sophia", "Grace", "Mia", "Poppy", "Ella"]

        for entry in range(0, number_of_entries):
            first_name_generated = first_names[randint(0, len(first_names) - 1)]
            last_name_generated = last_names[randint(0, len(last_names) - 1)]
            generated_student = Student(randint(1, 100000), first_name_generated + " " + last_name_generated, randint(1, 1000))
            list_of_students.append(generated_student)

class Validation:

    def check_list_of_students(list_of_students):
        for student in list_of_students:
            if not isinstance(student, Student):
                raise Exception("The list should only contain students!\n")


    def check_id(id):
        if not isinstance(id, int):
            raise Exception("The student's ID should be an integer!\n")


    def check_group(group_number):
        if not (isinstance(group_number, int) and group_number > 0):
            raise Exception("The student's group number should be a positive integer!\n")

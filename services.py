from domain import Student

class Services:

    def add_student_to_list(list_of_students, id, name, group):
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

    def filter_student_list(list_of_students, group):
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

        for student in list_of_students:
            if student.get_group() != group:
                new_list_of_students.append(student)

        list_of_students[:] = new_list_of_students

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

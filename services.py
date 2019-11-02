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

class Validation:
    def check_list_of_students(list_of_students):
        for student in list_of_students:
            if not isinstance(student, Student):
                raise Exception("The list should only contain students!")

    def check_id(id):
        if not isinstance(id, int):
            raise Exception("The student's ID should be an integer!")

    def check_group(group_number):
        if not (isinstance(group_number, int) and group_number > 0):
            raise Exception("The student's group number should be a positive integer!")

from services import *
from domain import Student

class Tests:

    def __assert_students(student1, student2):
        assert(student1.get_id() == student2.get_id())
        assert(student1.get_name() == student2.get_name())
        assert(student1.get_group() == student2.get_group())

    def __assert_lists_of_students(list_of_students1, list_of_students2):
        assert(len(list_of_students1) == len(list_of_students2))

        for student_index in range(0, len(list_of_students1)):
            Tests.__assert_students(list_of_students1[student_index], list_of_students2[student_index])

    @staticmethod
    def addStudentToList__ValidStudent__IsInTheList():
        list_of_students = []
        expected_result = [Student(5, "Abc", 917)]
        history = []
        Services.add_student_to_list(list_of_students, 5, "Abc", 917, history)
        Tests.__assert_lists_of_students(list_of_students, expected_result)

    @staticmethod
    def filterStudentList__Group125__ListWithoutTheStudentsOfGroup125():
        history = []
        some_student = Student(17, "ef", 128)
        removed_student1 = Student(1725, "abcdef", 125)
        removed_student2 = Student(333, "aaaaa", 125)
        list_of_students = [removed_student1, some_student, removed_student2]
        expected_result = [some_student]
        Services.filter_student_list(list_of_students, 125, history)
        Tests.__assert_lists_of_students(list_of_students, expected_result)

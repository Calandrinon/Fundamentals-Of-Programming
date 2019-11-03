from services import *
from domain import Student

class Tests:
    def assert_students(student1, student2):
        assert(student1.get_id() == student2.get_id())
        assert(student1.get_name() == student2.get_name())
        assert(student1.get_group() == student2.get_group())

    def assert_lists_of_students(list_of_students1, list_of_students2):
        assert(len(list_of_students1) == len(list_of_students2))

        for student_index in range(0, len(list_of_students1)):
            Tests.assert_students(list_of_students1[student_index], list_of_students2[student_index])

    def test_add_student_to_list():
        list_of_students = []
        Services.add_student_to_list(list_of_students, 5, "Abc", 917)
        Tests.assert_lists_of_students(list_of_students, [Student(5, "Abc", 917)])

    def test_filter_student_list():
        buffer = []
        some_student = Student(17, "ef", 128)
        removed_student1 = Student(1725, "abcdef", 125)
        removed_student2 = Student(333, "aaaaa", 125)
        list_of_students = [removed_student1, some_student, removed_student2]
        Services.filter_student_list(list_of_students, 125, buffer)
        Tests.assert_lists_of_students(list_of_students, [some_student])
        for buffer_sublist in buffer:
            for student in buffer_sublist:
                student[0].print()
                print(student[1])

from services import *
from domain import Student

def assert_students(student1, student2):
    assert(student1.get_id() == student2.get_id())
    assert(student1.get_name() == student2.get_name())
    assert(student1.get_group() == student2.get_group())

def assert_lists_of_students(list_of_students1, list_of_students2):
    assert(len(list_of_students1) == len(list_of_students2))

    for student_index in range(0, len(list_of_students1)):
        assert_students(list_of_students1[student_index], list_of_students2[student_index])

def test_add_student_to_list():
    list_of_students = []
    add_student_to_list(list_of_students, 5, "Abc", 917)
    assert_lists_of_students(list_of_students, [Student(5, "Abc", 917)])

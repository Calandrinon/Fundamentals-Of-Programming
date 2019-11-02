from ui import *
from tests import *

"""
    TODO: Add the functions <add>, <list> and <filter>
    TODO: Add data validation
    TODO: Add <undo> function
"""

def run_tests():
    Tests.test_add_student_to_list()

def main():
    list_of_students = []
    menu_option = [UI.add]

    while True:
        option = input("Enter an option: ")

        try:
            option = int(option)

            if option == 0:
                return

            if option >= 1 and option <= 4:
                menu_option[option - 1](list_of_students)
        except ValueError:
            print("Enter an integer between 0 and 4!")
        except Exception as e:
            print(e)

run_tests()
main()

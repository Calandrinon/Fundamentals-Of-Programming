from ui import *
from tests import *
from services import Services

"""
    TODO: Add the functions <add>, <list> and <filter>
    TODO: Add data validation
    TODO: Add <undo> function
"""

def run_tests():
    Tests.test_add_student_to_list()
    Tests.test_filter_student_list()

def main():
    list_of_students = []
    operation_history = []
    menu_option = [UI.add, UI.list_students, UI.filter, UI.undo]
    UI.clear_screen()
    Services.generate_entries(list_of_students, 10)

    while True:
        UI.print_options()
        option = input("Enter an option: ")
        UI.clear_screen()

        try:
            option = int(option)

            if option < 0:
                print("You have entered a negative value!\n")
                continue

            if option == 0:
                return

            menu_option[option - 1](list_of_students, operation_history)
        except (ValueError, IndexError):
            print("Enter an integer between 0 and 4!\n")
        except Exception as e:
            print(e)


run_tests()
main()

from ui import *
from non_ui import *
from tests import *

"""
    TODO: Add "help" function.
"""

def run_all_tests():
    print("Tests:")
    test_sum_of_transactions_by_type()
    test_list_balance()
    test_list_transaction_by_value_size()
    test_list_transaction_by_type()
    test_write_transactions_file()
    test_read_transactions_file()
    test_list_transaction()
    test_edit_transaction()
    test_remove_transaction()
    test_add_transaction()
    test_transaction_class()
    test_split_command()
    test_insert_transaction()
    print("\n\n\nTests are done!\n\n\n\n\n")

def main():
    account_transactions = read_transactions_file()
    commands = {"add":ui_add, "insert":ui_insert, "remove":ui_remove,
    "replace":ui_replace, "list":ui_list, "clear":ui_clear}

    while True:
        command = input("###: ")
        parameters = split_command(command)
        number_of_parameters = len(parameters)
        clear_screen()

        if number_of_parameters == 0:
            print("Please enter a command...")
            continue

        if parameters[0] == "quit" or parameters[0] == "exit":
            break

        try:
            commands[parameters[0]](account_transactions, parameters)
        except KeyError:
            print("That command doesn't exist! This is the list of commands: add, insert, remove, replace, list, clear")
            #ui_help()

    write_transactions_file(account_transactions)

clear_screen()
run_all_tests()
main()

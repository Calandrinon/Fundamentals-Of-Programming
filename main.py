from ui import *
from non_ui import *
from tests import *

"""
    TODO: Implement "undo" function.
    TODO: Replace print statements from UI functions with raised exceptions.
    TODO: Add "help" function.
    TODO: Replace obscure element deletion lines in <remove_transaction> and
          <filter_transactions> with the slice syntax for the whole array [:]
"""

def run_all_tests():
    print("Tests:")
    test_filter_transactions()
    test_maximum_transferred_value()
    test_sum_of_transactions_by_type()
    test_list_balance()
    test_list_transaction_by_value_size()
    test_list_transaction_by_type()
    #test_write_transactions_file()
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
    account_transactions = read_transactions_file("transactions_file.txt")
    write_transactions_file(account_transactions, "operation_0.txt")
    number_of_executed_operations = 0
    last_operation_number = 0
    save_last_operation_number(last_operation_number)
    commands = {"add":ui_add, "insert":ui_insert, "remove":ui_remove,
    "replace":ui_replace, "list":ui_list, "clear":ui_clear, "sum":ui_sum,
    "max":ui_max, "filter":ui_filter, "undo":ui_undo}

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
            last_operation_number = get_last_operation_number()
            commands[parameters[0]](account_transactions, parameters)

            if parameters[0] not in ["list", "clear", "sum", "max", "undo"]:
                last_operation_number += 1
                if last_operation_number > number_of_executed_operations:
                    number_of_executed_operations += 1
                save_last_operation_number(last_operation_number)
                write_transactions_file(account_transactions, "operation_" + str(last_operation_number) + ".txt")
        except KeyError:
            print("That command doesn't exist! This is the list of commands: \nadd, insert, remove, replace, list, clear, sum, max, filter")
            #ui_help()

    write_transactions_file(account_transactions, "transactions_file.txt")
    delete_operation_files(number_of_executed_operations)

clear_screen()
run_all_tests()
main()

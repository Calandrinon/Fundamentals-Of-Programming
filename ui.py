import validation
from non_ui import clear_screen
from operations import *
from transaction import Transaction

def ui_add(account_transactions, parameters):
    number_of_parameters = len(parameters)
    ### In case the user doesn't enter 3 parameters
    if number_of_parameters != 4:
        print("Invalid number of parameters!")
        ui_print_specification_function_add()
        return

    try:
        #validate_add_command_parameters()
        add_transaction(account_transactions, int(parameters[1]), parameters[2], parameters[3])
    except Exception as e:
        print(e)
        ui_print_specification_function_add()

def ui_insert(account_transactions, parameters):
    number_of_parameters = len(parameters)
    ### In case the user doesn't enter 4 parameters
    if number_of_parameters != 5:
        print("Invalid number of parameters!")
        ui_print_specification_function_insert()
        return

    try:
        #validate_insert_command_parameters()
        insert_transaction(account_transactions, int(parameters[1]), int(parameters[2]), parameters[3], parameters[4])
    except Exception as e:
        print(e)
        ui_print_specification_function_insert()

def ui_remove(account_transactions, parameters):
    number_of_parameters = len(parameters)
    ### In case the user doesn't enter 1 parameter or 3 parameters
    if not(number_of_parameters == 2 or number_of_parameters == 4):
        print("Invalid number of parameters!")
        ui_print_specification_function_remove()
        return

    try:
        if number_of_parameters == 2:
            is_parameter_1_int = True
            try:
                int(parameters[1])
            except ValueError:
                is_parameter_1_int = False

            if is_parameter_1_int:
                remove_transaction(account_transactions, int(parameters[1]), int(parameters[1]), ["in", "out"])
            else:
                if parameters[1] not in ["in", "out"]:
                    clear_screen()
                    print("You should enter one of the following values in the 'type' parameter: 'in', 'out'")
                else:
                    remove_transaction(account_transactions, 1, 31, [parameters[1]])
        elif number_of_parameters == 4:
            if parameters[2] != "to":
                ui_print_specification_function_remove()
                return
            remove_transaction(account_transactions, int(parameters[1]), int(parameters[3]), ["in", "out"])
    except Exception as e:
        print(e)

def ui_replace(account_transactions, parameters):
    number_of_parameters = len(parameters)
    ### In case the user doesn't enter exactly 5 parameters
    if number_of_parameters != 6:
        print("Invalid number of parameters!")
        ui_print_specification_function_replace()
        return

    if parameters[4] != "with":
        print("Wrong usage!")
        ui_print_specification_function_replace()
        return

    try:
        edit_transaction(account_transactions, int(parameters[1]), parameters[2], parameters[3], int(parameters[5]))
    except Exception as e:
        print(e)
        ui_print_specification_function_replace()

def ui_list(account_transactions, parameters):
    number_of_parameters = len(parameters)
    clear_screen()

    if number_of_parameters == 1:
        list_transaction(account_transactions)
    elif number_of_parameters == 2:
        try:
            list_transaction_by_type(account_transactions, parameters[1])
        except Exception as e:
            print(e)
            ui_print_specification_function_list()
    elif number_of_parameters == 3:
        if parameters[1] != "balance":
            try:
                list_transaction_by_value_size(account_transactions, parameters[1], int(parameters[2]))
            except Exception as e:
                print(e)
                ui_print_specification_function_list()
        else:
            try:
                list_balance(account_transactions, int(parameters[2]))
            except Exception as e:
                print(e)
                ui_print_specification_function_list()
    else:
        print("Wrong number of parameters!")
        ui_print_specification_function_list()

def ui_clear(account_transactions, parameters):
    ### The account_transactions parameter is not useful in this function
    ### but we create this in order to be able to insert this function into a
    ### dictionary which will associate the function with the command entered
    ### by the user as input.
    number_of_parameters = len(parameters)

    if number_of_parameters > 1:
        print("The command 'clear' takes no parameters!")
        return

    clear_screen()

def ui_print_specification_function_add():
    """
        Prints the usage instructions of the function <add>.
    """
    usage_warning_message = "\n\nUsage:\nadd <value> <type> <description>\n\nAdds to a transaction list a new transaction on the current day.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_insert():
    """
        Prints the usage instructions of the function <insert>.
    """
    usage_warning_message = "\n\nUsage:\ninsert <day> <value> <type> <description>\n\nAdds to a transaction list a new transaction on the day specified in the parameter 'day'.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_remove():
    """
        Prints the usage instructions of the function <remove>.
    """
    usage_warning_message = "\n\nUsage:\nremove <day>\nremove <start day> to <end day>\nremove <type>\n\nThis function removes transactions from the transaction list, based on the\nentered parameters.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_replace():
    """
        Prints the usage instructions of the function <replace>.
    """
    usage_warning_message = "\n\nUsage:\nreplace <day> <type> <description> with <value>\n\nThis function edits the amount of money of a specific transaction made on\nthe mentioned day, based on the entered parameters.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_list():
    """
        Prints the usage instructions of the function <list>.
    """
    usage_warning_message = "\n\nUsage:\nlist\nlist <type>\nlist [ < | = | > | <= | >= ] <value>\nlist balance <day>\n\nThis function lists the transactions specified by the user in the parameters.\n\n"
    print(usage_warning_message)

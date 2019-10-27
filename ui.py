from non_ui import clear_screen
from operations import *
from transaction import *

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
        try:
            list_transaction(account_transactions)
        except Exception as e:
            print(e)
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

def ui_sum(account_transactions, parameters):
    number_of_parameters = len(parameters)
    ### In case the user doesn't enter exactly 1 parameter
    if number_of_parameters != 2:
        print("The command 'sum' takes 1 parameter")
        ui_print_specification_function_sum()
        return

    try:
        print("The sum of all '{}' transactions of this month is: {}".format(parameters[1], sum_of_transactions_by_type(account_transactions, parameters[1])))
    except Exception as e:
        print(e)
        ui_print_specification_function_sum()

def ui_max(account_transactions, parameters):
    number_of_parameters = len(parameters)
    ### In case the user doesn't enter exactly 2 parameters
    if number_of_parameters != 3:
        print("The command 'max' takes 2 parameters.")
        ui_print_specification_function_max()
        return

    try:
        maximum_transaction = maximum_transferred_value(account_transactions, parameters[1], int(parameters[2]))
        print("The transaction of type '{}' made on day {} has the maximum value of {}.".format(parameters[1], parameters[2], maximum_transaction.get_value()))
        maximum_transaction.print()
    except Exception as e:
        print(e)
        ui_print_specification_function_max()

def ui_filter(account_transactions, parameters):
    number_of_parameters = len(parameters)
    try:
        if number_of_parameters == 2:
            filter_transactions(account_transactions, parameters[1], 0)
        elif number_of_parameters == 3:
            filter_transactions(account_transactions, parameters[1], int(parameters[2]))
        else:
            print("Wrong usage!")
            ui_print_specification_function_filter()
    except Exception as e:
        print(e)
        ui_print_specification_function_filter()

def ui_undo(account_transactions, parameters):
    undo_last_operation(account_transactions)

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

def ui_print_specification_function_sum():
    """
        Prints the usage instructions of the function <sum>.
    """
    usage_warning_message = "\n\nUsage:\nsum <type>\n\nThis function lists the transactions specified by the user in the parameters.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_max():
    """
        Prints the usage instructions of the function <max>.
    """
    usage_warning_message = "\n\nUsage:\nmax <type> <day>\n\nThis function lists the transaction of type <type> made on day <day> with\nthe maximum transferred value.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_filter():
    """
         Prints the usage instructions of the function <max>.
    """
    usage_warning_message = "\n\nUsage:\nfilter <type>\nfilter <type> <value>\n\nThis function filters the transactions of the month based on the entered parameters.\n If the user enters 2 parameters, the remaining transactions after the filtering\nwill be those with the value less that the entered parameter <value>.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_clear():
    """
        Prints the usage instructions of the function <clear>.
    """
    usage_warning_message = "\n\nUsage:\nclear\n\nThis function clears the screen.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_help():
    usage_warning_message = "\n\nUsage:\nhelp\nhelp <command name>\n\nThis function prints the list of commands and the description of the command with the name <command name>.\n\n"
    print(usage_warning_message)

def ui_print_specification_function_quit():
    usage_warning_message = "\n\nUsage:\nquit\nexit\n\nThis command terminates the program.\n\n"
    print(usage_warning_message)

def ui_help(account_transactions, parameters):
    """
        Prints to the user the usage of a specific command.
    """
    number_of_parameters = len(parameters)
    if number_of_parameters == 1:
        print("This is the list of commands: \nquit, exit, help, add, insert, remove, replace, list, clear, sum, max, filter")
    elif number_of_parameters == 2:
        specifications = {"add":ui_print_specification_function_add,
        "insert":ui_print_specification_function_insert,
        "remove":ui_print_specification_function_remove,
        "replace":ui_print_specification_function_replace,
        "list":ui_print_specification_function_list,
        "sum":ui_print_specification_function_sum,
        "max":ui_print_specification_function_max,
        "filter":ui_print_specification_function_filter,
        "clear":ui_print_specification_function_clear,
        "help":ui_print_specification_function_help,
        "exit":ui_print_specification_function_quit,
        "quit":ui_print_specification_function_quit}

        try:
            specifications[parameters[1]]()
        except KeyError:
            message = "The command '{}' does not exist!".format(parameters[1])
            raise Exception(message)
    else:
        message = "'help' takes only 1 parameter or no parameters!".format(parameters[1])
        raise Exception(message)

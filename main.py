import datetime

"""
    TODO: Add <remove> function and test it.
"""

class Transaction:
    def __init__(self, date, value, type, description):
        self.date = date
        self.value = value
        self.type = type
        self.description = description

    def get_date(self):
        return self.date

    def get_value(self):
        return self.value

    def get_type(self):
        return self.type

    def get_description(self):
        return self.description

    def set_date(self, date):
        self.date = date

    def set_value(self, value):
        self.value = value

    def set_type(self, type):
        self.type = type

    def set_description(self, description):
        self.description = description

    def print(self):
        print("[{}, {}, {}, {}]".format(self.get_date(), self.get_value(), self.get_type(),
        self.get_description()))

def ui_add(transaction_list, value, type, description):
    """
    Adds to a transaction list a new transaction on the current day.
    Input:
        > transaction_list - The list of transactions.

        > value - A positive integer which represents the amount of
                  money that was transferred

        > type - A string which represents the type of the transaction.
                 It can be one of the following:
                        * in - a sum of money was transferred into the
                               account
                        * out - a sum of money was transferred from the
                               account to somewhere else

        > description - A description of the transaction:
                        E.g: "add 100 out PIZZA"
    """

    if value < 0:
        print("You should have entered a positive integer as a value.")
        print("The value will be automatically made positive.")

    if isinstance(value, float):
        print("You should have entered an integer as a value, not a float.")
        print("The value will be converted to an integer automatically.")

    if type not in ["in", "out"]:
        message = "The parameter 'type' should have one of the following values: 'in', 'out'."
        raise Exception(message)

    if not isinstance(description, str):
        message = "The parameter 'description' should be a string."
        raise Exception(message)

    value = abs(int(value))
    current_date = datetime.datetime.today().day ### The current date when the
                                                 ### transaction is made.

    new_transaction = Transaction(current_date, value, type, description)
    transaction_list.append(new_transaction)

def ui_insert(transaction_list, day, value, type, description):
    """
    Adds to a transaction list a new transaction on the day specified in the
    parameter "day".
    Input:
        > transaction_list - The list of transactions.

        > day - The day when the transaction has been made.

        > value - A positive integer which represents the amount of
                  money that was transferred.

        > type - A string which represents the type of the transaction.
                 It can be one of the following:
                        * in - a sum of money was transferred into the
                               account
                        * out - a sum of money was transferred from the
                               account to somewhere else

        > description - A description of the transaction:
                        E.g: "insert 25 100 in SALARY"
    """
    if day < 1 or day > 31 or isinstance(day, float):
        message = "The day parameter should be an integer value between 1 and 31!"
        raise Exception(message)

    ui_add(transaction_list, value, type, description)
    transaction_list[-1].set_date(day)

def ui_print_transactions(transaction_list):
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    for transaction in transaction_list:
        transaction.print()

def ui_remove(transaction_list, start_day, end_day, types):
    """
    This function removes transactions from the transaction list, based on the
    entered parameters.
    Input:
        > transaction_list - The list of transactions.

        > start_day, end_day - These are the parameters which represent the
                               transactions made in the interval of days with
                               the boundaries [start_day, end_day]. All the
                               transactions made in this interval of days will
                               be deleted from the list.

                             - The "types" parameter is a list with all the
                               types of transactions that will be deleted.
    """

    if start_day < 1 or start_day > 31 or end_day < 1 or end_day > 31 or start_day > end_day or isinstance(start_day, float) or isinstance(end_day, float):
        message = "The days should be positive integers between 1 and 31.\nThe starting day should be smaller or equal to the end day."
        raise Exception(message)

    if not("in" in types or "out" in types):
        message = "The types of the transactions are 'in' and 'out'."
        raise Exception(message)

    blank_transaction = Transaction(0, 0, "none", "deleted")
    for transaction_index in range(0, len(transaction_list)):
        transaction_day = transaction_list[transaction_index].get_date()
        transaction_type = transaction_list[transaction_index].get_type()
        if transaction_day >= start_day and transaction_day <= end_day and transaction_type in types:
            transaction_list[transaction_index] = blank_transaction

    changes_made = True
    while len(transaction_list) > 0 and changes_made:
        initial_length_of_list = len(transaction_list)
        try:
            transaction_list.remove(blank_transaction)
        except ValueError:
            break
        final_length_of_list = len(transaction_list)

        if final_length_of_list < initial_length_of_list:
            changes_made = True
        else:
            changes_made = False

def split_command(command):
    """
    Gets a string (in this case the command that is given as an input from
    the keyboard by the user) and splits it in multiple tokens.
    Input:
        > string (command)

    Output:
        A list with all the tokens in the string "command".
    """
    list_of_tokens = command.split(" ")
    while "" in list_of_tokens:
        list_of_tokens.remove("") ### In case the user enters too many spaces
                                  ### between the arguments of the command.
    return list_of_tokens

def ui_print_specification_function_add():
    """
        Prints the usage instructions of the function <ui_add>.
    """
    usage_warning_message = "\n\nUsage:\nAdds to a transaction list a new transaction on the current day.\nInput:\n\t> value - A positive integer which represents the amount of\n\tmoney that was transferred\n\t> type - A string which represents the type of the transaction.\n\tIt can be one of the following:\n\t\t* in - a sum of money was transferred into the\n\t\taccount\n\t\t* out - a sum of money was transferred from the\n\t\taccount to somewhere else\n\t> description - A description of the transaction:\n\t\tE.g: 'add 100 out PIZZA'\n\n\n"
    print(usage_warning_message)

def ui_print_specification_function_insert():
    """
        Prints the usage instructions of the function <ui_insert>.
    """
    usage_warning_message = "\n\nUsage:\nAdds to a transaction list a new transaction on the day specified in the parameter 'day'.\nInput:\n\t> day - The day when the transaction has been made.\n\t> value - A positive integer which represents the amount of\n\tmoney that was transferred\n\t> type - A string which represents the type of the transaction.\n\tIt can be one of the following:\n\t\t* in - a sum of money was transferred into the\n\t\taccount\n\t\t* out - a sum of money was transferred from the\n\t\taccount to somewhere else\n\t> description - A description of the transaction:\n\t\tE.g: 'add 100 out PIZZA'\n\n\n"
    print(usage_warning_message)
    pass

def clear_screen():
    print("\n"*200)

def test_remove():
    print("\n\n<ui_remove> function test running...")
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = []

    def assert_transaction_lists():
        assert(len(account_transactions) == len(correct_final_result))

        for transaction_index in range(0, len(correct_final_result)):
            assert(account_transactions[transaction_index].get_date() == correct_final_result[transaction_index].get_date())
            assert(account_transactions[transaction_index].get_value() == correct_final_result[transaction_index].get_value())
            assert(account_transactions[transaction_index].get_type() == correct_final_result[transaction_index].get_type())
            assert(account_transactions[transaction_index].get_description() == correct_final_result[transaction_index].get_description())

    ### Test 1
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = []
    ui_remove(account_transactions, 1, 31, ["in", "out"])
    assert_transaction_lists()

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(25, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    ui_remove(account_transactions, 1, 20, ["in", "out"])
    assert_transaction_lists()

    ### Test 3
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    ui_remove(account_transactions, 1, 10, ["in", "out"])
    assert_transaction_lists()

    ### Test 4
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    ui_remove(account_transactions, 1, 20, ["in"])
    assert_transaction_lists()

    ### Test 5
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(21, 100, "in", "gift")]
    ui_remove(account_transactions, 1, 31, ["out"])
    assert_transaction_lists()

    ### Test 6
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_remove(account_transactions, 1111, 25, ["in"])
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 7
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_remove(account_transactions, 1111.5, 25, ["out"])
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 8
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_remove(account_transactions, 2.5, 25, ["out"])
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 9
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_remove(account_transactions, -2, 25, ["out"])
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 10
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_remove(account_transactions, 0, 31, ["in"])
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 11
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_remove(account_transactions, 0, 32, ["crap"])
    except Exception as e:
        print(e)

    ### Test 11
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_remove(account_transactions, 1, 5, ["crap"])
    except Exception as e:
        print(e)
    assert_transaction_lists()

    print("<ui_remove> function test passed.\n\n")

def test_insert():
    print("\n\n<ui_insert> function test running...")
    account_transactions = []
    correct_result = []

    def assert_last_transactions():
        assert(account_transactions[-1].get_date() == correct_result[-1].get_date())
        assert(account_transactions[-1].get_value() == correct_result[-1].get_value())
        assert(account_transactions[-1].get_type() == correct_result[-1].get_type())
        assert(account_transactions[-1].get_description() == correct_result[-1].get_description())

    ### Test 1
    ui_insert(account_transactions, 24, 125, "in", "jacket")
    correct_result.append(Transaction(24, 125, "in", "jacket"))
    assert_last_transactions()

    ### Test 2
    try:
        ui_insert(account_transactions, -24, 125, "in", "jacket")
        correct_result.append(Transaction(24, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 3
    try:
        ui_insert(account_transactions, 24.5, 125, "in", "jacket")
        correct_result.append(Transaction(24, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 4
    try:
        ui_insert(account_transactions, 52, 125, "in", "jacket")
        correct_result.append(Transaction(24, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    print("<ui_insert> function test passed.\n\n")

def test_split_command():
    print("\n\n<split_command> function test running...")
    assert(split_command("add 100 out pizza") == ["add", "100", "out", "pizza"])
    assert(split_command("add     100      out   pizza") == ["add", "100", "out", "pizza"])
    assert(split_command("insert    515 in   cool") == ["insert", "515", "in", "cool"])
    print("<split_command> function test passed.\n\n")

def test_add():
    print("\n\n<ui_add> function test running...")
    account_transactions = []
    correct_result = []

    def assert_last_transactions():
        assert(account_transactions[-1].get_date() == correct_result[-1].get_date())
        assert(account_transactions[-1].get_value() == correct_result[-1].get_value())
        assert(account_transactions[-1].get_type() == correct_result[-1].get_type())
        assert(account_transactions[-1].get_description() == correct_result[-1].get_description())

    today = datetime.datetime.today().day
    test_value = 100
    test_type = "out"
    test_description = "pizza"

    ### Test 1
    ui_add(account_transactions, test_value, test_type, test_description)
    correct_result.append(Transaction(today, test_value, test_type, test_description))
    assert_last_transactions()

    ### Test 2
    ui_add(account_transactions, 125, "in", "jacket")
    correct_result.append(Transaction(today, 125, "in", "jacket"))
    assert_last_transactions()

    ### Test 3
    ui_add(account_transactions, -125, "in", "jacket")
    correct_result.append(Transaction(today, 125, "in", "jacket"))
    assert_last_transactions()

    ### Test 4
    ui_add(account_transactions, 125.56, "in", "jacket")
    correct_result.append(Transaction(today, 125, "in", "jacket"))
    assert_last_transactions()

    ### Test 5
    try:
        ui_add(account_transactions, 125, "blahblah", "jacket")
        correct_result.append(Transaction(today, 125, "blahblah", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 6
    try:
        ui_add(account_transactions, 125, "in", 123)
        correct_result.append(Transaction(today, 125, "in", 123))
        assert_last_transactions()
    except Exception as e:
        print(e)

    print("<ui_add> function test passed.\n\n")

def test_transaction_class():
    print("\n\n<Transaction> class test running...")
    today = datetime.datetime.today().day
    transaction = Transaction(today, 100, "out", "pizza")
    assert(transaction.get_date() == today)
    assert(transaction.get_value() == 100)
    assert(transaction.get_type() == "out")
    assert(transaction.get_description() == "pizza")
    print("<Transaction> class test passed.\n\n")

def run_all_tests():
    print("Tests:")
    test_remove()
    test_add()
    test_transaction_class()
    test_split_command()
    test_insert()
    print("\n\n\nTests are done!\n\n\n\n\n")

def main():
    account_transactions = []
    commands = ["quit", "exit", "add", "clear", "insert"]

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
        elif parameters[0] == "add":
            ### In case the user doesn't enter 3 parameters
            if number_of_parameters != 4:
                print("Invalid number of parameters!")
                ui_print_specification_function_add()
                continue

            try:
                ui_add(account_transactions, int(parameters[1]), parameters[2], parameters[3])
            except Exception as e:
                print(e)
                ui_print_specification_function_add()
            ui_print_transactions(account_transactions)
        elif parameters[0] == "insert":
            ### In case the user doesn't enter 4 parameters
            if number_of_parameters != 5:
                print("Invalid number of parameters!")
                ui_print_specification_function_insert()
                continue

            try:
                ui_insert(account_transactions, int(parameters[1]), int(parameters[2]), parameters[3], parameters[4])
            except Exception as e:
                print(e)
                ui_print_specification_function_insert()
            ui_print_transactions(account_transactions)
        elif parameters[0] == "clear":
            clear_screen()
        elif parameters[0] not in commands:
            print("That command doesn't exist! This is the list of commands: ", commands)

clear_screen()
run_all_tests()
main()

import datetime

"""
    TODO: Add a transaction saving system with files. Create transaction
          loading and saving functions.
    TODO: Write a big try-catch statement in <run_all_tests> and delete the
          try-catch statements in each of the small tests.
    TODO: Shorten the test functions.
    TODO: Check <ui_print_specification_function_remove> once again.
    TODO: Print specifications for list functions if the user enters Invalid
          parameters.
    TODO: Check for invalid inputs in <main> again and add exception handling.
    TODO: Check <ui_remove> function once again.
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
        print("[Day: {}, Sum: {}, Type of transaction: {}, Description: {}]".format(self.get_date(), self.get_value(), self.get_type(),
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

def ui_list(transaction_list):
    """
    Lists all the transactions made on the account.
    """
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    for transaction in transaction_list:
        transaction.print()

def ui_list_by_type(transaction_list, type):
    """
    Lists all the transactions with the specified type (in, out).
    Input:
        > type - The type of the transaction.
    """
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    for transaction in transaction_list:
        if transaction.get_type() == type:
            transaction.print()
    pass

def ui_list_by_value_size(transaction_list, condition, value):
    """
    Lists all the transactions with respect to the condition given as a
    parameter.
    E.g: list > 100
         - lists all transactions with the value greater than 100
    Input:
        > condition - The condition used for filtering the list.

        > value - The value which is compared with the values of the filtered
                  transactions.
    """
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    if condition not in ["<", ">", "<=", ">=", "="]:
        message = "The condition parameter should contain one of the following operands: <, >, =."
        raise Exception(message)

    for transaction in transaction_list:
        if condition == "<":
            if transaction.get_value() < value:
                transaction.print()
        elif condition == "<=":
            if transaction.get_value() <= value:
                transaction.print()
        elif condition == ">=":
            if transaction.get_value() >= value:
                transaction.print()
        elif condition == ">":
            if transaction.get_value() > value:
                transaction.print()
        else:
            if transaction.get_value() == value:
                transaction.print()

def ui_list_balance(transaction_list, day):
    """
    Computes the account’s balance on the day specified in the parameter.
    Input:
        > day
    """
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    if not isinstance(day, int):
        message = "The day parameter needs to be a positive integer between 1 and 31."
        raise Exception(message)

    in_transactions_sum = 0
    out_transactions_sum = 0

    for transaction in transaction_list:
        if transaction.get_date() <= day:
            if transaction.get_type() == "in":
                in_transactions_sum += transaction.get_value()
            else:
                out_transactions_sum += transaction.get_value()
    print("The balance is: ", in_transactions_sum - out_transactions_sum)

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

        > The "types" parameter is a list with all the
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

def ui_replace(transaction_list, day, type, description, value):
    """
    This function edits the amount of money of a specific transaction made on
    the mentioned day, based on the entered parameters.
    Input:
        > transaction_list - The list of transactions.

        > day - The day when the transaction was made.

        > type - A string which represents the type of the transaction.
                 It can be one of the following:
                        * in - a sum of money was transferred into the
                               account
                        * out - a sum of money was transferred from the
                               account to somewhere else

        > description - A description of the transaction:
                        E.g: "insert 25 100 in SALARY"

        > value - The amount of money involved in the transaction. In this
                  case, "value" will be the new amount of money assigned
                  to the transaction made on the day "day", with the type
                  and the description mentioned in the parameters.
    """

    if day < 1 or day > 31 or not isinstance(day, int):
        message = "The day parameter should be a positive integer between 1 and 31!"
        raise Exception(message)

    if not isinstance(value, int) or value <= 0:
        message = "The value parameter should be a positive integer!"
        raise Exception(message)

    if type not in ["in", "out"]:
        message = "The type parameter should have one of the following values: 'in', 'out'."
        raise Exception(message)

    for transaction in transaction_list:
        if transaction.get_date() == day and transaction.get_type() == type and transaction.get_description() == description:
            transaction.set_value(value)

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

def ui_print_specification_function_remove():
    """
        Prints the usage instructions of the function <ui_remove>.
    """
    usage_warning_message = "\n\nUsage:\nThis function removes transactions from the transaction list, based on the\nentered parameters.\nInput:\n\t> start_day, end_day - These are the parameters which represent the\n\ttransactions made in the interval of days with\n\tthe boundaries [start_day, end_day]. All the\n\ttransactions made in this interval of days will\n\tbe deleted from the list.\n\t> The 'types' parameter is a list with all the\n\ttypes of transactions that will be deleted.\n\t"
    print(usage_warning_message)

def ui_print_specification_function_replace():
    """
        Prints the usage instructions of the function <ui_replace>.
    """
    usage_warning_message = "\n\nUsage:\nThis function edits the amount of money of a specific transaction made on\nthe mentioned day, based on the entered parameters.\nInput:\n\t> day - The day when the transaction was made.\n\t> type - A string which represents the type of the transaction.\n\tIt can be one of the following:\n\t* in - a sum of money was transferred into the\n\t\taccount\n\t\t* out - a sum of money was transferred from the\n\t\taccount to somewhere else\n\t\t> description - A description of the transaction:\n\tE.g: 'insert 25 100 in SALARY'\n\t>description - A string which represents the description associated with the transaction.\n\t> value - The amount of money involved in the transaction. In this\n\tcase, 'value' will be the new amount of money assigned\n\tto the transaction made on the day 'day', with the type\n\tand the description mentioned in the parameters.\n\t"
    print(usage_warning_message)

def clear_screen():
    print("\n"*200)

def test_list():
    print("\n\n<ui_list> function test running...")
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    ui_list(account_transactions)
    print("<ui_list> function test passed.\n\n")

def test_replace():
    print("\n\n<ui_replace> function test running...")
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
    correct_final_result = [Transaction(19, 55, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    ui_replace(account_transactions, 19, "out", "pizza", 55)
    assert_transaction_lists()

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_replace(account_transactions, -19, "out", "pizza", 55)
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 3
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_replace(account_transactions, 5.5, "out", "pizza", 55)
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 4
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_replace(account_transactions, 5, "abcdef", "pizza", 55)
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 5
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_replace(account_transactions, 19, "out", "pizza", -12)
    except Exception as e:
        print(e)
    assert_transaction_lists()

    ### Test 6
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        ui_replace(account_transactions, 19, "out", "pizza", 12.5)
    except Exception as e:
        print(e)
    assert_transaction_lists()

    print("<ui_replace> function test passed.\n\n")

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
    test_list()
    test_replace()
    test_remove()
    test_add()
    test_transaction_class()
    test_split_command()
    test_insert()
    print("\n\n\nTests are done!\n\n\n\n\n")

def main():
    account_transactions = []
    commands = ["quit", "exit", "add", "clear", "insert", "remove", "replace", "list"]

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
        elif parameters[0] == "remove":
            ### In case the user doesn't enter 1 parameter or 3 parameters
            if not(number_of_parameters == 2 or number_of_parameters == 4):
                print("Invalid number of parameters!")
                ui_print_specification_function_remove()
                continue
            try:
                if number_of_parameters == 2:
                    is_parameter_1_int = True
                    try:
                        int(parameters[1])
                    except ValueError:
                        is_parameter_1_int = False

                    if is_parameter_1_int:
                        ui_remove(account_transactions, int(parameters[1]), int(parameters[1]), ["in", "out"])
                    else:
                        if parameters[1] not in ["in", "out"]:
                            clear_screen()
                            print("You should enter one of the following values in the 'type' parameter: 'in', 'out'")
                        else:
                            ui_remove(account_transactions, 1, 31, [parameters[1]])
                elif number_of_parameters == 4:
                    if parameters[2] != "to":
                        ui_print_specification_function_remove()
                        continue
                    ui_remove(account_transactions, int(parameters[1]), int(parameters[3]), ["in", "out"])
            except Exception as e:
                print(e)
        elif parameters[0] == "replace":
            ### In case the user doesn't enter exactly 5 parameters
            if number_of_parameters != 6:
                print("Invalid number of parameters!")
                ui_print_specification_function_replace()
                continue

            if parameters[4] != "with":
                print("Wrong usage!")
                ui_print_specification_function_replace()
                continue

            ui_replace(account_transactions, int(parameters[1]), parameters[2], parameters[3], int(parameters[5]))
        elif parameters[0] == "list":
            clear_screen()
            if number_of_parameters == 1:
                ui_list(account_transactions)
            elif number_of_parameters == 2:
                ui_list_by_type(account_transactions, parameters[1])
            elif number_of_parameters == 3:
                if parameters[1] != "balance":
                    try:
                        ui_list_by_value_size(account_transactions, parameters[1], int(parameters[2]))
                    except Exception as e:
                        print(e)
                else:
                    try:
                        ui_list_balance(account_transactions, int(parameters[2]))
                    except Exception as e:
                        print(e)
        elif parameters[0] == "clear":
            clear_screen()
        elif parameters[0] not in commands:
            print("That command doesn't exist! This is the list of commands: ", commands)

clear_screen()
run_all_tests()
main()

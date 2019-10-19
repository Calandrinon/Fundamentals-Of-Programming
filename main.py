import datetime

"""
    TODO: Add <insert> function and test it.
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
        > transaction_list - The list of transactions. It contains 31
                             positions, each being associated to a list of
                             the transactions made on a specific day of the
                             current month.

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

def ui_print_transactions(transaction_list):
    for transaction in transaction_list:
        transaction.print()

def ui_print_specification_function_add():
    """
        Prints the usage instructions of the function <ui_add>.
    """
    usage_warning_message = "\n\nUsage:\nAdds to a transaction list a new transaction on the current day.\nInput:\n\t> value - A positive integer which represents the amount of\n\tmoney that was transferred\n\t> type - A string which represents the type of the transaction.\n\tIt can be one of the following:\n\t\t* in - a sum of money was transferred into the\n\t\taccount\n\t\t* out - a sum of money was transferred from the\n\t\taccount to somewhere else\n\t> description - A description of the transaction:\n\t\tE.g: 'add 100 out PIZZA'\n\n\n"
    print(usage_warning_message)

def clear_screen():
    print("\n"*200)

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
    test_add()
    test_transaction_class()
    test_split_command()
    print("\n\n\n")

def main():
    account_transactions = []
    commands = ["quit", "exit", "add"]

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
        elif parameters[0] not in commands:
            print("That command doesn't exist! This is the list of commands: ", commands)

clear_screen()
run_all_tests()
main()

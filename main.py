import datetime

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
        print("\nYou should have entered a positive integer as a value.")
        print("The value will be automatically made positive.\n")

    if isinstance(value, float):
        print("\nYou should have entered an integer as a value, not a float.")
        print("The value will be converted to an integer automatically.\n")

    if type not in ["in", "out"]:
        message = "The parameter 'type' should have one of the following values: 'in', 'out'."
        raise Exception(message)

    value = abs(int(value))
    current_date = datetime.datetime.today().day ### The current date when the
                                                 ### transaction is made.

    new_transaction = Transaction(current_date, value, type, description)
    transaction_list.append(new_transaction)

def test_add():
    print("<ui_add> function test:")
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

    """
    ### Test 5
    ui_add(account_transactions, 125.56, "blahblah", "jacket")
    correct_result.append(Transaction(today, 125, "in", "jacket"))
    assert_last_transactions()
    """

    print("<ui_add> function test passed.")

def test_transaction_class():
    print("<Transaction> class test:")
    today = datetime.datetime.today().day
    transaction = Transaction(today, 100, "out", "pizza")
    assert(transaction.get_date() == today)
    assert(transaction.get_value() == 100)
    assert(transaction.get_type() == "out")
    assert(transaction.get_description() == "pizza")
    print("<Transaction> class test passed.")

def run_all_tests():
    print("Tests:")
    test_add()
    test_transaction_class()

def main():
    pass

run_all_tests()

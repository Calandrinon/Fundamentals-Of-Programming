import datetime

"""
    TODO: Change the transaction_list specification in the <ui_add>
          function to indicate that the list contains 31 positions, each
          representing the days in the current month.
"""

def ui_add(transaction_list, value, type, description):
    """
    Adds to a transaction list a new transaction on the current day.
    Input:
        > transaction_list - The list of transactions

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
    current_date = datetime.datetime.today().day ### The current date when the
                                                 ### transaction is made.
    new_transaction = (current_date, value, type, description)
    transaction_list[current_date - 1].append(new_transaction)

def test_add():
    account_transactions = [[] for i in range(31)]
    correct_result = [[] for i in range(31)]

    today = datetime.datetime.today().day
    test_value = 100
    test_type = "out"
    test_description = "pizza"

    ui_add(account_transactions, test_value, test_type, test_description)
    correct_result[today - 1].append((today, test_value, test_type, test_description))

    assert(account_transactions == correct_result)

def run_all_tests():
    test_add()

def main():
    pass

run_all_tests()

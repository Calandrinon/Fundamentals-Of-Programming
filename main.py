from datetime import date

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
    current_date = date.today() ### The current date when the transaction
                                ### is made.
    new_transaction = (current_date, value, type, description)
    transaction_list.append(new_transaction)

def main():
    pass

import datetime
from transaction import Transaction

def add_transaction(transaction_list, value, type, description):
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

def insert_transaction(transaction_list, day, value, type, description):
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

    add_transaction(transaction_list, value, type, description)
    transaction_list[-1].set_date(day)

def list_transaction(transaction_list):
    """
    Lists all the transactions made on the account.
    """
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    for transaction in transaction_list:
        if not isinstance(transaction, Transaction):
            message = "The list parameter is not a list of Transaction objects!"
            raise Exception(message)
        transaction.print()

def list_transaction_by_type(transaction_list, type):
    """
    Lists all the transactions with the specified type (in, out).
    Input:
        > type - The type of the transaction.
    """
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    if type not in ["in", "out"]:
        message = "The type parameter should be either 'in' or 'out'."
        raise Exception(message)

    for transaction in transaction_list:
        if not isinstance(transaction, Transaction):
            message = "The list parameter is not a list of Transaction objects!"
            raise Exception(message)

        if transaction.get_type() == type:
            transaction.print()

def list_transaction_by_value_size(transaction_list, condition, value):
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
        message = "The condition parameter should contain one of the following operands: <, >, =. <=, >="
        raise Exception(message)

    if not isinstance(value, int) or value < 0:
        message = "The value parameter should be a positive integer."
        raise Exception(message)

    for transaction in transaction_list:
        if not isinstance(transaction, Transaction):
            message = "The list parameter is not a list of Transaction objects!"
            raise Exception(message)

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

def list_balance(transaction_list, day):
    """
    Computes the account’s balance on the day specified in the parameter.
    Input:
        > day - integer which represents the day of the month when the user had
                the computed balance.
    """
    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    if not isinstance(day, int) or day < 1 or day > 31:
        message = "The day parameter needs to be a positive integer between 1 and 31."
        raise Exception(message)

    in_transactions_sum = 0
    out_transactions_sum = 0

    for transaction in transaction_list:
        if not isinstance(transaction, Transaction):
            message = "The list parameter is not a list of Transaction objects!"
            raise Exception(message)

        if transaction.get_date() <= day:
            if transaction.get_type() == "in":
                in_transactions_sum += transaction.get_value()
            else:
                out_transactions_sum += transaction.get_value()
    print("The balance is: ", in_transactions_sum - out_transactions_sum)

def remove_transaction(transaction_list, start_day, end_day, types):
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

def edit_transaction(transaction_list, day, type, description, value):
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

def sum_of_transactions_by_type(transaction_list, type):
    """
    Returns the sum of transactions of type "type"("in" or "out")
    """

    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    if type not in ["in", "out"]:
        message = "The type parameter should be either 'in' or 'out'."
        raise Exception(message)

    sum = 0
    for transaction in transaction_list:
        if not isinstance(transaction, Transaction):
            message = "The list parameter is not a list of Transaction objects!"
            raise Exception(message)

        if transaction.get_type() == type:
            sum += transaction.get_value()

    return sum

def maximum_transferred_value(transaction_list, type, day):
    """
    Returns the transaction of type "type" on day "day" with the maximum value.
    """

    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    if type not in ["in", "out"]:
        message = "The type parameter should be either 'in' or 'out'."
        raise Exception(message)

    if not isinstance(day, int) or day < 1 or day > 31:
        message = "The day parameter needs to be a positive integer between 1 and 31."
        raise Exception(message)

    maximum_value = 0
    maximum_transaction = 0

    for transaction in transaction_list:
        if not isinstance(transaction, Transaction):
            message = "The list parameter is not a list of Transaction objects!"
            raise Exception(message)

        if transaction.get_type() == type and transaction.get_date() == day:
            if transaction.get_value() > maximum_value:
                maximum_value = transaction.get_value()
                maximum_transaction = transaction

    if not isinstance(maximum_transaction, Transaction):
        message = "There were no '{}' transactions made on day {}".format(type, day)
        raise Exception(message)

    return maximum_transaction

def filter_transactions(transaction_list, type, value):
    """
    Filters the transactions based on their type or both type and value.
    In case the user enters a value as a second parameter, the transactions that
    will remain after filtering the list will be those with the value smaller than
    the "value" parameter.
    """

    if len(transaction_list) == 0:
        print("The transaction list is empty!")
        return

    if type not in ["in", "out"]:
        message = "The type parameter should be either 'in' or 'out'."
        raise Exception(message)

    if not isinstance(value, int) or value < 0:
        message = "The value parameter should be a positive integer!"
        raise Exception(message)

    if value == 0:
        removed_type = ""
        if type == "out":
            removed_type = "in"
        else:
            removed_type = "out"

        no_type_to_filter = True
        for transaction in transaction_list:
            if transaction.get_type() == type:
                no_type_to_filter = False
                break

        if no_type_to_filter == False:
            remove_transaction(transaction_list, 1, 31, [removed_type])
        else:
            message = "There is no '{}' transaction in the transaction list!".format(type)
            raise Exception(message)

        return

    blank_transaction = Transaction(0, 0, "none", "deleted")
    for transaction_index in range(0, len(transaction_list)):
        if not isinstance(transaction_list[transaction_index], Transaction):
            message = "The list parameter is not a list of Transaction objects!"
            raise Exception(message)

        if transaction_list[transaction_index].get_type() != type or transaction_list[transaction_index].get_value() >= value:
            transaction_list[transaction_index] = blank_transaction

    changes_made = True
    while len(transaction_list) > 0 and changes_made:
        initial_length_of_list = len(transaction_list)
        try:
            transaction_list.remove(blank_transaction)
        except ValueError:    ### in case the value is not found
            break
        final_length_of_list = len(transaction_list)

        if final_length_of_list < initial_length_of_list:
            changes_made = True
        else:
            changes_made = False

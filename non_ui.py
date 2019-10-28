from transaction import Transaction
import os

def clear_screen():
    print("\n"*200)

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

def read_transactions_file(filename):
    """
    Reads the file with the transactions that were saved.
    """
    file = open(filename, 'r')
    transaction_strings_list = file.readlines()
    transaction_objects = []

    for transaction in transaction_strings_list:
        transaction = transaction.replace("[", "")  ### Deletes the first square bracket of the transaction
        transaction = transaction.replace("]", "")  ### Deletes the last square bracket
        transaction = transaction.replace(",", "")  ### Deletes the commas
        transaction = transaction.replace("\n", "")  ### Removes newline \n
        transaction = split_command(transaction)
        ### Takes the string and converts it into a list of strings of details
        ### about the transaction.

        if len(transaction) == 4:
            day = int(transaction[0])
            value = int(transaction[1])
            type = transaction[2]
            description = transaction[3]
            transaction_objects.append(Transaction(day, value, type, description))

    return transaction_objects
    file.close()

def write_transactions_file(account_transactions, filename):
    """
    Writes the account transactions in the transaction file.
    Input:
        > account_transactions - A list with all transactions
        > filename - The name of the file
    """

    file = open(filename, 'w')

    for transaction in account_transactions:
        file.write("[{}, {}, {}, {}]\n".format(transaction.get_date(),
        transaction.get_value(), transaction.get_type(), transaction.get_description()))

    file.close()

def save_last_operation_number(last_operation_number):
    """
    Saves the number of the last operation that has been made.
    This function is used for the "undo" feature.
    """
    file = open("last_operation_number.txt", 'w')
    file.write(str(last_operation_number))
    file.close()

def get_last_operation_number():
    """
    Gets the number of the last operation that has been made.
    This function is used for the "undo" feature.
    """
    file = open("last_operation_number.txt", 'r')
    number = file.read()
    file.close()
    return int(number)

def delete_operation_files(number_of_files):
    """
    Deletes the files that have been used to store each state of the
    transaction list for the undo feature.
    """
    for file in range(0, number_of_files + 1):
        os.remove("operation_"+str(file)+".txt")

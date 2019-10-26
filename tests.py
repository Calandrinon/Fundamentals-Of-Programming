import datetime, operations
from transaction import Transaction
from operations import *
from non_ui import split_command, read_transactions_file, write_transactions_file

def test_filter_transactions():
    print("\n\n<filter_transactions> function test running...")
    account_transactions = []
    correct_result = []

    ### Test 1
    account_transactions = [Transaction(19, 100, "out", "pizza"),  Transaction(19, 500, "out", "stuff"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza"),
    Transaction(21, 100, "in", "gift")]
    correct_result = [Transaction(21, 100, "in", "gift")]
    filter_transactions(account_transactions, "in", 0)
    assert(len(account_transactions) == len(correct_result))
    account_transactions[0].print()

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),  Transaction(19, 500, "out", "stuff"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza"),
    Transaction(21, 100, "in", "gift")]
    correct_result = [Transaction(19, 100, "out", "pizza"),  Transaction(19, 500, "out", "stuff"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza")]
    filter_transactions(account_transactions, "out", 0)
    for transaction in account_transactions:
        transaction.print()
    assert(len(account_transactions) == len(correct_result))

    ### Test 3
    account_transactions = []
    filter_transactions(account_transactions, "in", 0)

    ### Test 4
    account_transactions = [Transaction(19, 100, "out", "pizza"),  Transaction(19, 500, "out", "stuff"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza"),
    Transaction(21, 100, "in", "gift")]
    try:
        filter_transactions(account_transactions, "abc", 0)
    except Exception as e:
        print(e)

    ### Test 5
    account_transactions = [Transaction(19, 100, "out", "pizza"),  Transaction(19, 500, "out", "stuff"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza"),
    Transaction(21, 100, "in", "gift")]
    try:
        filter_transactions(account_transactions, "in", 5.6)
    except Exception as e:
        print(e)

    ### Test 6
    account_transactions = [Transaction(19, 100, "out", "pizza"),  Transaction(19, 500, "out", "stuff"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza"),
    Transaction(21, 100, "in", "gift")]
    try:
        filter_transactions(account_transactions, "in", -300)
    except Exception as e:
        print(e)

    ### Test 7
    account_transactions = [Transaction(19, 100, "out", "pizza"),  Transaction(19, 500, "out", "stuff"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza"),
    Transaction(21, 100, "in", "gift")]
    correct_result = [Transaction(19, 100, "out", "pizza"), Transaction(25, 100, "out", "pizza"),
     Transaction(19, 35, "out", "pizza")]

    filter_transactions(account_transactions, "out", 150)
    for transaction in account_transactions:
        transaction.print()
    assert(len(account_transactions) == len(correct_result))

    print("<filter_transactions> function test passed.\n\n")

def test_maximum_transferred_value():
    print("\n\n<maximum_transferred_value> function test running...")

    ### Test 1
    max = Transaction(19, 500, "out", "stuff")
    account_transactions = [Transaction(19, 100, "out", "pizza"), max,
    Transaction(25, 100, "out", "pizza"), Transaction(19, 35, "out", "pizza"),
    Transaction(21, 100, "in", "gift")]
    assert(max.get_value() == maximum_transferred_value(account_transactions, "out", 19).get_value())

    print("<maximum_transferred_value> function test passed.\n\n")

def test_sum_of_transactions_by_type():
    print("\n\n<sum_of_transactions_by_type> function test running...")

    ### Test 1
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 50, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    assert(sum_of_transactions_by_type(account_transactions, "out") == 350)
    assert(sum_of_transactions_by_type(account_transactions, "in") == 100)

    print("<sum_of_transactions_by_type> function test passed.\n\n")

def test_read_transactions_file():
    print("\n\n<read_transactions_file> function test running...")
    transactions = read_transactions_file("transactions_file.txt")
    for transaction in transactions:
        transaction.print()
    print("<read_transactions_file> function test passed.\n\n")

def test_write_transactions_file():
    print("\n\n<write_transactions_file> function test running...")
    transactions = [Transaction(25, 10, "in", "gift"), Transaction(10, 5000, "in", "bonus"), Transaction(5, 10000, "in", "salary")]
    write_transactions_file(transactions, "transactions_file.txt")
    print("<write_transactions_file> function test passed.\n\n")

def test_list_transaction():
    print("\n\n<list_transaction> function test running...")

    ### Test 1
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    list_transaction(account_transactions)

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), 5]
    try:
        list_transaction(account_transactions)
    except Exception as e:
        print(e)

    print("<list_transaction> function test passed.\n\n")

def test_list_transaction_by_type():
    print("\n\n<list_transaction_by_type> function test running...")

    ### Test 1
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    list_transaction_by_type(account_transactions, "in")

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(20, 100, "in", "some_stuff"), 5]
    try:
        list_transaction_by_type(account_transactions, "in")
    except Exception as e:
        print(e)

    ### Test 3
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(20, 100, "in", "some_stuff"), 5]
    try:
        list_transaction_by_type(account_transactions, "abc")
    except Exception as e:
        print(e)

    print("<list_transaction_by_type> function test passed.\n\n")

def test_list_transaction_by_value_size():
    print("\n\n<list_transaction_by_value_size> function test running...")

    ### Test 1
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 50, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    list_transaction_by_value_size(account_transactions, ">", 75)

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        list_transaction_by_value_size(account_transactions, "<", -13)
    except Exception as e:
        print(e)

    ### Test 3
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        list_transaction_by_value_size(account_transactions, "<", 13.5)
    except Exception as e:
        print(e)

    ### Test 4
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(20, 100, "in", "some_stuff"), 5]
    try:
        list_transaction_by_type(account_transactions, "in")
    except Exception as e:
        print(e)

    print("<list_transaction_by_value_size> function test passed.\n\n")

def test_list_balance():
    print("\n\n<list_balance> function test running...")

    ### Test 1
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 50, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    list_balance(account_transactions, 20)

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        list_balance(account_transactions, 3.5)
    except Exception as e:
        print(e)

    ### Test 3
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        list_balance(account_transactions, -3)
    except Exception as e:
        print(e)

    ### Test 4
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), 5, Transaction(21, 100, "in", "gift")]
    try:
        list_balance(account_transactions, 3)
    except Exception as e:
        print(e)

    print("<list_balance> function test passed.\n\n")

def test_edit_transaction():
    print("\n\n<edit_transaction> function test running...")
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
    edit_transaction(account_transactions, 19, "out", "pizza", 55)
    assert_transaction_lists()

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        edit_transaction(account_transactions, -19, "out", "pizza", 55)
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
        edit_transaction(account_transactions, 5.5, "out", "pizza", 55)
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
        edit_transaction(account_transactions, 5, "abcdef", "pizza", 55)
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
        edit_transaction(account_transactions, 19, "out", "pizza", -12)
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
        edit_transaction(account_transactions, 19, "out", "pizza", 12.5)
    except Exception as e:
        print(e)
    assert_transaction_lists()

    print("<edit_transaction> function test passed.\n\n")

def test_remove_transaction():
    print("\n\n<remove_transaction> function test running...")
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
    remove_transaction(account_transactions, 1, 31, ["in", "out"])
    assert_transaction_lists()

    ### Test 2
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(25, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    remove_transaction(account_transactions, 1, 20, ["in", "out"])
    assert_transaction_lists()

    ### Test 3
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    remove_transaction(account_transactions, 1, 10, ["in", "out"])
    assert_transaction_lists()

    ### Test 4
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    remove_transaction(account_transactions, 1, 20, ["in"])
    assert_transaction_lists()

    ### Test 5
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(21, 100, "in", "gift")]
    remove_transaction(account_transactions, 1, 31, ["out"])
    assert_transaction_lists()

    ### Test 6
    account_transactions = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    correct_final_result = [Transaction(19, 100, "out", "pizza"),
    Transaction(25, 100, "out", "pizza"), Transaction(19, 100, "out", "stuff"),
    Transaction(20, 100, "out", "pizza"), Transaction(21, 100, "in", "gift")]
    try:
        remove_transaction(account_transactions, 1111, 25, ["in"])
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
        remove_transaction(account_transactions, 1111.5, 25, ["out"])
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
        remove_transaction(account_transactions, 2.5, 25, ["out"])
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
        remove_transaction(account_transactions, -2, 25, ["out"])
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
        remove_transaction(account_transactions, 0, 31, ["in"])
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
        remove_transaction(account_transactions, 0, 32, ["crap"])
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
        remove_transaction(account_transactions, 1, 5, ["crap"])
    except Exception as e:
        print(e)
    assert_transaction_lists()

    print("<remove_transaction> function test passed.\n\n")

def test_insert_transaction():
    print("\n\n<insert_transaction> function test running...")
    account_transactions = []
    correct_result = []

    def assert_last_transactions():
        assert(account_transactions[-1].get_date() == correct_result[-1].get_date())
        assert(account_transactions[-1].get_value() == correct_result[-1].get_value())
        assert(account_transactions[-1].get_type() == correct_result[-1].get_type())
        assert(account_transactions[-1].get_description() == correct_result[-1].get_description())

    ### Test 1
    insert_transaction(account_transactions, 24, 125, "in", "jacket")
    correct_result.append(Transaction(24, 125, "in", "jacket"))
    assert_last_transactions()

    ### Test 2
    try:
        insert_transaction(account_transactions, -24, 125, "in", "jacket")
        correct_result.append(Transaction(24, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 3
    try:
        insert_transaction(account_transactions, 24.5, 125, "in", "jacket")
        correct_result.append(Transaction(24, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 4
    try:
        insert_transaction(account_transactions, 52, 125, "in", "jacket")
        correct_result.append(Transaction(24, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    print("<insert_transaction> function test passed.\n\n")

def test_split_command():
    print("\n\n<split_command> function test running...")
    assert(split_command("add 100 out pizza") == ["add", "100", "out", "pizza"])
    assert(split_command("add     100      out   pizza") == ["add", "100", "out", "pizza"])
    assert(split_command("insert    515 in   cool") == ["insert", "515", "in", "cool"])
    print("<split_command> function test passed.\n\n")

def test_add_transaction():
    print("\n\n<add_transaction> function test running...")
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
    try:
        add_transaction(account_transactions, test_value, test_type, test_description)
        correct_result.append(Transaction(today, test_value, test_type, test_description))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 2
    try:
        add_transaction(account_transactions, 125, "in", "jacket")
        correct_result.append(Transaction(today, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 3
    try:
        add_transaction(account_transactions, -125, "in", "jacket")
        correct_result.append(Transaction(today, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 4
    try:
        add_transaction(account_transactions, 125.56, "in", "jacket")
        correct_result.append(Transaction(today, 125, "in", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 5
    try:
        add_transaction(account_transactions, 125, "blahblah", "jacket")
        correct_result.append(Transaction(today, 125, "blahblah", "jacket"))
        assert_last_transactions()
    except Exception as e:
        print(e)

    ### Test 6
    try:
        add_transaction(account_transactions, 125, "in", 123)
        correct_result.append(Transaction(today, 125, "in", 123))
        assert_last_transactions()
    except Exception as e:
        print(e)

    print("<add_transaction> function test passed.\n\n")

def test_transaction_class():
    print("\n\n<Transaction> class test running...")
    today = datetime.datetime.today().day
    transaction = Transaction(today, 100, "out", "pizza")
    assert(transaction.get_date() == today)
    assert(transaction.get_value() == 100)
    assert(transaction.get_type() == "out")
    assert(transaction.get_description() == "pizza")
    print("<Transaction> class test passed.\n\n")

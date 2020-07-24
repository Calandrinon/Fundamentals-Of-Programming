def palindrome(integer):
    result = 0
    ### Returns the palindrome of the parameter.
    while integer > 0:
        ### Takes the current last digit of the parameter and appends it to the
        ### result variable.
        result = result * 10 + integer % 10
        integer /= 10 ### Removes the current last digit of parameter.

    return result

def main():
    number = input("Enter a number: ")
    print(palindrome(number))

main()

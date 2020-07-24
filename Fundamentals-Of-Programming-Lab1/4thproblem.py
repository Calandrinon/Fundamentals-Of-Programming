
def digit_frequency(integer):
    ### Returns the frequency of all digits in the integer given as a parameter.
    frequency_of_digits = [0 for i in range(0, 10)] ### This initializes an empty list with zeroes.

    while integer > 0:
        ### We take each digit of the number and increase the frequency value of the digit in the list.
        frequency_of_digits[integer % 10] += 1
        integer /= 10

    return frequency_of_digits

def largest_number_from_digits(integer):
    result = 0 ### This variable stores the result.
    frequency_list = digit_frequency(integer)

    for digit in range(9, -1, -1): ### Takes all digits from 9 to 0 and appends them to the result variable.
        for i in range(0, frequency_list[digit]):
            result = result * 10 + digit

    return result

def main():
    integer = input("Enter the number: ")
    print(largest_number_from_digits(integer))

main()

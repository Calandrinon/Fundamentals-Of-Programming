import math

"""
    TODO: Functions <increasing_modulus_sequence> and <real_numbers_sequence>:
          If there are multiple sequences of maximum length with the given
          property, print them all
    TODO: Test the function <real_numbers_sequence> once more
    TODO: At function <main> in the while loop: Clear screen after each input
    TODO: At function <main>: Make a function for each option and a map which
          associates the option numbers with the functions
    TODO: At function <main>: Check for exceptions at line 238 when the user
          enters literals other than '+' and 'i'
    TODO: At function <main>: Test the cases where the user enters negative
          imaginary parts (for example: 2 - 5i)  ---> IN PROGRESS
    TODO: At function <real_numbers_sequence>:
          The function doesn't work for lists with only 1 real number
          Repair unexpected results for exception cases like this:
          >  [2 + i, 3 + i, 1]
          >  [2, 5i, i, 2 + i, 2 + 2i, 3 + 2i, 1 + i]
          >  [4i, i, 4, i, i]
          The result: "There are no real numbers in the list!"
"""
class Complex:
    ### This is the complex number being stored in a tuple with the first
    ### position being the real part and the second position being the
    ### imaginary part.
    number = (0, 0)

    ### A constructor which initializes the tuple that represents the
    ### complex number.
    def __init__(self, real_part, imaginary_part):
        self.number = (real_part, imaginary_part)

    ### A getter which gets the real part of the number from the tuple.
    def get_real_part(self):
        return self.number[0]

    ### A getter which gets the imaginary part of the number from the tuple.
    def get_imaginary_part(self):
        return self.number[1]

    ### A setter which sets the real part of the number in the tuple.
    def set_real_part(self, new_real_part):
        new_number = (new_real_part, self.number[1])
        self.number = new_number

    ### A setter which sets the imaginary part of the number in the tuple.
    def set_imaginary_part(self, new_imaginary_part):
        new_number = (self.number[0], new_imaginary_part)
        self.number = new_number

    ### A getter which gets the number tuple.
    def get_number(self):
        return self.number

    ### A setter which sets the number with a new tuple.
    def set_number(self, new_number):
        self.number = new_number

    ### Prints the number.
    def print(self):
        imaginary_part = self.get_imaginary_part()
        real_part = self.get_real_part()

        ### This condition implies that the real part of the number shouldn't
        ### be printed if it's equal to 0 (meaning that 0 shouldn't be printed).
        if real_part == 0 and imaginary_part != 0:
            ### If the imaginary part is 1 then print only "i" instead of "1i".
            if imaginary_part == 1:
                print("i", end="")
            else:
                print(str(imaginary_part) + "i", end="")
            return
        elif real_part != 0 and imaginary_part == 0:
            ### This condition implies that the imaginary part of the number
            ### shouldn't be printed if it's equal to 0 (meaning that "0i"
            ### shouldn't be printed).
            print(real_part, end="")
            return
        elif real_part == 0 and imaginary_part == 0:
            ### This prints only "0" instead of "0+0i" at the line 74.
            print(0, end="")
            return

        if imaginary_part == 1:
            ### This sets the imaginary part to a null string if it is equal to
            ### 1 in order to not print the number as "a + i" instead of
            ### "a + 1i".
            imaginary_part = ""
        elif imaginary_part < 0:
            print("{} - {}i".format(real_part, abs(imaginary_part)), end="")
            return

        print("{} + {}i".format(real_part, imaginary_part), end="")

    ### Returns the modulus of the number.
    def modulus(self):
        return math.sqrt(math.pow(self.get_real_part(), 2) + math.pow(self.get_imaginary_part(), 2))

### Prints the complex number "complex_num" on the screen by using the method
### "print" from the class "Complex".
def write_complex_num(complex_num):
    complex_num.print()

def remove_occurences(list_of_elements, element_del):
    """
    Removes all the occurences of an element in a list.
    Input:
        > list_of_elements - The list that is going to be edited.

        > element_del - The element that will be deleted from the list.

    Output:
        Returns the new list without the occurences of element_del.
    """
    new_list = []
    for element in list_of_elements:
        if element != element_del:
            new_list.append(element)

    return new_list

def expression_evaluator(expression):
    """
    Evaluates an expression of the form "a+bi" of a complex number and returns
    the real and imaginary part of the number as a Complex class instance.


    1 +   2i , -1 - 3 i, +9-6i, -10   + 100i, i, 2i, 3i, 1, 9, 0, -1, +7 + i, -7  -  i, 7  - i, -7+i
    """
    result = Complex(0, 0)
    sign = 1
    parts = []
    current_number = 0
    character_index = 0
    expression += '|'

    for character in expression:
        if character >= '0' and character <= '9':
            current_number = current_number * 10 + int(character)
        else:
            if character_index > 0:
                parts.append(current_number*sign)
                current_number = 0

            if character == 'i':
                break
            elif character == '-':
                sign = -1
            elif character == '+':
                sign = 1
        character_index += 1

    if len(parts) > 2:
        message = "The complex number should have 2 parts."
        raise Exception(message)

    if len(parts) < 2:
        if expression.find('i') != -1:
            if len(parts) == 0:
                result.set_imaginary_part(1)
                return result
            else:
                result.set_imaginary_part(parts[0])
        else:
            result.set_real_part(parts[0])
    else:
        if expression.find('i') != -1 and parts[1] == 0:
            parts[1] = sign
        result.set_real_part(parts[0])
        result.set_imaginary_part(parts[1])
    return result

### Reads the list of complex numbers as a string.
def read_complex_num_list():
    """
    Reads a list of complex numbers as strings.
    """
    numbers_as_strings = str(input("Enter some complex numbers in the form of a+bi and separate them with a comma: "))
    numbers_as_strings = numbers_as_strings.replace(" ", "") ### Replaces spaces in the string with
                                       ### null strings.
    numbers_as_strings = numbers_as_strings.split(",")       ### Splits the string with comma as a
                                       ### delimitator and returns a list with
                                       ### all the remaining elements
    ### For each number in the list "numbers" there will be generated a list
    ### where the complex number in form of a string will be split in two parts
    ### with + as a delimitator.

    numbers = []

    for number_as_string in numbers_as_strings:
        pluses = number_as_string.count('+')
        minuses = number_as_string.count('-')
        i_occurrences = number_as_string.count('i')

        if pluses > 2:
            message = "The expression should have maximum 2 pluses."
            raise Exception(message)

        if minuses > 2:
            message = "The expression should have maximum 2 minuses."
            raise Exception(message)

        if i_occurrences > 1:
            message = "The expression should have only one 'i'."
            raise Exception(message)

        for character in number_as_string:
            if character not in ['+','-','i'] and (character < '0' or character > '9'):
                 message = "The expression should only contain digits, pluses, minuses and the number 'i'."
                 raise Exception(message)

        numbers.append(expression_evaluator(number_as_string))

    return numbers

### Prints the options that can be chosen by the user.
def print_options():
    print("1. Read a list of complex numbers (in a + bi form) from the console.")
    print("2. Display the entire list of numbers on the console.")
    print("3. Display on the console the longest sequence that observes a given property. Each student will receive 2 of the properties from the list provided below.")
    print("4. Exit the application.\n\n\n")

### Prints the contents of a list from pos1 to pos2-1.
def print_list(complex_num_list, pos1, pos2):
    print("[", end="")
    for i in range(pos1, pos2-1):
        write_complex_num(complex_num_list[i])
        print(", ", end="")
    write_complex_num(complex_num_list[pos2-1])
    print("]\n\n")

### Prints the longest sequence of numbers with increasing modulus.
### The numbers are taken from the list of complex numbers being given as a
### parameter.
def increasing_modulus_sequence(complex_num_list):
    sequence_length = 0
    max_seq_length = 0
    previous_modulus = -1
    pos = 0
    first_pos = -1
    last_pos = -1

    print("The modulus of each complex number in the list: ")
    for number in complex_num_list:
        number.print()
        print(": ", number.modulus())
        if number.modulus() > previous_modulus:
            sequence_length += 1
        else:
            if sequence_length > max_seq_length:
                max_seq_length = sequence_length
                last_pos = pos
                first_pos = last_pos - sequence_length
            sequence_length = 1
        previous_modulus = number.modulus()
        pos += 1

    if sequence_length > max_seq_length:
        max_seq_length = sequence_length
        last_pos = pos
        first_pos = last_pos - sequence_length

    print("\n", "First position: {}, Last position: {}".format(first_pos, last_pos - 1))
    print_list(complex_num_list, first_pos, last_pos)

### Prints the longest sequence of real numbers.
### The numbers are taken from the list of complex numbers being given as a
### parameter.
def real_numbers_sequence(complex_num_list):
    sequence_length = 0
    max_seq_length = 0
    previous_imaginary_part = -1
    pos = 0
    first_pos = -1
    last_pos = -1
    has_real_numbers = False ### This variable holds the value True if
                             ### the sequence has real numbers and False if
                             ### it doesn't

    for number in complex_num_list:
        if number.get_imaginary_part() == 0 and previous_imaginary_part == 0:
            sequence_length += 1
            has_real_numbers = True
        else:
            if sequence_length > max_seq_length:
                max_seq_length = sequence_length
                last_pos = pos
                first_pos = last_pos - sequence_length
            sequence_length = 1
        previous_imaginary_part = number.get_imaginary_part()
        pos += 1

    #In case the list has no real numbers we stop the function
    if has_real_numbers == False:
        print("There are no real numbers in the list!")
        return

    if sequence_length > max_seq_length:
        max_seq_length = sequence_length
        last_pos = pos
        first_pos = last_pos - sequence_length

    print("\n", "First position: ", first_pos, ";  Last position: ", last_pos - 1)
    print_list(complex_num_list, first_pos, last_pos)

def clear_screen():
    print("\n" * 200)

def test_read_complex_num_list():
    complex_num_list = read_complex_num_list()
    print_list(complex_num_list, 0, len(complex_num_list))

def test_expression_evaluator():
    ### Test 1
    expression = "1+2i"
    result = expression_evaluator(expression)
    assert(result.get_real_part(), 1)
    assert(result.get_imaginary_part(), 2)

    ### Test 2
    expression = "1-2i"
    result = expression_evaluator(expression)
    assert(result.get_real_part(), 1)
    assert(result.get_imaginary_part(), -2)

    ### Test 3
    expression = "-1+2i"
    result = expression_evaluator(expression)
    assert(result.get_real_part(), -1)
    assert(result.get_imaginary_part(), 2)

    ### Test 4
    expression = "-1-2i"
    result = expression_evaluator(expression)
    assert(result.get_real_part(), -1)
    assert(result.get_imaginary_part(), -2)

def test_remove_occurences():
    test_list = ['a', 'b', 'c', 'a', 'c']
    test_list = remove_occurences(test_list, 'c')
    assert(test_list == ['a', 'b', 'a'])

def run_all_tests():
    test_read_complex_num_list()
    test_expression_evaluator()
    test_remove_occurences()

### The main function.
def main():
    complex_num_list = []

    ### An infinite loop which is broken when the user enters the number 4,
    ### which corresponds to the 4th option, the exit option.
    while True:
        print_options()
        option = int(input("Enter an option: "))
        clear_screen()

        if option == 1:
            try:
                complex_num_list = read_complex_num_list()
                ###clear_screen()
                #1 + 2i, 2i, 3i, 4i, 5, 6, 1, 2, 2 , 6, 735, 12, 1,24
            except ValueError as ve:
                print(ve)
            ### A try and catch statement which catches value errors caused
            ### by faulty conversions from str to int in the
            ### "read_complex_num_list()" function.
        elif option == 2:
            try:
                print_list(complex_num_list, 0, len(complex_num_list))
            except IndexError as IE:
                print(IE) ### Catches the exception IndexError in case the user
                          ### doesn't enter a list.
                print("The list is empty. You should enter some numbers by choosing the option 1.")
        elif option == 3:
            print("Choose one of these 2 options: ")
            print("       A. Get the longest sequence of complex numbers with increasing modulus from the list.")
            print("       B. Get the longest sequence of real numbers from the list.")
            suboption = input("Type A or B: ")
            clear_screen()
            if suboption == 'A':
                increasing_modulus_sequence(complex_num_list)
            elif suboption == 'B':
                real_numbers_sequence(complex_num_list)
            else:
                print("I SAID ENTER A OR B!")
        elif option == 4:
            print("Exiting the program...")
            break
        else:
            print("Type a number between 1 and 4...\n\n")
        print("\n\n")

#run_all_tests()
main()

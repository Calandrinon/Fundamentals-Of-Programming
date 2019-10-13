import math

"""
    TODO: In method "print" from class "Complex": if the imaginary part is
          negative, print '-' instead of '+'
    TODO: Check the comments in class "Complex" once again
    TODO: Check lines 109 and 110 and comment them properly
    TODO: Functions <increasing_modulus_sequence> and <real_numbers_sequence>
          If there are multiple sequences of maximum length with the given
          property, print them all
    TODO: Test the function <real_numbers_sequence> once more
    TODO: At function <main> in the while loop: Clear screen after each input
    TODO: At function <main>: Make a function for each option and a map which
          associates the option numbers with the functions
    TODO: At function <main>: Check for exceptions at line 238 when the user
          enters literals other than '+' and 'i'
    TODO: At function <main>: Test the cases where the user enters negative
          real and imaginary parts (for example: -2 - 5i)
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

        print("{} + {}i".format(real_part, imaginary_part), end="")

    ### Returns the modulus of the number.
    def modulus(self):
        return math.sqrt(math.pow(self.get_real_part(), 2) + math.pow(self.get_imaginary_part(), 2))

### Prints the complex number "complex_num" on the screen by using the method
### "print" from the class "Complex".
def write_complex_num(complex_num):
    complex_num.print()

### Reads a single complex number and returns it as an instance of the
### class "Complex".
def read_complex_num():
    number = str(input("Enter the complex number: "))### Reads the number as a
                                                     ### string.
    number = number.replace(" ", "") ### Replaces each space in the entered
                                     ### string with a null string if the
                                     ### user enters more than one space
                                     ### between each token of the expression.

    parts = number.split("+")        ### Splits the string in 2 parts, real and
                                     ### imaginary (or more parts if the user
                                     ### entered multiple "+" characters).
                                     ### The split method returns a list with
                                     ### the 2 parts.

    parts[-1] = parts[-1].replace("i", "") ### Replaces each i in the imaginary
                                           ### part (which is stored in the
                                           ### last element of the list) with
                                           ### a null string.
    if parts[-1] == "":
        parts[-1] = "1"

    return Complex(int(parts[0]), int(parts[-1]))

def read_complex_num_list():
    numbers = str(input("Enter some complex numbers in the form of a+bi and separate them with a comma: "))
    numbers = numbers.replace(" ", "")
    numbers = numbers.split(",")
    numbers = [list(number.split("+")) for number in numbers]
    for number in numbers:
        if number[-1].find("i") != -1:
            if number[0].find("i") != -1:
                number.insert(0, "0")
            number[-1] = number[-1].replace("i", "")
        else:
            number.append("0")
    final_list = []

    for number in numbers:
        if len(number) == 2:
            if number[-1] == "":
                number[-1] = "1"      #case of 2+i or 1+i or 4+i
            final_list.append(Complex(int(number[0]), int(number[-1])))

    return final_list

def print_options():
    print("1. Read a list of complex numbers (in a + bi form) from the console.")
    print("2. Display the entire list of numbers on the console.")
    print("3. Display on the console the longest sequence that observes a given property. Each student will receive 2 of the properties from the list provided below.")
    print("4. Exit the application.\n\n\n")

def print_list(complex_num_list, pos1, pos2):
    print("[", end="")
    for i in range(pos1, pos2-1):
        write_complex_num(complex_num_list[i])
        print(", ", end="")
    write_complex_num(complex_num_list[pos2-1])
    print("]\n\n")

def increasing_modulus_sequence(complex_num_list):
    sequence_length = 0
    max_seq_length = 0
    previous_modulus = -1
    pos = 0
    first_pos = -1
    last_pos = -1

    print("The modulus of each complex number in the list: ")
    for number in complex_num_list:
        print(number.modulus())
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

    print("\n", "First position: ", first_pos, ";  Last position: ", last_pos - 1)
    print_list(complex_num_list, first_pos, last_pos)

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

def main():
    print_options()
    functionalities = (read_complex_num_list, print_list)
    complex_num_list = []

    while True:
        option = int(input("Enter an option: "))
        print("\n")

        if option == 1:
            try:
                complex_num_list = read_complex_num_list()
            except ValueError as ve:
                print(ve)
        elif option == 2:
            try:
                print_list(complex_num_list, 0, len(complex_num_list))
            except IndexError as IE:
                print(IE)
                print("The list is empty. You should enter some numbers by choosing the option 1.")
        elif option == 3:
            print("Choose one of these 2 options: ")
            print("       A. Get the longest sequence of complex numbers with increasing modulus from the list.")
            print("       B. Get the longest sequence of real numbers from the list.")
            suboption = input("Type A or B: ")
            if suboption == 'A':
                increasing_modulus_sequence(complex_num_list)
            elif suboption == 'B':
                real_numbers_sequence(complex_num_list)
                pass
            else:
                print("I SAID ENTER A OR B!")
        elif option == 4:
            print("Exiting the program...")
            break
        else:
            print("Type a number between 1 and 4...\n\n")
        print("\n\n")

def test_write_complex_num(number):
    write_complex_num(number)

def test_read_complex_num():
    num = read_complex_num()
    write_complex_num(num)
    print("\n")

def test_read_complex_num_list():
    l = read_complex_num_list()
    print_list(l, 0, len(l))

def test_print_list():
    a_list = [Complex(0, 5), Complex(4, 0), Complex(-3, -2), Complex(0, 0), Complex(1, 0), Complex(2, 1)]
    print_list(a_list, 0, len(a_list))

def test_increasing_modulus_sequence():
    numbers = [Complex(1, 5), Complex(1, 6), Complex(71, 7), Complex(1, 1), Complex(0, 2), Complex(15, 12), Complex(16, 19), Complex(27, 39), Complex(32, 77), Complex(1, 1), Complex(1, 2), Complex(1, 3), Complex(1, 4), Complex(1, 5)]
    numbers2 = [Complex(0, 0), Complex(0, 0), Complex(0, 0), Complex(0, 0)]
    numbers3 = [Complex(0, 1), Complex(1, 1), Complex(0, 2), Complex(1, 0)]
    numbers4 = [Complex(0, 1)]
    numbers5 = [Complex(0, 1), Complex(0, 50), Complex(0, 3), Complex(2, 6), Complex(1, 0)]
    increasing_modulus_sequence(numbers)
    increasing_modulus_sequence(numbers2)
    increasing_modulus_sequence(numbers3)
    increasing_modulus_sequence(numbers4)
    increasing_modulus_sequence(numbers5)

def test_real_numbers_sequence():
    numbers = [Complex(1, 5), Complex(1, 6), Complex(71, 7), Complex(1, 1), Complex(0, 2), Complex(15, 12), Complex(16, 19), Complex(27, 39), Complex(32, 77), Complex(1, 1), Complex(1, 2), Complex(1, 3), Complex(1, 4), Complex(1, 5)]
    numbers2 = [Complex(0, 0), Complex(0, 0), Complex(0, 0), Complex(0, 0)]
    numbers3 = [Complex(0, 1), Complex(1, 1), Complex(0, 2), Complex(1, 0)]
    numbers4 = [Complex(0, 1)]
    numbers5 = [Complex(0, 1), Complex(0, 50), Complex(0, 3), Complex(2, 6), Complex(1, 0)]
    real_numbers_sequence(numbers)
    real_numbers_sequence(numbers2)
    real_numbers_sequence(numbers3)
    real_numbers_sequence(numbers4)
    real_numbers_sequence(numbers5)

def test():
    #test_write_complex_num(Complex(5, 3))  #--> passed
    #test_read_complex_num() #--> passed
    #test_read_complex_num_list() #--> passed (but should be verified with more cases)
    #print_options() #--> passed
    #test_print_list() #--> passed
    #test_increasing_modulus_sequence() #--> passed
    #test_real_numbers_sequence() #--> NOT PASSED, SHOULD BE TESTED ONCE MORE!!!!!!!!
    pass

#test()
main()

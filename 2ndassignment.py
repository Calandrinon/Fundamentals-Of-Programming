import math

"""
    TODO: In method "print" from class "Complex": if the imaginary part is
          negative, print '-' instead of '+'
    TODO: Check lines 109 and 110 and comment them properly
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
          imaginary parts (for example: 2 - 5i)
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

### Reads the list of complex numbers as a string.
def read_complex_num_list():
    numbers = str(input("Enter some complex numbers in the form of a+bi and separate them with a comma: "))
    numbers = numbers.replace(" ", "") ### Replaces spaces in the string with
                                       ### null strings.
    numbers = numbers.split(",")       ### Splits the string with comma as a
                                       ### delimitator and returns a list with
                                       ### all the remaining elements
    numbers = [list(number.split("+")) for number in numbers]
    ### For each number in the list "numbers" there will be generated a list
    ### where the complex number in form of a string will be split in two parts
    ### with + as a delimitator.

    for number in numbers:
        if number[-1].find("i") != -1:    ### This takes the last element in the
                                          ### list "number"(which is usually
                                          ### the imaginary part, if it exists)
                                          ### and checks if the string "i" is
                                          ### present in this last element.
            if number[0].find("i") != -1:
                ### This if statement checks if the string "i" is present in
                ### the first element, in order to see if the number has a
                ### real part or not.
                number.insert(0, "0")
                ### Inserts a zero on the first position into the list "number"
                ### in case the number has no real part.
            number[-1] = number[-1].replace("i", "")
            ### Replaces each "i" in the last element of the list number with
            ### a null string.
        else:
            ### If the last element of the list "number" doesn't contain the
            ### string "i", then we append a 0 to the end of the list which
            ### will represent the null imaginary part.
            number.append("0")

    final_list = []

    for number in numbers:
        ### This takes each list "number" in the list "numbers" and
        ### checks if it has at least 2 elements and if it does, then
        ### it checks if the last element of the list "number" is a null string.
        ### If it is, then it means the string "i" was deleted and we add a
        ### "1" in the string form of the representation of the number.

        ### If there are more than 2 elements in the list "number", they are
        ### null strings which were included in the list as a result of the use
        ### of the function "split()".
        if len(number) >= 2:
            if number[-1] == "":
                number[-1] = "1"      #case of 2+i or 1+i or 4+i
            final_list.append(Complex(int(number[0]), int(number[-1])))

    return final_list

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

### The main function.
def main():
    print_options()
    complex_num_list = []

    ### An infinite loop which is broken when the user enters the number 4,
    ### which corresponds to the 4th option, the exit option.
    while True:
        option = int(input("Enter an option: "))
        print("\n")

        if option == 1:
            try:
                complex_num_list = read_complex_num_list()
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

main()

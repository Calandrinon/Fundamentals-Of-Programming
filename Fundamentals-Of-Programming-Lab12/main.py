
def generate_option_alternatives_recursively(solution_length, index=0, number_of_1_options=0, result=""):
    options = ['1', 'X', '2']
    if index == solution_length:
        print(result)
        return

    if index == solution_length - 1:
        del options[1]

    for option in options:
        new_result = result

        if option == '1':
            if number_of_1_options < 2:
                new_result += option
                generate_option_alternatives_recursively(solution_length, index+1, number_of_1_options+1, new_result)
        else:
            new_result += option
            generate_option_alternatives_recursively(solution_length, index+1, number_of_1_options, new_result)


def generate_option_alternatives_iteratively(solution_length, index=0, number_of_1_options=0, result=""):
    stack = []
    stack.append((solution_length, index, number_of_1_options, result))

    while len(stack) > 0:
        parameter_solution_length, parameter_index, parameter_number_of_1_options, parameter_result = stack[-1]
        del stack[-1]

        options = ['1', 'X', '2']

        if parameter_index == parameter_solution_length:
            print(parameter_result)
            continue

        if parameter_index == parameter_solution_length - 1:
            del options[1]


        for option in options:
            new_result = parameter_result

            if option == '1':
                if parameter_number_of_1_options < 2:
                    new_result += option
                    stack.append((parameter_solution_length, parameter_index+1, parameter_number_of_1_options+1, new_result))
            else:
                new_result += option
                stack.append((parameter_solution_length, parameter_index+1, parameter_number_of_1_options, new_result))



print("Recursive:")
generate_option_alternatives_recursively(4)

print("\n\nIterative:")
generate_option_alternatives_iteratively(4)

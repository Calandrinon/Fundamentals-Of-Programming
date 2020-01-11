
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


generate_option_alternatives_recursively(4)

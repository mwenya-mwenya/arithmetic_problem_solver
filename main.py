
def arithmetic_arranger(problems, show_answers=False):
    # Split the arithmetic problems into components
    calc_list_split = [a.split() for a in problems]
    formatted_output = ''
    answer = show_answers

    # Check for various error conditions
    verify_num_length = any([True if len(ls[0]) > 4 or len(ls[2]) > 4 else False for ls in calc_list_split])
    verify_op = any([op[1] not in ('-', '+') for op in calc_list_split])
    verify_num = any([False if num[0].isdigit() and num[2].isdigit() else True for num in calc_list_split])
    verify_number_of_problems = len(calc_list_split) > 5

    if verify_op:
        return "Error: Operator must be '+' or '-'."
    elif verify_number_of_problems:
        return 'Error: Too many problems.'
    elif verify_num:
        return 'Error: Numbers must only contain digits.'
    elif verify_num_length:
        return 'Error: Numbers cannot be more than four digits.'
    else:
        # Create a list to organize the formatted output
        reformat_list = [
            [a[0] for a in calc_list_split],
            [[b[1], b[2]] for b in calc_list_split],
            [(lambda arr=c: int(arr[0]) + int(arr[2]) if c[1] == '+' else int(arr[0]) - int(arr[2]))() for c in calc_list_split]
        ]

        # Determine maximum lengths for formatting
        longest_char = [max([len(reformat_list[0][i]), len(reformat_list[1][i][1])]) for i in range(len(calc_list_split))]
        shortest_char = [min([len(reformat_list[0][i]), len(reformat_list[1][i][1])]) for i in range(len(calc_list_split))]

        # Build the formatted output
        for idx1, char_list in enumerate(reformat_list):
            for idx2, char in enumerate(char_list):
                if idx1 == 0 and idx2 == 0:
                    formatted_output += char.rjust(2 + longest_char[idx2])
                if idx1 == 0 and idx2 > 0:
                    formatted_output += char.rjust(6 + longest_char[idx2])
                if idx1 == 1 and idx2 == 0:
                    if len(char_list[0][1]) < longest_char[idx2]:
                        formatted_output += '\n' + char[0] + char_list[0][1].rjust(2 + longest_char[idx2] - shortest_char[idx2])
                    else:
                        formatted_output += '\n' + char[0] + char_list[0][1].rjust(1 + longest_char[idx2])
                if idx1 == 1 and idx2 > 0:
                    formatted_output += char[0].rjust(5) + char[1].rjust(1 + longest_char[idx2])
                if idx1 == 1 and idx2 == len(char_list) - 1:
                    formatted_output += '\n'
                    continue
                if idx1 == 2:
                    number_of_dashes = longest_char[idx2] + 2
                    str_to_add = '-' * number_of_dashes
                    if idx2 == 0:
                        formatted_output += str_to_add.rjust(longest_char[idx2])
                    else:
                        formatted_output += str_to_add.rjust(6 + longest_char[idx2])

        # Add answers if requested
        for idx3, char1 in enumerate(reformat_list[2]):
            if answer:
                if idx3 == 0:
                    formatted_output += '\n'
                    formatted_output += str(char1).rjust(2 + longest_char[idx3])
                else:
                    formatted_output += str(char1).rjust(6 + longest_char[idx3])

        return formatted_output

# Example usage
string = arithmetic_arranger(["3 + 855", "988 + 40"], True)
print(string)

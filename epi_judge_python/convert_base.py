from test_framework import generic_test
import string


def convert_base(num_as_string, b1, b2):
    # TODO - you fill in here.
    if num_as_string[0] == "-":
        sign = "-"
        num_as_string = num_as_string[1:]
    else:
        sign = ""

    int_rep = 0
    for i, digit in enumerate(reversed(num_as_string)):
        int_digit = string.hexdigits.index(digit.lower())
        int_rep += int_digit * b1 ** i

    output = ''
    while True:
        output += string.hexdigits[int_rep % b2].upper()
        int_rep //= b2
        if int_rep == 0:
            break
    
    return sign + output[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))

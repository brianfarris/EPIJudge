from test_framework import generic_test
import math


def is_palindrome_number(x):
    # TODO - you fill in here.
    if x < 0:
        return False
    if x == 0:
        return True
    n_digits = math.floor(math.log10(x)) + 1
    mask = 10**(n_digits - 1)
    for _ in range(n_digits // 2):
        first_digit = x // mask
        last_digit = x % 10
        if first_digit != last_digit:
            return False
        x %= mask
        x //= 10
        mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))

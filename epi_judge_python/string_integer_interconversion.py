from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    is_neg = False
    if x < 0:
        is_neg, x = True, -x

    s = []
    while True:
        s.append(str(x % 10))
        x //= 10
        if x == 0:
            break
    return ('-' if is_neg else '') + ''.join(reversed(s)) 


def string_to_int(s):
    # TODO - you fill in here.
    if s[0] == '-':
        sign = -1
        s = s[1:]
    else:
        sign = 1

    total = 0
    for i, c in enumerate(reversed(s)):
        total += 10**i * int(c)
    return sign * total


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))

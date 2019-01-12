from test_framework import generic_test
import sys


def palindrome_decompositions(input):
    # TODO - you fill in here.
    if input == '':
        return [[]]
    output = []
    for i in range(1, len(input)+1):
        prefix = input[:i]
        if prefix == prefix[::-1]:
            output += [[prefix] + x for x in
                       palindrome_decompositions(input[i:])]
    return output


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))

from test_framework import generic_test
import copy

def has_two_sum(A, t):
    while len(A) >= 2:
        end_sum = A[0] + A[-1]
        if end_sum == t:
            return True
        elif end_sum > t:
            A.pop()
        elif end_sum < t:
            A.pop(0)
    return False


def has_three_sum(A, t):
    # TODO - you fill in here.
    return any(has_two_sum(copy.copy(A), t - a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))

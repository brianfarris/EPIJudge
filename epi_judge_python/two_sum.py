from test_framework import generic_test


def has_two_sum(A, t):
    # TODO - you fill in here.
    answer = False

    while len(A) >= 2:
        end_sum = A[0] + A[-1]
        if end_sum == t:
            return True
        elif end_sum > t:
            A.pop()
        elif end_sum < t:
            A.pop(0)
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))

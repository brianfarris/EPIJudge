from test_framework import generic_test


def has_two_sum(A, t):
    i = 0
    j = len(A) - 1
    while j >= i:
        endpoints_sum = A[i] + A[j]
        if endpoints_sum == t:
            return True
        elif endpoints_sum > t:
            j -= 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))

from test_framework import generic_test

def has_two_sum(A, t):
    i, j = 0, len(A) - 1
    while j >= i:
        end_sum = A[i] + A[j]
        if end_sum == t:
            return True
        elif end_sum > t:
            j -= 1
        elif end_sum < t:
            i += 1
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))

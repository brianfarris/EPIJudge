from test_framework import generic_test


def smallest_nonconstructible_value(A):
    # TODO - you fill in here.
    max_val = 0
    A.sort()
    for a in A:
        if a > max_val + 1:
            break
        else:
            max_val += a
    return max_val + 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))

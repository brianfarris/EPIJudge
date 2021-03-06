from test_framework import generic_test


def smallest_nonconstructible_value(A):
    max_val = 0
    for a in sorted(A):
        if a > max_val + 1:
            break
        max_val += a
    return max_val + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))

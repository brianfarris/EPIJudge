from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(ifs):
    counter = [0] * 2**16
    for x in map(int, ifs):
        upper_part_x = x >> 16
        counter[upper_part_x] += 1
    candidate_bucket = next(i for i, c in enumerate(counter) if c < 2**16)

    ifs.seek(0)
    bit_vec = [0] * 2**16

    for x in map(int, ifs):
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            lower_part_x = ((1 << 16) - 1) & x
            bit_vec[lower_part_x] = 1

    for i, v in enumerate(bit_vec):
        if v == 0:
            return (candidate_bucket << 16) | i

def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))

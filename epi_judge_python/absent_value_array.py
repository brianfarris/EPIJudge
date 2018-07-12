from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream):
    stream = list(stream)
    print(len(stream))
    print(19 in stream)
    print(127 in stream)
    missing = 0
    for i in range(10):
        num = [0, 0]
        for x in stream:
            # print("(x >> i) & 1: ", (x >> i) & 1)
            if (x >> i) &  1:
                num[1] += 1
            else:
                num[0] += 1
        print("i: ", i, "num: ", num, "num[0] > num[1]: ", num[0] > num[1])
        if num[0] > num[1]:
            missing += 2**i

    return missing


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

import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def gray_code(num_bits):
    # TODO - you fill in here.
    def differs_by_one_bit(x, y):
        bit_diff = x ^ y
        return bit_diff and not (bit_diff & (bit_diff - 1))

    def rec():
        if len(result) == 1 << num_bits: # 2^num_bits, done
            return differs_by_one_bit(result[0], result[-1])

        for i in range(num_bits):
            prev = result[-1]
            next_cand = prev ^ (1 << i)
            if next_cand not in result:
                result.append(next_cand)
                if rec():
                    return True
                del result[-1]
        return False

    result = [0]
    rec()

    return result


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    def differs_by_1_bit(a, b):
        x = a ^ b
        if x == 0:
            return False
        while x & 1 == 0:
            x >>= 1
        return x == 1

    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = (1 << num_bits)
    if len(result) != expected_size:
        raise TestFailure("Length mismatch: expected " + str(expected_size) +
                          ", got " + str(len(result)))
    for i in range(1, len(result)):
        if not differs_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure("Two adjacent entries are equal")
            else:
                raise TestFailure(
                    "Two adjacent entries differ by more than 1 bit")

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure("Not all entries are distinct: found " +
                          str(len(result) - len(uniq)) + " duplicates")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("gray_code.py", "gray_code.tsv",
                                       gray_code_wrapper))

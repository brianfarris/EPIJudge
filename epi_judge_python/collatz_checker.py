from test_framework import generic_test


def test_collatz_conjecture(n):
    visited = set()
    for i in range(3, n + 1):

        test_i = i
        while test_i >= i:
            if test_i in visited:
                return False
            visited.add(test_i)

            if test_i % 2: # odd case
                if test_i in visited:
                    break
                visited.add(test_i)
                test_i = 3 * test_i + 1
            else:
                test_i //= 2
    return True

"""
def test_collatz_conjecture(n):
    # TODO - you fill in here.
    verified = set()
    for i in range(3, n + 1):
        sequence = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                return False
            sequence.add(test_i)

            if test_i % 2:
                if test_i in verified:
                    break
                verified.add(test_i)
                test_i = 3 * test_i + 1
            else:
                test_i //= 2
    return True
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("collatz_checker.py",
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))

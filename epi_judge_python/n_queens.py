from test_framework import generic_test
import copy


def n_queens(n):
    # TODO - you fill in here.
    def rec(row):
        if row == n:
            result.append(copy.copy(col_placement))
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                rec(row + 1)
    result, col_placement = [], [0]*n
    rec(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))

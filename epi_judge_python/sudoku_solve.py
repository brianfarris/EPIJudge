import itertools
import copy
import functools
import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment):
    # TODO - you fill in here.
    def rec(i, j):
        if i == len(partial_assignment):
            i = 0
            j += 1
            if j == len(partial_assignment[i]):
                return True

        if partial_assignment[i][j] != 0:
            return rec(i + 1, j)

        def check_valid(i, j, val):

            if any(val == partial_assignment[k][j]
                   for k in range(len(partial_assignment))):
                return False

            if val in partial_assignment[i]:
                return False

            region_size = int(math.sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size

            return not any(
                val == partial_assignment[region_size * I + a][region_size * J + b]
                for a, b in itertools.product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment) + 1):
            if check_valid(i, j, val):
                partial_assignment[i][j] = val
                if rec(i + 1, j):
                    return True
        partial_assignment[i][j] = 0
        return False

    return rec(0,0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))

    for i in range(len(solved)):
        pass
        assert_unique_seq(solved[i])
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sudoku_solve.py", 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))

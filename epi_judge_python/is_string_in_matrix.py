from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    m = len(grid)
    n = len(grid[0])
    cache = {}
    def rec(i, j, offset):
        if offset == len(S):
            return True

        if i < 0 or i >= m or j < 0 or j >= n:
            return False

        if (i, j, offset) not in cache:
            cache[(i, j, offset)] = (grid[i][j] == S[offset]
                    and any([rec(i + 1, j, offset + 1),
                             rec(i - 1, j, offset + 1),
                             rec(i, j + 1, offset + 1),
                             rec(i, j - 1, offset + 1)]))
        return cache[(i, j, offset)]
    return any(rec(i, j, 0) for i in range(m) for j in range(n))


"""
def is_pattern_contained_in_grid(grid, S):
    # TODO - you fill in here.
    m = len(grid)
    n = len(grid[0])
    cache = {}
    def rec(i, j, offset):
        if offset == len(S):
            return True

        if i < 0 or i >= m or j < 0 or j >= n:
            return False

        if (i, j, offset) not in cache:
            cache[(i, j, offset)] = (grid[i][j] == S[offset]
                                     and any([rec(i + 1, j, offset + 1),
                                              rec(i - 1, j, offset + 1),
                                              rec(i, j + 1, offset + 1),
                                              rec(i, j - 1, offset + 1)]))
        return cache[(i, j, offset)]


    return any(rec(i, j, 0) for i in range(m) for j in range(n))
"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))

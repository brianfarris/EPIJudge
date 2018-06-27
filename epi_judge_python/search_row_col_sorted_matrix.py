from test_framework import generic_test


def matrix_search(A, x):
    # TODO - you fill in here.
    m = len(A)
    if m == 0:
        return False
    n = len(A[0])
    if n == 0:
        return False
    if x < A[0][n-1]:
        return matrix_search([row[:n-1] for row in A], x)
    elif x > A[0][n-1]:
        return matrix_search(A[1:], x)
    else:
        return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))

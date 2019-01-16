from test_framework import generic_test

cache = {}
def number_of_ways(n, m):
    if n==1 or m==1:
        return 1
    if (n, m) not in cache:
        cache[(n, m)] = number_of_ways(n-1, m) + number_of_ways(n, m - 1)
    return cache[(n, m)]

"""
cache = {}
def number_of_ways(n, m):
    # TODO - you fill in here.
    if n == 1 or m == 1:
        return 1
    if (n, m) in cache:
        return cache[(n, m)]

    cache[(n, m)] = number_of_ways(n - 1, m) + number_of_ways(n, m - 1)
    return cache[(n, m)]
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))

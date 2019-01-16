from test_framework import generic_test


cache = {}
def compute_binomial_coefficient(n, k):
    if k in (0, n):
        return 1

    if (n, k) not in cache:
        cache[(n,k)] = (compute_binomial_coefficient(n - 1, k - 1) +
                        compute_binomial_coefficient(n -  1, k))
    return cache[(n, k)]

"""
cache = {}
def compute_binomial_coefficient(n, k):
    # TODO - you fill in here.
    if k in (0, n):
        return 1

    if (n, k) in cache:
        return cache[(n, k)]

    cache[(n, k)] = compute_binomial_coefficient(n - 1, k - 1) + compute_binomial_coefficient(n - 1, k)
    return cache[(n, k)]
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))

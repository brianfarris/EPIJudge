from test_framework import generic_test, test_utils


def combinations(n, k):

    def rec(start, k):
        if k == 0:
            return [[]]
        elif n - start + 1 == k:
            return [list(range(start, n + 1))]

        return rec(start + 1, k) + [[start] + x for x in rec(start + 1, k-1)]

    return rec(1, k)

"""
def combinations(n, k):
    # TODO - you fill in here.
    if n == k:
        return [list(range(1, n+1))]
    elif k == 0:
        return [[]]
    else:
        return [[x + 1 for x in comb] for comb in combinations(n-1, k)] \
                + [[1] + [x + 1 for x in comb] for comb in combinations(n-1, k-1)]
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))

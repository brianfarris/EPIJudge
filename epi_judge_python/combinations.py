from test_framework import generic_test, test_utils


def combinations(n, k):
    # TODO - you fill in here.
    if n == k:
        return [list(range(1, n+1))]
    elif k == 0:
        return [[]]
    else:
        return [[x + 1 for x in comb] for comb in combinations(n-1, k)] \
                + [[1] + [x + 1 for x in comb] for comb in combinations(n-1, k-1)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))

from test_framework import generic_test


def find_nearest_repetition(paragraph):
    cache = {}
    min_dist = float("inf")
    for i, word in enumerate(paragraph):
        if word in cache:
            min_dist = min(min_dist, i - cache[word])
        cache[word] = i
    return -1 if min_dist == float("inf") else min_dist


"""
def find_nearest_repetition(paragraph):
    cache = {}
    min_dist = float("inf")
    for i, word in enumerate(paragraph):
        if word in cache:
            i_eq = cache[word]
            min_dist = min(min_dist, i - i_eq)

        cache[word] = i
    if min_dist == float("inf"):
        return -1
    else:
        return min_dist
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))

from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    cache = {}
    min_dist = float('inf')
    i = 0
    for word in paragraph:
        if word in cache:
            dist = i - cache[word]
            min_dist = min(min_dist, dist)
        cache[word] = i
        i += 1
    if min_dist == float('inf'):
        return -1
    else:
        return min_dist

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))

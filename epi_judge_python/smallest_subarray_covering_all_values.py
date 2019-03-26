import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    i = j = 0
    shortest_ij = (0, 0)
    shortest = float("inf")
    missing = {keyword: 1 for keyword in keywords}
    keywords_cache = {keyword: 0 for keyword in keywords}
    while missing and j < len(paragraph):
        if paragraph[j] in keywords_cache:
            keywords_cache[paragraph[j]] += 1
            if paragraph[j] in missing:
                del missing[paragraph[j]]
        j += 1
        while not missing and i < j:
            if paragraph[i] in keywords_cache:
                keywords_cache[paragraph[i]] -= 1
                if keywords_cache[paragraph[i]] == 0:
                    missing[paragraph[i]] = 1
            i += 1
            print("i: ", i, "j: ", j)
        if (j - i) < shortest:
            shortest = j - i
            shortest_ij = (i, j)

    return shortest_ij










"""
def find_smallest_sequentially_covering_subset(paragraph, keywords):
    n_kw = len(keywords)
    kw_idx = {k: i for i, k in enumerate(keywords)}
    latest = [-1] * n_kw
    shortest_subarray_length = [float('inf')] * n_kw

    shortest_dist = float('inf')
    result = Subarray(-1, -1)

    for i, word in enumerate(paragraph):
        if word in kw_idx:
            word_idx = kw_idx[word]
            if word_idx == 0:
                shortest_subarray_length[word_idx] = 1
            elif shortest_subarray_length[word_idx - 1] != float('inf'):
                shortest_subarray_length[word_idx] = (
                        i - latest[word_idx - 1] +
                        shortest_subarray_length[word_idx - 1])
            latest[word_idx] = i

            if (word_idx == n_kw - 1 and shortest_subarray_length[-1] < shortest_dist):
                shortest_dist = shortest_subarray_length[-1]
                result = Subarray(i - shortest_dist + 1, i)
    return result
"""

"""
def find_smallest_sequentially_covering_subset(paragraph, keywords):
    # TODO - you fill in here.
    keyword_to_idx = {k:i for i, k in enumerate(keywords)}
    latest_occurence = [-1] * len(keywords)
    shortest_subarray_length = [float('inf')] * len(keywords)

    shortest_distance = float('inf')
    result = Subarray(-1, -1)
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_previous_keyword = i - latest_occurence[keyword_idx - 1]
                shortest_subarray_length[keyword_idx] = (distance_to_previous_keyword
                        + shortest_subarray_length[keyword_idx - 1])
            latest_occurence[keyword_idx] = i

            if (keyword_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i - shortest_distance + 1, i)
    return result
"""

@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))

import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    hash_table = {}
    for k in keywords:
        if k not in hash_table:
            hash_table[k] = 1
        else:
            hash_table[k] += 1

    result = (-1, -1)
    n_remaining = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            hash_table[p] -= 1
            if hash_table[p] >= 0:
                n_remaining -= 1
        while n_remaining == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)

            pl = paragraph[left]
            if pl in keywords:
                hash_table[pl] += 1
                if hash_table[pl] > 0:
                    n_remaining += 1
            left += 1
    return result

"""
def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = (-1, -1)
    remaining_to_cover = len(keywords)
    left=0
    for right, word in enumerate(paragraph):
        if word in keywords:
            keywords_to_cover[word] -= 1
            if keywords_to_cover[word] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            left_word = paragraph[left]
            if left_word in keywords:
                keywords_to_cover[left_word] += 1
                if keywords_to_cover[left_word] > 0:
                    remaining_to_cover += 1
            left += 1
    return result

"""

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))

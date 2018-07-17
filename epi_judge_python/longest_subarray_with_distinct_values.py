from test_framework import generic_test
import collections


def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.
    if A == []:
        return 0
    start = 0
    end = 0
    cache = collections.defaultdict(int)
    best_length = 0
    while end <= len(A):
        length = end - start

        if len(cache) == end - start:
            if length > best_length:
                best_length = length
                result = A[start:end]
            end += 1
            if end <= len(A):
                cache[A[end-1]] += 1
        else:
            if cache[A[start]] == 1:
                del cache[A[start]]
            else:
                cache[A[start]] -= 1
            start += 1
    return best_length

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))

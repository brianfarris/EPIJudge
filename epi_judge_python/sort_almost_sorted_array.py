from test_framework import generic_test
import heapq
import itertools


def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    sequence = iter(sequence)
    min_heap = []
    output = []
    for _ in range(k):
        next_num = next(sequence, None)
        if next_num is not None:
            heapq.heappush(min_heap, next_num)

    for next_num in sequence:
        smallest = heapq.heappushpop(min_heap, next_num)
        output.append(smallest)

    while min_heap:
        output.append(heapq.heappop(min_heap))

    return output


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))

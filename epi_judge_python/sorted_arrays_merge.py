from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    sorted_arrays = [iter(x) for x in sorted_arrays]
    min_heap = []
    output = []
    for i, arr in enumerate(sorted_arrays):
        first_elem = next(arr, None)
        if first_elem is not None:
            heapq.heappush(min_heap, (first_elem, i))

    while min_heap:
        smallest, i = heapq.heappop(min_heap)
        output.append(smallest)
        arr_i = sorted_arrays[i]
        next_elem = next(arr_i, None)
        if next_elem is not None:
            heapq.heappush(min_heap, (next_elem, i))

    return output
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))

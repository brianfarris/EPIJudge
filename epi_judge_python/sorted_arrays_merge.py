from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_elem = next(it, None)
        if first_elem is not None:
            heapq.heappush(min_heap, (first_elem, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
        result.append(smallest_entry)
    return result
"""    
def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, arr in enumerate(sorted_arrays_iters):
        first_elem = next(arr, None)
        if first_elem is not None:
            heapq.heappush(min_heap, (first_elem, i))

    result = []
    while min_heap:
        smallest, i = heapq.heappop(min_heap)
        result.append(smallest)
        next_elem = next(sorted_arrays_iters[i], None)
        if next_elem is not None:
            heapq.heappush(min_heap, (next_elem, i))
    return result
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))

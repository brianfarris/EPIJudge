from test_framework import generic_test
import bintrees


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    min_so_far = float("inf")
    iters = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)

    while True:
        min_value, min_idx = iters.min_key()
        max_value, _ = iters.max_key()
        min_so_far = min(min_so_far, max_value - min_value)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        if next_min is None:
            return min_so_far
        iters.insert((next_min, min_idx), it)

"""
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    iters = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)
    output = float('inf')
    while True:
        min_value, min_idx = iters.min_key()
        max_value, max_idx = iters.max_key()
        output = min(max_value - min_value, output)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        if next_min is None:
            return output
        iters.insert((next_min, min_idx), it)
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))

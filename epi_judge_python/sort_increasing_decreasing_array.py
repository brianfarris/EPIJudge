from test_framework import generic_test
from sorted_arrays_merge import merge_sorted_arrays


def sort_k_increasing_decreasing_array(A):
    # TODO - you fill in here.
    start = 0
    direction = "inc"
    subarrays = []
    for i in range(1, len(A)):
        if direction == "inc" and A[i] < A[i-1]:
            subarrays.append(A[start:i])
            direction = "dec"
            start = i
        elif direction == "dec" and A[i] > A[i-1]:
            subarrays.append(list(reversed(A[start:i])))
            direction = "inc"
            start = i
    if direction == "inc":
        subarrays.append(A[start:])
    else:
        subarrays.append(list(reversed(A[start:])))


    return merge_sorted_arrays(subarrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))

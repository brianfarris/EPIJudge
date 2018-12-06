from test_framework import generic_test
import random

def partition_pivot(A, left, right, piv_idx):
    A_piv = A[piv_idx]

    new_piv_idx = left
    A[piv_idx], A[right] = A[right], A[piv_idx] # set piv aside
    for i in range(left, right):
        if A[i] < A_piv:
            A[i], A[new_piv_idx] = A[new_piv_idx], A[i]
            new_piv_idx += 1

    A[new_piv_idx], A[right] = A[right], A[new_piv_idx] # bring it back
    return new_piv_idx




def find_kth_largest(k, A):
    left, right = 0, len(A) - 1
    while left <= right:
        piv_idx = random.randint(left, right)
        new_piv_idx = partition_pivot(A, left, right, piv_idx)
        if len(A) - new_piv_idx == k:
            return A[new_piv_idx]
        elif len(A) - new_piv_idx > k:
            left = new_piv_idx + 1
        else:
            right = new_piv_idx - 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))

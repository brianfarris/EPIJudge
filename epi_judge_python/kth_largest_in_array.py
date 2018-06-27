from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    # TODO - you fill in here.
    def partition_pivot(left, right, piv_idx):
        A_piv = A[piv_idx]
        new_piv_idx = left
        A[piv_idx], A[right] = A[right], A[piv_idx]
        for i in range(left, right):
            if A[i] > A_piv:
                A[i], A[new_piv_idx] = A[new_piv_idx], A[i]
                new_piv_idx += 1
        A[right], A[new_piv_idx] = A[new_piv_idx], A[right]
        return new_piv_idx

    left, right = 0, len(A) - 1
    while left <= right:
        piv_idx = random.randint(left, right)
        new_piv_idx = partition_pivot(left, right, piv_idx)
        if new_piv_idx > k - 1:
            right = new_piv_idx - 1
        elif new_piv_idx < k -1:
            left = new_piv_idx + 1
        else:
            return A[new_piv_idx]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))

from test_framework import generic_test


def search_smallest(A):
    l = 0
    r = len(A) - 1
    while r > l:
        mid = (l + r) // 2
        if A[mid] > A[r]:
            l = mid + 1
        else:
            r = mid
    return l

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))

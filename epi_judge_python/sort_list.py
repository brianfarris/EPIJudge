from sorted_lists_merge import merge_two_sorted_lists
from test_framework import generic_test


def stable_sort_list(L):
    if not L or not L.next:
        return L

    slow = L
    fast = L
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next
    pre_slow.next = None
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))

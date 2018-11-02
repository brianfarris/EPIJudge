from test_framework import generic_test
from list_node import ListNode

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # TODO - you fill in here.
    dummy = ListNode(999)
    dummy.next = L
    runner1 = dummy
    runner2 = dummy
    for _ in range(k):
        runner1 = runner1.next
    while runner1.next:
        runner1 = runner1.next
        runner2 = runner2.next

    runner2.next = runner2.next.next

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))

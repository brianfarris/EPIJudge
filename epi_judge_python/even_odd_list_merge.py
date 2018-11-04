from test_framework import generic_test
from list_node import ListNode

def even_odd_merge(L):
    # TODO - you fill in here.
    if not L:
        return L

    even_head = ListNode(0)
    odd_head = ListNode(0)
    even_runner = even_head
    odd_runner = odd_head
    i = 0
    while L:
        if i % 2 == 0:
            even_runner.next = L
            even_runner = even_runner.next
        else:
            odd_runner.next = L
            odd_runner = odd_runner.next
        L = L.next
        i += 1
    even_runner.next = odd_head.next
    odd_runner.next = None

    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))

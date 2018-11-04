from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    # TODO - you fill in here.
    def reverse_list(L):
        prev = None
        while L:
            temp = L.next
            L.next = prev
            prev = L
            L = temp
        return prev

    slow = L
    fast = L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first_iter = L
    second_iter = reverse_list(slow)
    while first_iter and second_iter:
        if first_iter.data != second_iter.data:
            return False
        else:
            first_iter = first_iter.next
            second_iter = second_iter.next
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))

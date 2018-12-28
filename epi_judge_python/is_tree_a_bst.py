from test_framework import generic_test
import collections


def is_binary_tree_bst(tree):
    q = collections.deque([[tree, float('-inf'), float('inf')]])

    while q:
        n = q.popleft()
        if n[0]:
            if not n[1] <= n[0].data <= n[2]:
                return False
            q += [[n[0].left, n[1], n[0].data], [n[0].right, n[0].data, n[2]]]
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))


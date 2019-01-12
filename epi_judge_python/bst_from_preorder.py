from test_framework import generic_test
from bst_node import BstNode


def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    left = [a for i, a in enumerate(preorder_sequence)
            if a < preorder_sequence[0]]
    right = [a for i, a in enumerate(preorder_sequence)
             if a > preorder_sequence[0]]

    return BstNode(preorder_sequence[0],
            rebuild_bst_from_preorder(left),
                   rebuild_bst_from_preorder(right))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))

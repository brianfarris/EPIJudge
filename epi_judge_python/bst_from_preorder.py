from test_framework import generic_test
from bst_node import BstNode


def rebuild_bst_from_preorder(preorder_sequence):
    # TODO - you fill in here.
    if not preorder_sequence:
        return None

    transition = next((i for i, a in enumerate(preorder_sequence)
                        if a > preorder_sequence[0]),
                        len(preorder_sequence))

    return BstNode(preorder_sequence[0],
            rebuild_bst_from_preorder(preorder_sequence[1:transition]),
            rebuild_bst_from_preorder(preorder_sequence[transition:]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))

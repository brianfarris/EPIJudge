import functools
from binary_tree_node import BinaryTreeNode

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder):
    key = preorder.pop(0)
    if key is None:
        return None
    left_subtree = reconstruct_preorder(preorder)
    right_subtree = reconstruct_preorder(preorder)
    return BinaryTreeNode(key, left_subtree, right_subtree)


"""
def reconstruct_preorder(preorder):
    # TODO - you fill in here.
    sub_key = preorder.pop(0)
    if sub_key is None:
        return None
    left_subtree = reconstruct_preorder(preorder)
    right_subtree = reconstruct_preorder(preorder)
    return BinaryTreeNode(sub_key, left_subtree, right_subtree)
"""

@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))

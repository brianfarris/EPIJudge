import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def get_height(node):
        h = 0
        runner = node
        while runner:
            runner = runner.parent
            h += 1
        return h

    h0 = get_height(node0)
    h1 = get_height(node1)

    if h1 > h0:
        for _ in range(h1-h0):
            node1 = node1.parent
    if h1 < h0:
        for _ in range(h0-h1):
            node0 = node0.parent

    while node0 != node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0


"""
def lca(node0, node1):
    # TODO - you fill in here.
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    depth0 = get_depth(node0)
    depth1 = get_depth(node1)

    if depth0 > depth1:
        for _ in range(depth0 - depth1):
            node0 = node0.parent
    else:
        for _ in range(depth1 - depth0):
            node1 = node1.parent

    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0
"""

@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))

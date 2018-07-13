import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    visited = set()
    while node0 or node1:
        if node0:
            if node0 in visited:
                return node0
            visited.add(node0)
            node0 = node0.parent
        if node1:
            if node1 in visited:
                return node1
            visited.add(node1)
            node1 = node1.parent
    raise ValueError("node_0 and node_1 are not in the same tree")

    # TODO - you fill in here.
    return None


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
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))

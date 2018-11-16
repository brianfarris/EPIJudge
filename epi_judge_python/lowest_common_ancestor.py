import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    # TODO - you fill in here.
    def lca_helper(tree):
        if not tree:
            return (0, None)

        left_result = lca_helper(tree.left)
        if left_result[0] == 2:
            return left_result
        
        right_result = lca_helper(tree.right)
        if right_result[0] == 2:
            return right_result
        
        num_target_nodes = left_result[0] + right_result[0] + int(tree == node0) + int(tree == node1)
        return (num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree)[1]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))

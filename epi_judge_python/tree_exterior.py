import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree_root):
    # TODO - you fill in here.
    if tree_root is None:
        return []
    elif not tree_root.left and not tree_root.right:
        return [tree_root]

    left_output = []
    if tree_root.left:
        tree = tree_root.left
        while tree.left or tree.right:
            left_output.append(tree)
            if tree.left:
                tree = tree.left
            else:
                tree = tree.right
        left_output.append(tree)

    def get_leaves(tree):
        if not tree:
            return []
        elif not tree.left and not tree.right:
            return [tree]
        else:
            return get_leaves(tree.left) + get_leaves(tree.right)

    bottom_output = get_leaves(tree_root)

    right_output = []
    if tree_root.right:
        tree = tree_root.right
        while tree.right or tree.left:
            right_output.append(tree)
            if tree.right:
                tree = tree.right
            else:
                tree = tree.left
        right_output.append(tree)

    output = [tree_root]
    output += left_output
    start = 1 if left_output else 0
    end = -1 if right_output else len(bottom_output)
    output += bottom_output[start:end]
    output += right_output[::-1]
    return output


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))

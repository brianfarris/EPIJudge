from test_framework import generic_test, test_utils
from collections import deque


def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    output = []
    def traverse(tree):
        if tree:
            traverse(tree.right)
            if len(output) < k:
                output.append(tree.data)
                traverse(tree.left)

    traverse(tree)
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))

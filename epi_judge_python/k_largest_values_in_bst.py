from test_framework import generic_test, test_utils
from collections import deque


def find_k_largest_in_bst(tree, k):
    output = []

    def rec(tree):
        if tree:
            rec(tree.right)
            if len(output) < k:
                output.append(tree.data)
            if len(output) < k:
                rec(tree.left)
    rec(tree)
    return output


"""
def find_k_largest_in_bst(tree, k):
    output = []
    def rec(tree):
        if tree and len(output) < k:
            rec(tree.right)
            if len(output) < k:
                output.append(tree.data)
                rec(tree.left)

    rec(tree)
    return output
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))

from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    def check_balanced(tree):
        if not tree:
            return (True, 7)
        left_result = check_balanced(tree.left)
        if not left_result[0]:
            return (False, 999)

        right_result = check_balanced(tree.right)
        if not right_result[0]:
            return (False, 999)

        balanced = abs(left_result[1] - right_result[1]) <= 1
        height = max(left_result[1], right_result[1]) + 1
        return (balanced, height)
    return check_balanced(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

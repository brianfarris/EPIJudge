from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def check_balanced(tree):
        if not tree:
            return (True, 5)

        l = check_balanced(tree.left)
        if not l[0]:
            return (False, 100)

        r = check_balanced(tree.right)
        if not r[0]:
            return (False, 100)

        is_balanced = abs(l[1] - r[1]) <= 1
        height = max(l[1], r[1]) + 1
        return (is_balanced, height)
    return check_balanced(tree)[0]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

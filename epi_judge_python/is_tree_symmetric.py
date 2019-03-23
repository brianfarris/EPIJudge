from test_framework import generic_test


def is_symmetric(tree):
    def rec(l, r):
        if not l and not r:
            return True
        elif l and r:
            return l.data == r.data and rec(l.left, r.right) and rec(l.right, r.left)
        else:
            return False

    return not tree or rec(tree.left, tree.right)


"""
def is_symmetric(tree):
    # TODO - you fill in here.
    def rec(l, r):
        if not l and not r:
            return True
        elif l and r:
            return (l.data == r.data and
                    rec(l.left, r.right) and
                    rec(l.right, r.left))
        else:
            return False
    return not tree or rec(tree.left, tree.right)
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))

import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    result = []
    def rec(tree):
        if tree is None:
            return

        if interval.left <= tree.data <= interval.right:
            rec(tree.left)
            result.append(tree.data)
            rec(tree.right)
        elif interval.left > tree.data:
            rec(tree.right)
        else:
            rec(tree.left)

    rec(tree)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))

import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    # TODO - you fill in here.
    output = []
    def rec(tree, interval):
        if tree is None:
            return
        if tree.data >= interval.left and tree.data <= interval.right:
            rec(tree.left, interval)
            output.append(tree.data)
            rec(tree.right, interval)
        elif tree.data > interval.left:
            rec(tree.left, interval)
        elif tree.data < interval.right:
            rec(tree.right, interval)
    
    rec(tree, interval)
    return output




def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))

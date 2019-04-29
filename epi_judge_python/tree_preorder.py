from test_framework import generic_test


def preorder_traversal(tree):
    stack = [tree]
    result = []

    while stack:
        curr = stack.pop()
        if curr:
            result.append(curr.data)
            stack += [curr.right, curr.left]
    return result


"""
def preorder_traversal(tree):
    # TODO - you fill in here.
    stack = [tree]
    result = []
    while stack:
        temp = stack.pop()
        if temp:
            result.append(temp.data)
            stack += [temp.right, temp.left]
    return result
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))

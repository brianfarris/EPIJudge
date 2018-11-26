from test_framework import generic_test


def inorder_traversal(tree):
    # TODO - you fill in here.
    prev = None
    result = []
    while tree:
        if prev is tree.parent:
            if tree.left:
                next_tree = tree.left
            else:
                result.append(tree.data)
                next_tree = tree.right or tree.parent
        elif tree.left is prev:
            result.append(tree.data)
            next_tree = tree.right or tree.parent
        else:
            next_tree = tree.parent

        prev = tree
        tree = next_tree

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))

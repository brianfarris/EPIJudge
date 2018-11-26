from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder, inorder):
    # TODO - you fill in here.
    hash_table = {data: i for i, data in enumerate(inorder)}
    def binary_tree_from_preorder_inorder_helper(p_start, p_end, i_start, i_end):
        if p_end <= p_start or i_end <= i_start:
            return None
        
        i_root_idx = hash_table[preorder[p_start]]
        left_size = i_root_idx - i_start
        
        root = BinaryTreeNode(preorder[p_start])
        root.left = binary_tree_from_preorder_inorder_helper(p_start + 1, p_start + 1 + left_size, i_start, i_root_idx)
        root.right = binary_tree_from_preorder_inorder_helper(p_start + 1 + left_size, p_end, i_root_idx + 1, i_end)
        return root
    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))

from test_framework import generic_test
import collections


def binary_tree_depth_order(tree):
    q = collections.deque([tree])
    result = []
    while q:
        q_next = collections.deque([])
        this_level = []
        while q:
            current = q.popleft()
            if current:
                this_level.append(current.data)
                q_next += [current.left, current.right]
        if this_level:
            result.append(this_level)
        q = q_next
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))

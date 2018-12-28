from test_framework import generic_test
import bintrees
import math


class AB:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt(2.)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def generate_first_k_a_b_sqrt2(k):
    tree = bintrees.RBTree()
    tree.insert(AB(0, 0), None)
    result = []
    while len(result) < k:
        cand = tree.pop_min()[0]
        result.append(cand.val)
        tree.insert(AB(cand.a + 1, cand.b), None)
        tree.insert(AB(cand.a, cand.b + 1), None)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))

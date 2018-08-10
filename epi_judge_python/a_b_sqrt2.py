from test_framework import generic_test
import bintrees
import math

class AB:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt(2.)
    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

def generate_first_k_a_b_sqrt2(k):
    # TODO - you fill in here.
    tree = bintrees.RBTree()
    tree.insert(AB(0,0), None)
    result = []
    while len(result) < k:
        next_smallest = tree.pop_min()[0]
        result.append(next_smallest.val)
        tree.insert(AB(next_smallest.a + 1, next_smallest.b), None)
        tree.insert(AB(next_smallest.a, next_smallest.b + 1), None) 

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))

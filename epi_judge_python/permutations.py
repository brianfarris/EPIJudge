from test_framework import generic_test, test_utils


def permutations(A):
    # TODO - you fill in here.
    def rec(A):
        if len(A) <= 1:
            return [A]
        output = []
        for i in range(len(A)):
            output += [[A[i]] + x for x in rec(A[:i] + A[i+1:])]
        return output
    return rec(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

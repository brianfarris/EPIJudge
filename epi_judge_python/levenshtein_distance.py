from test_framework import generic_test

def levenshtein_distance(A, B):
    cache = {}

    # TODO - you fill in here.
    def rec(Ai, Bi):
        if Ai < 0:
            return Bi + 1
        elif Bi < 0:
            return Ai + 1
        if (Ai, Bi) not in cache:
            if A[Ai] == B[Bi]:
                cache[(Ai, Bi)] = rec(Ai - 1, Bi - 1)
            else:
                temp1 = rec(Ai - 1, Bi)
                temp2 = rec(Ai, Bi - 1)
                temp3 = rec(Ai - 1, Bi - 1)
                temp = min(temp1, temp2, temp3) +  1
                cache[(Ai, Bi)] = temp
        return cache[(Ai, Bi)]
    return rec(len(A)-1, len(B)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))

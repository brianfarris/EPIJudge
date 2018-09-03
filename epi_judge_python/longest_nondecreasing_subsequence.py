from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    # TODO - you fill in here.
    longest = [1]
    for a in A[1:]:
        candidates = [longest[i] for i in range(len(longest)) if A[i] <= a]
        l = max(candidates) + 1 if candidates else 1
        longest.append(l)
    return max(longest)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))

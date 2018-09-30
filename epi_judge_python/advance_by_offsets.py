from test_framework import generic_test


def can_reach_end(A):
    # TODO - you fill in here.
    furthest_so_far = 0
    i = 0
    while i <= furthest_so_far and furthest_so_far < len(A) - 1:
        furthest_so_far = max(furthest_so_far, A[i] + i)
        i += 1
    return furthest_so_far >= len(A) - 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))

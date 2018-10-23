from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    spiral_ordering = []
    def func(offset):
        if offset == len(square_matrix) - offset - 1:
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset: -1 - offset])
        spiral_ordering.extend(list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset:offset:-1])
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    for offset in range((len(square_matrix) + 1) // 2):
        func(offset)

    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))

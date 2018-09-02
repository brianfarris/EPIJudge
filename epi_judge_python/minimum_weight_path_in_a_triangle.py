from test_framework import generic_test


def minimum_path_weight(triangle):
    # TODO - you fill in here.
    cache = {}
    def rec_top_down(i,j):
        if i == len(triangle) - 1:
            return triangle[i][j]
        if (i, j) not in cache:
            cache[(i, j)] = min(rec_top_down(i+1, j), rec_top_down(i+1, j+1)) + triangle[i][j]
        return cache[(i, j)]
    if not triangle:
        return 0

    min_to_row = [0]
    for row in triangle:
        min_to_row = [min(min_to_row[max(i-1, 0)], min_to_row[min(i, len(min_to_row)-1)]) + row[i] for i in range(len(row))]
    return min(min_to_row)

    # return rec_top_down(0, 0)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))

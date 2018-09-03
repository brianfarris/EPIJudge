from test_framework import generic_test


def calculate_largest_rectangle(heights):
    # TODO - you fill in here.
    pillar_indices = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1
            max_area = max(max_area, height * width)
        pillar_indices.append(i)
    return max_area

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))

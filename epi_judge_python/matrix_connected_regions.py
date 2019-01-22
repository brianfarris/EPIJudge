from test_framework import generic_test
from collections import deque


def flip_color(x, y, image):
    color = image[x][y]
    q = deque()
    q.append((x, y))
    image[x][y] = 1 - image[x][y]
    while q:
        curr = q.popleft()
        for coord in ((curr[0] + 1, curr[1]),
                      (curr[0] - 1, curr[1]),
                      (curr[0], curr[1] + 1),
                      (curr[0], curr[1] - 1)):
            if (0 <= coord[0] < len(image) and
                    0 <= coord[1] < len(image[0]) and
                    image[coord[0]][coord[1]] == color):
                image[coord[0]][coord[1]] = 1 - image[coord[0]][coord[1]]
                q.append(coord)


"""
def flip_color(x, y, image):
    # TODO - you fill in here.
    def rec(i, j, color):
        if (i < 0 or
            i > len(image) - 1 or
            j < 0 or
            j > len(image[0]) - 1 or
            image[i][j] == color):
            return

        image[i][j] = color
        rec(i + 1, j, color)
        rec(i - 1, j, color)
        rec(i, j + 1, color)
        rec(i, j - 1, color)

    rec(x, y, 1 - image[x][y])
    return image
"""

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))

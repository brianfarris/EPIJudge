from test_framework import generic_test


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


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))

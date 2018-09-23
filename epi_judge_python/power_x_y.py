from test_framework import generic_test


def power(x, y):
    # TODO - you fill in here.
    result = 1
    power = y
    if y < 0:
        power = - power
        x = 1. / x
    while power:
        if power % 2 == 1:
            result *= x
        x = x * x
        power //= 2

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))

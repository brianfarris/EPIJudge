from test_framework import generic_test


mask_size = 16
mask = (1 << mask_size) - 1



def fill_cache():
    cache = {}
    for y in range(1 << mask_size):

        result = 0
        x = y
        while x:
            result ^= 1
            x &= x - 1
        cache[y] = result
    return cache

cache = fill_cache()


def parity(x):
    # TODO - you fill in here.
    return (cache[(x >> (3 * mask_size)) & mask] ^
            cache[(x >> (2 * mask_size)) & mask] ^
            cache[(x >> (1 * mask_size)) & mask] ^
            cache[(x >> (0 * mask_size)) & mask])


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))

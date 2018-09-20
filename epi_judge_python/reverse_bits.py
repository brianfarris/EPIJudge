from test_framework import generic_test
from swap_bits import swap_bits

mask_size = 16
mask = (1 << mask_size) - 1

cache = {}
for num in range(1 << mask_size):
    num_rev = num
    for i in range(8):
        num_rev = swap_bits(num_rev, 16-i - 1, i)
    cache[num] = num_rev

def reverse_bits(x):
    # TODO - you fill in here.
    return (cache[x & mask] << (3 * mask_size) |
    cache[(x >> mask_size) & mask] << (2 * mask_size) |
    cache[(x >> (2 * mask_size)) & mask] << mask_size |
    cache[(x >> (3 * mask_size)) & mask])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))

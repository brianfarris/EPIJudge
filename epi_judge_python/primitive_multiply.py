from test_framework import generic_test


def multiply(x, y):
    # TODO - you fill in here.
    def add(a, b):
        running_sum = 0
        carryin = 0
        k = 1
        temp_a = a
        temp_b = b
        while temp_a or temp_b:
            ak = a & k
            bk = b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin = carryout << 1
            k <<= 1
            temp_a >>= 1
            temp_b >>= 1

        return running_sum | carryin

    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))

from test_framework import generic_test


cache = {}
def fibonacci(n):
    # TODO - you fill in here.
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n not in cache:
        cache[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return cache[n]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))

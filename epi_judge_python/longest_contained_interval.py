from test_framework import generic_test


def longest_contained_range(A):
    # TODO - you fill in here.
    storage = set(A)
    res = 0
    while storage:
        e = storage.pop()

        lower_bound = e - 1
        while lower_bound in storage:
            storage.remove(lower_bound)
            lower_bound -= 1

        upper_bound = e + 1
        while upper_bound in storage:
            storage.remove(upper_bound)
            upper_bound += 1

        res = max(res, upper_bound - lower_bound - 1)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))

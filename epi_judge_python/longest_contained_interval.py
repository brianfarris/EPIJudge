from test_framework import generic_test


def longest_contained_range(A):
    storage = set(A)

    output = 0
    while storage:
        num = storage.pop()
        length = 1
        lower = num - 1
        while lower in storage:
            storage.remove(lower)
            length += 1
            lower -= 1
        upper = num + 1
        while upper in storage:
            storage.remove(upper)
            length += 1
            upper += 1

        output = max(output, length)
    return output

        

"""
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
    """


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))

from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    # TODO - you fill in here.
    cache = {}
    def rec(top):
        if top == 0:
            return 1
        if top < 0:
            return 0
        if top not in cache:
            answer = 0
            for step in range(1, maximum_step + 1):
                answer += rec(top - step)
            cache[top] = answer
        return cache[top]
    return rec(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))

import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    # TODO - you fill in here.
    cache = {}
    def rec(i, cap):
        if cap <= 0 or i < 0:
            return 0
        if (i, cap) not in cache:
            without_i = rec(i - 1, cap)
            with_i = rec(i - 1, cap - items[i].weight) + items[i].value
            if items[i].weight > cap:
                cache[(i, cap)] = without_i
            else:
                cache[(i, cap)] = max(without_i, with_i)

        return cache[(i, cap)]



    return rec(len(items)-1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))

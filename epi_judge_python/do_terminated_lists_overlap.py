import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.
    def get_length(l):
        runner = l
        length = 0
        while runner:
            runner = runner.next
            length += 1
        return length

    length0 = get_length(l0)
    length1 = get_length(l1)

    runner0 = l0
    runner1 = l1
    for _ in range(abs(length1 - length0)):
        if length1 > length0:
            runner1 = runner1.next
        else:
            runner0 = runner0.next

    while runner0 and runner1 and runner1 is not runner0:
        runner0 = runner0.next
        runner1 = runner1.next

    if runner0 is runner1:
        return runner0
    else:
        return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))

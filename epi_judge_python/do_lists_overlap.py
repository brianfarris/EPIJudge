import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from is_list_cyclic import has_cycle
from do_terminated_lists_overlap import overlapping_no_cycle_lists

def overlapping_lists(l0, l1):
    # TODO - you fill in here.
    root0 = has_cycle(l0)
    root1 = has_cycle(l1)

    if not root0 and not root1:
        return overlapping_no_cycle_lists(l0, l1)
    elif (root0 and not root1) or (root1 and not root0):
        return None

    runner = root1
    while True:
        runner = runner.next
        if runner is root0 or runner is root1:
            break

    if runner is not root0:
        return None

    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis

    stem_length0 = distance(l0, root0)
    stem_length1 = distance(l1, root1)

    # make sure that root0 comes first
    if stem_length0 > stem_length1:
        l0, l1 = l1, l0
        root0, root1 = root1, root0

    for _ in range(abs(stem_length0 - stem_length1)):
        l1 = l1.next

    while l0 is not l1 and l0 is not root0 and l1 is not root1:
        l0 = l0.next
        l1 = l1.next

    if l0 is l1:
        return l0
    else:
        return root1

@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))

import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    # TODO - you fill in here.
    endpoints = [(a.start, 0) for a in A] + [(a.finish, 1) for a in A]
    endpoints.sort()
    max_num = num = 0
    for e in endpoints:
        if e[1] == 0:
            num += 1
            max_num = max(max_num, num)
        else:
            num -= 1
    return max_num


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))

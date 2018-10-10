import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

def find_max_simultaneous_events(A):
    points = [(a.start, 0) for a in A] + [(a.finish, 1) for a in A]
    points.sort()
    max_ev = 0
    ev = 0
    for p in points:
        if p[1] == 0:
            ev += 1
        else:
            ev -= 1
        max_ev = max(ev, max_ev)
    return max_ev


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

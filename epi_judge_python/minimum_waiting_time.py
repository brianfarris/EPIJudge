from test_framework import generic_test
from itertools import accumulate


def minimum_total_waiting_time(service_times):
    service_times.sort()
    return sum(accumulate([0] + service_times[:-1]))

"""
def minimum_total_waiting_time(service_times):
    # TODO - you fill in here.
    service_times.sort()
    return sum(accumulate([0] + service_times[:-1]))
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))

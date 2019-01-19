import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    task_durations.sort()
    output = []
    while task_durations:
        pair = (task_durations.pop(0), task_durations.pop())
        output.append(pair)
    return output


"""
def optimum_task_assignment(task_durations):
    # TODO - you fill in here.
    task_durations.sort()
    output = []
    while task_durations:
        pair = (task_durations.pop(0), task_durations.pop())
        output.append(pair)
    return output
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))

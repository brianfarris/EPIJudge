import collections
import functools
import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people):
    ages = [person.age for person in people]
    age_to_count = collections.Counter(ages)
    offsets = [0] + list(itertools.accumulate(age_to_count.values()))[:-1]
    age_to_offset = {age: offset for age, offset in zip(age_to_count.keys(), offsets)}

    while age_to_offset:
        old_age = next(iter(age_to_offset))
        old_offset = age_to_offset[old_age]
        new_age = people[old_offset].age
        new_offset = age_to_offset[new_age]
        people[old_offset], people[new_offset] = people[new_offset], people[old_offset]

        age_to_count[new_age] -= 1
        if age_to_count[new_age]:
            age_to_offset[new_age] = new_offset + 1
        else:
            del age_to_offset[new_age]


"""
def group_by_age(people):
    age_to_count = collections.Counter([person.age for person in people])
    age_to_offset = {}
    offset = 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[to_age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] += 1
        else:
            del age_to_offset[to_age]
    return people
"""

@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))

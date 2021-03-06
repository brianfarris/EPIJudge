import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


def find_ample_city(gallons, distances):
    tank = 0
    min_tank = float("inf")
    min_tank_index = 0
    for i in range(len(gallons)):
        tank += gallons[i]
        tank -= distances[i] / MPG
        if tank < min_tank:
            min_tank = tank
            min_tank_index = i

    return min_tank_index + 1


"""
# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    # TODO - you fill in here
    tank = 0
    min_tank = 0
    min_tank_index = 0
    for i in range(len(gallons)):
        tank += gallons[i]
        tank -= distances[i] / MPG
        if tank <= min_tank:
            min_tank = tank
            min_tank_index = i
    return min_tank_index + 1
    """

@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))

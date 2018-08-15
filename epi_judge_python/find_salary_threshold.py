from test_framework import generic_test


def find_salary_cap(target_payroll, current_salaries):
    # TODO - you fill in here.
    current_salaries.sort()
    running_sum = 0
    for i, salary in enumerate(current_salaries):
        adjusted_sum = salary * (len(current_salaries) - i)
        if running_sum + adjusted_sum >= target_payroll:
            return (target_payroll - running_sum) / (len(current_salaries) - i)
        running_sum += salary
    return -1.


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))

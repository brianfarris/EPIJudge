from test_framework import generic_test


def find_salary_cap(target_payroll, current_salaries):
    current_salaries.sort()

    n = len(current_salaries)
    salary_sum = 0
    for i, salary in enumerate(current_salaries):

        c = (target_payroll - salary_sum) / (n - i)
        if c <= salary:
            return c
        salary_sum += salary

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))

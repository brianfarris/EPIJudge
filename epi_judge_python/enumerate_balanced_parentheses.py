from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    # TODO - you fill in here.
    if num_pairs == 0:
        return ['']
    elif num_pairs == 1:
        return ['()']
    else:
        return ['(' + x + ')' + y for i in range(num_pairs)
                for x in generate_balanced_parentheses(i)
                for y in generate_balanced_parentheses(num_pairs - 1 - i)
                ] 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))

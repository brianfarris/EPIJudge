from test_framework import generic_test, test_utils


def generate_power_set(S):
    # TODO - you fill in here.
    if len(S) == 0:
        return [S]
    else:
        output = generate_power_set(S[1:])
        for subset in generate_power_set(S[1:]):
            output.append([S[0]] + subset)
        return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))

from test_framework import generic_test, test_utils


def generate_power_set(S):
    
    power_set = []
    def directed_power_set(n, x):
        if n == len(S):
            power_set.append(x)
            return

        directed_power_set(n + 1, x)
        directed_power_set(n + 1, x + [S[n]])
    
    directed_power_set(0, [])
    return power_set
        
"""
def generate_power_set(S):
    # TODO - you fill in here.
    if len(S) == 0:
        return [S]
    else:
        output = generate_power_set(S[1:])
        for subset in generate_power_set(S[1:]):
            output.append([S[0]] + subset)
        return output
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))

from test_framework import generic_test


def maximum_revenue(coins):
    cache = {}
    def rec(a, b):
        if a > b:
            return 0
        if (a, b) not in cache:
            cache[(a, b)] = max(coins[a] + sum(coins[a+1: b+1]) - rec(a+1, b),
                                coins[b] + sum(coins[a: b]) - rec(a, b-1))
        return cache[(a, b)]
    return rec(0, len(coins) - 1)

"""
def maximum_revenue(coins):
    # TODO - you fill in here.
    cache = {}
    def rec(a, b):
        if a > b:
            return 0
        if (a, b) not in cache:
            cache[(a, b)] = max(coins[a] + sum(coins[a+1:b+1]) - rec(a+1, b),
                                coins[b] + sum(coins[a:b]) - rec(a, b-1))
        return cache[(a, b)]
    return rec(0, len(coins)-1)
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))

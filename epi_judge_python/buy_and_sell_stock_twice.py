from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    # TODO - you fill in here.
    max_profit = 0.0
    min_price = float('inf')
    first_profits = []
    for i, price in enumerate(prices):
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)
        first_profits.append(max_profit)

    max_profit = 0.0
    max_price = float('-inf')
    last_profits_rev = []
    for i, price in reversed(list(enumerate(prices))):
        max_price = max(price, max_price)
        max_profit = max(max_profit, max_price - price)
        last_profits_rev.append(max_profit)


    profit = [last_profits_rev[len(prices)-1]]
    for i in range(1, len(prices) - 1):
        profit.append(last_profits_rev[len(prices) - 1 - i] + first_profits[i-1])

    return max(profit)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))

from test_framework import generic_test


def evaluate(expression):
    # TODO - you fill in here.
    OPERATORS = {
            "+": lambda y, x: x + y,
            "-": lambda y, x: x - y,
            "*": lambda y, x: x * y,
            "/": lambda y, x: int(x / y)
            }
    stack = []
    for token in expression.split(","):
        if token in OPERATORS:
            result = OPERATORS[token](stack.pop(), stack.pop())
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))

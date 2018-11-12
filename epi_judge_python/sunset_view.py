from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    # TODO - you fill in here.
    stack = []
    for i, height in enumerate(sequence):
        while stack and height >= stack[-1][1]:
            stack.pop()
        stack.append((i, height))
    return [x[0] for x in reversed(stack)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))

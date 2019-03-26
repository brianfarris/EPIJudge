import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

HighwaySection = collections.namedtuple('HighwaySection',
                                        ('x', 'y', 'distance'))


def find_best_proposals(H, P, n):
    # TODO - you fill in here.
    graph = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for h in H:
        graph[h.x][h.y] = h.distance
        graph[h.y][h.x] = h.distance

    for k in range(n):
        for j in range(n):
            for i in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    best_saving = float("-inf")
    best_p = HighwaySection(-1, -1, 0.0)
    for p in P:
        p_save = 0.0
        for a in range(n):
            for b in range(n):
                p_save += max(graph[a][b] -
                        graph[a][p.x] -
                        p.distance -
                        graph[p.y][b], 0.0
                        )
        if p_save > best_saving:
            best_saving = p_save
            best_p = p
    return best_p


@enable_executor_hook
def find_best_proposals_wrapper(executor, H, P, n):
    H = [HighwaySection(*x) for x in H]
    P = [HighwaySection(*x) for x in P]

    return executor.run(functools.partial(find_best_proposals, H, P, n))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "road_network.py",
            'road_network.tsv',
            find_best_proposals_wrapper,
            res_printer=res_printer))

from test_framework import generic_test
import math


def is_arbitrage_exist(graph):
    # TODO - you fill in here.
    neg_log_graph = [[-math.log(edge) for edge in edge_list] for edge_list in graph]
    dist = [float("inf") for _ in range(len(graph))]
    dist[0] = 0.0
    for _ in range(len(graph)):
        for i, row in enumerate(neg_log_graph):
            for j, g in enumerate(row):
                dist[j] = min(dist[j], dist[i] + g)


    for i, row in enumerate(neg_log_graph):
        for j, g in enumerate(row):
            if dist[j] > dist[i] + g:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("arbitrage.py", "arbitrage.tsv",
                                       is_arbitrage_exist))

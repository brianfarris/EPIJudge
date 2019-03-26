import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self):
        self.edges = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0


def find_largest_number_teams(graph):
    top_order = []

    def dfs(vertex):
        if vertex.max_distance == 0:
            vertex.max_distance = 1
            for edge in vertex.edges:
                dfs(edge)
            top_order.append(vertex)

    for vertex in graph:
        dfs(vertex)

    max_distance = 0
    while top_order:
        u = top_order.pop()
        max_distance = max(max_distance, u.max_distance)
        for edge in u.edges:
            edge.max_distance = max(edge.max_distance, u.max_distance + 1)
    return max_distance

"""
def find_largest_number_teams(graph):
    sorted_list = []

    def dfs(parent):
        parent.max_distance = 1
        for child in parent.edges:
            if not child.max_distance:
                dfs(child)
        sorted_list.append(parent)

    for v in graph:
        if not v.max_distance:
            dfs(v)

    max_distance = 0
    while sorted_list:
        u = sorted_list.pop()
        max_distance = max(max_distance, u.max_distance)
        for v in u.edges:
            v.max_distance = max(v.max_distance, u.max_distance + 1)
    return max_distance
"""


"""
def find_largest_number_teams(graph):
    # TODO - you fill in here.
    sorted_list = []

    def dfs(parent):
        parent.max_distance = 1
        for child in parent.edges:
            if not child.max_distance:
                dfs(child)
        sorted_list.append(parent)

    for g in graph:
        if not g.max_distance:
            dfs(g)

    max_distance = 0
    while sorted_list:
        u = sorted_list.pop()
        max_distance = max(max_distance, u.max_distance)
        for v in u.edges:
            v.max_distance = max(v.max_distance, u.max_distance + 1)
    return max_distance
"""


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(find_largest_number_teams, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_teams_in_photograph.py",
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))

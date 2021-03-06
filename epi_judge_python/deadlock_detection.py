import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self):
        self.edges = []
        self.color = 'white'


def is_deadlocked(graph):
    def dfs(vertex):
        for edge in vertex.edges:
            if edge.color in ("grey", "black"):
                return True
            else:
                edge.color = "grey"
                dfs(edge)
        vertex.color = "black"
        return False

    for vertex in graph:
        if vertex.color != "black":
            vertex.color = "grey"
            if dfs(vertex):
                return True
    return False


"""
def is_deadlocked(graph):
    def rec(vert):
        if vert.color == "grey":
            return True
        vert.color = "grey"
        any_dead = any(rec(dep) for dep in vert.edges if dep.color != "black")
        vert.color = "black"
        return any_dead

    return any(rec(vert) for vert in graph if vert.color == "white")
"""
"""
def is_deadlocked(graph):
    # TODO - you fill in here.
    def rec(vert):
        if vert.color == 'gray':
            return True

        vert.color = 'gray'
        if any([v.color != 'black' and rec(v) for v in vert.edges]):
            return True
        vert.color = 'black'
        return False

    return any([vert.color == 'white' and rec(vert) for vert in graph])
"""

@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))

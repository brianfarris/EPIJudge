import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import deque


class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []


def is_any_placement_feasible(graph):
    def bfs(v):
        v.d = 0
        q = deque()
        q.append(v)
        while q:
            curr = q.popleft()
            for t in curr.edges:
                if t.d == -1:
                    t.d = curr.d + 1
                    q.append(t)
                elif t.d == curr.d:
                    return False
        return True
    return all(bfs(v) for v in graph if v.d == -1)


"""
def is_any_placement_feasible(graph):
    # TODO - you fill in here.
    def bfs(v):
        v.d = 0
        q = deque([v])
        while q:
            this = q.pop()
            for new_v in this.edges:
                if new_v.d == -1:
                    new_v.d = this.d + 1
                    q.appendleft(new_v)
                elif new_v.d == this.d:
                        return  False
        return True

    return all([bfs(v) for v in graph if v.d == -1])
"""


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))

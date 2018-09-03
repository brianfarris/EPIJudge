import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    # TODO - you fill in here.
    path = []
    def is_reachable_dfs(curr):
        if (curr.x < 0 or
            curr.x > len(maze)-1 or
            curr.y < 0 or
            curr.y > len(maze[0])-1
            or maze[curr.x][curr.y] == BLACK
            ):
            return False

        path.append(curr)
        maze[curr.x][curr.y] = BLACK

        if curr == e:
            return True

        if any([is_reachable_dfs(Coordinate(curr.x + 1, curr.y + 0)),
                is_reachable_dfs(Coordinate(curr.x - 1, curr.y + 0)),
                is_reachable_dfs(Coordinate(curr.x + 0, curr.y + 1)),
                is_reachable_dfs(Coordinate(curr.x + 0, curr.y - 1))]
               ):
            return True
        del path[-1]
        return False

    if not is_reachable_dfs(s):
        return []
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))

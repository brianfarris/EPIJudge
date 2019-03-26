from test_framework import generic_test
from collections import deque
import string


def transform_string(D, s, t):
    def replace(s, i, letter):
        return s[:i] + letter + s[i+1:]

    D.remove(s)

    q = [(s, 0)]
    while q:
        curr, dist = q.pop(0)
        if curr == t:
            return dist
        for letter in string.ascii_lowercase:
            for i in range(len(s)):
                cand = replace(curr, i, letter)
                if cand in D:
                    D.remove(cand)
                    q.append((cand, dist + 1))
    return -1


"""
def transform_string(D, s, t):
    q = deque()
    q.append((s, 0))
    D.remove(s)
    while q:
        vert, vert_dist = q.popleft()
        if vert == t:
            return vert_dist

        for i in range(len(vert)):
            for char in string.ascii_lowercase:
                candidate = vert[:i] + char + vert[i+1:]
                if candidate in D:
                    q.append((candidate, vert_dist + 1))
                    D.remove(candidate)
    return -1
"""


"""
# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    # TODO - you fill in here.
    q = deque([(s, 0)])
    D.remove(s)
    while q:
        vert, vert_dist = q.pop()
        if vert == t:
            return vert_dist

        for i in range(len(vert)):
            for char in string.ascii_lowercase:
                candidate = vert[:i] + char + vert[i+1:]
                if candidate in D:
                    q.appendleft((candidate, vert_dist + 1))
                    D.remove(candidate)
    return -1
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))

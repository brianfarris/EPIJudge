from test_framework import generic_test
from collections import deque


def fill_surrounded_regions(board):
    n = len(board)
    m = len(board[0])
    q = deque([(i, 0) for i in range(n)] +
            [(i, m - 1) for i in range(n)] +
            [(0, j) for j in range(m)] +
            [(n - 1, j) for j in range(m)])
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y] == "W":
            board[x][y] = 'T'
            q.append((x + 1, y))
            q.append((x - 1, y))
            q.append((x, y + 1))
            q.append((x, y - 1))

    board[:] = [['B' if c != "T" else 'W' for c in row] for row in board]


"""
def fill_surrounded_regions(board):
    # TODO - you fill in here.
    q = deque([(i,j) for i in range(len(board)) for j in range(len(board[0])) if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1])
    while q:
        x, y = q.pop()
        if x >= 0 and x <= len(board) - 1 and y >= 0 and y <= len(board[0]) - 1 and board[x][y] == 'W':
            board[x][y] = 'temp'
            q.appendleft((x - 1, y))
            q.appendleft((x + 1, y))
            q.appendleft((x, y - 1))
            q.appendleft((x, y + 1))

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'W':
                board[i][j] = 'B'
            elif board[i][j] == 'temp':
                board[i][j] = 'W'
    return board
"""


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))

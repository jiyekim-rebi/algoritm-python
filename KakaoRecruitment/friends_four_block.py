# B6: 프렌즈4블록
from typing import List


# 1. 일치여부 찾기
# 2. 일치한 위치 삭제
# 3. 블록 아래로 떨구기
def solution(m: int, n: int, board: List[str]) -> int:
    board = [list(x) for x in board]

    matched = True
    while matched:
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == \
                        board[i][j + 1] == \
                        board[i + 1][j + 1] == \
                        board[i + 1][j] != '#':
                    matched.append([i, j])

        for i, j in matched:
            board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = board[i + 1][j] = '#'

        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'

    return sum(x.count('#') for x in board)

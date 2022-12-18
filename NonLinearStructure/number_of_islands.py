# 섬의 개수
# https://leetcode.com/problems/number-of-islands
from typing import List

class Solution:
    # DFS로 그래프 탐색
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더이상 땅이 아니면 종료함
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = '0'

            # 동서남북 탐색
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


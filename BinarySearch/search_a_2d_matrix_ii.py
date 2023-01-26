# 2D 행렬 검색 ii
# https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    # 1. 첫 행의 맨 뒤에서 부터 탐색
    # 열 기준 이진 검색 수행하고, 찾아낸 값 기준으로 해당 위치의 각 행 기준으로 다시 이진 검색 수행
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1

        return False

    # 2. 파이썬다운 방식
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)
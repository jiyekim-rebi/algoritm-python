# 피보나치 수열
# https://leetcode.com/problems/fibonacci-number/
import collections

import np as np


class Solution:
    # 재귀 구조 브루트 포스
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

    # 두 변수만 이용해서 공간절약
    def fib(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x

# 메모이제이션
class Memoization:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]


# 타뷸레이션
class Tabulation:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        self.dp[0] = 1
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[N]

# 행렬
# 넘파일 모듈 사용
def fib(n):
    M = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])

    return np.matmul(M ** n, vec)[0]
# 1비트의 개수
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # 1. 1개수 계산
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    # 2. 비트 연산
    # 1을 뺀값과 and 연산을 할때마다 비트가 1개씩 빠짐 = 0이 될때까지 반복
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1

        return count
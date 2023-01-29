# 해밍 거리
# https://leetcode.com/problems/hamming-distance

class Solution:
    # 1. xor
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
# 싱글 넘버
# https://leetcode.com/problems/single-number
from typing import List


class Solution:
    # 1. xor 풀이(둘중 하나가 다르면 1)
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


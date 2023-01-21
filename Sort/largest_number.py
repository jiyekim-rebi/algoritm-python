# 가장 큰 수
# https://leetcode.com/problems/largest-number
from typing import List


class Solution:
    # 정렬 기법
    # 자리수 단위로 비교해서 정렬해야 함 (9 -> 30)
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n1) + str(n2)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))
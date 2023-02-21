# 최대 서브 배열
# https://leetcode.com/problems/maximum-subarray/
import sys
from typing import List


class Solution:
    # 메모이제이션
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

    # 카데인 알고리즘
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum
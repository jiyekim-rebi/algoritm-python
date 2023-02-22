# 집 도둑
# https://leetcode.com/problems/house-robber
import collections
from typing import List


class Solution:
    # 재귀 구조 브루트 포스
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])
        return _rob(len(nums) - 1)


    #타뷸레이션
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1, dp[i - 2]] + nums[i])

        return dp.popitem()[1]


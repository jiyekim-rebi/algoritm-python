# 최대 슬라이딩 윈도우
# https://leetcode.com/problems/sliding-window-maximum/
import collections
from typing import List


class Solution:
    # 1. 브루트 포스
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i+k]))

        return r

    # 2. 큐
    # 필요할때만 전체 최대값 계산하고 새로 추가되는 값만 최대인지 확인함
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')

        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')

        return results


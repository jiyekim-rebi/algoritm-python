# 과반수 엘리먼트
# https://leetcode.com/problems/majority-element/
import collections
from typing import List


class Solution:
    # 브루트 포스
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

    # 다이나믹 프로그래밍
    def majorityEleiemtn(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num

    # 분할 정복
    def majorityEleiemtDivide(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityEleiemtDivide(nums[:half])
        b = self.majorityEleiemtDivide(nums[half:])

        return [b, a][nums.count(a) > half]

    # 파이썬다운 방식
    def majorityEleiemtn(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
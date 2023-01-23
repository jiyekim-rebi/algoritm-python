# 회전 정렬된 배열 검색
# https://leetcode.com/problems/search-in-rotated-sorted-array
from typing import List


class Solution:
    # 1. 피벗 기준의 이진검색
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        # 최소값 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 피벗 기준으로 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1
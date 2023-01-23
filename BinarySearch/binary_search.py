# 이진 탐색
# https://leetcode.com/problems/binary-search
import bisect
from typing import List


class Solution:
    # 1. 재귀 풀이
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                # mid = (left + right) // 2
                # 중앙 위치 계산 버그 개선
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1

        return binary_search(0, len(nums) - 1)

    # 2. 반복 풀이
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # mid = (left + right) // 2
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

    # 3. 이진 검색 모듈
    # 파이썬에서 자체적으로 이진검색 모듈 제공: bisect
    # 배열의 크기가 크고, 찾아야 하는 닶이 항상 앞에만 있는게 아니면 해당 모듈 이용하면 cost 개선 가능 :)
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    # 번외: 이진 검색을 사용하지 않는 index 풀이
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
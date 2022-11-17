#세 수의 합
#https://leetcode.com/problems/3sum
from typing import List


class Solution:

    # 브루스 포스 (n^3)
    # 정렬 후 중복된값은 건너뛰게 처리
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뜀
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i]], [nums[j], [nums[k]]])

        return results

    # 투 포인터로 합 계산
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)-2):
            # 중복된 값 건너뜀
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 간격을 좁혀가면서 합 계산
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -=1
                else:
                    # result 처리
                    results.append([nums[i]], [nums[left], [nums[right]]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results

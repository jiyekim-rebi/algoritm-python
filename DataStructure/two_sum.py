# 두 수의 합
# 덧셈해서 타겟을 만들 수 있는 배열의 두 숫자 인덱스 리턴
# https://leetcode.com/problems/two-sum
from typing import List


class Solution:

    # 브루트 포스로 계산
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # in을 이용한 탐색
    # 타겟에서 첫번째 값을 뺀 target - n이 존재하는지 탐색하는 방식
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i+1)]

    # 첫번째 수를 뺀 결과키 조회
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        #키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        #타겟에서 첫번째 수를 뺀 결과를 키로 조회함
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    # 조회 구조 개선
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 투 포인터 이용
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 선 정렬
        nums.sort()

        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
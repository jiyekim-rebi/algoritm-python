# 배열 파티션, part 1
# https://leetcode.com/problems/array-partition-1
from typing import List


class Solution:
    # 정렬: 오름차순으로 정리
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    # 짝수번째값으로 계산
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum

    # 파이썬 다운 방식: 슬라이싱
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

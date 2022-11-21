# 자신을 제외한 배열의 곱
# https://leetcode.com/problems/product-of-array-except-selt/
from typing import List


class Solution:
    # 먼저 왼쪽부터 곱해서 result에 추가
    # 왼쪽 곱셈 결과에 오른쪽 곱셈을 차례대로 진행
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1

        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out

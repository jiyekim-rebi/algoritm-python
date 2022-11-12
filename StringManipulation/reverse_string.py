# 문자열 뒤집기
# https://leetcode.com/problems/reverse-string

from typing import List


class Solution:
    # 투 포인터를 이용한 스왑
    def reverseString_twopointer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # 파이썬 답게 해봅시다
    def reverseString_pythonic(self, s: List[str]) -> None:
        # 슬라이싱으로 적용하면: s[:]=s[::-1]
        s.reverse()

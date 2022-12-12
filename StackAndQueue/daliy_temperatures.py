# 일일 온도
# https://leetcode.com/problems/daliy-temperatures
from typing import List


class Solution:
    def daliyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높으면 정답
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
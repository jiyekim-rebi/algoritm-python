# 괄호를 삽입하는 여러가지 방법
# https://leetcode.com/problems/different-ways-to-add-parentheses
from typing import List


class Solution:
    # 분할 정복을 이용한 다양한 조합
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))

            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                results.extend(compute(left, right, value))

        return results
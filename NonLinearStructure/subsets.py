# 부분 집합
# https://leetcode.com/problems/subsets
from typing import List

class Solution:
    # 트리의 모든 dfs 결과
    # 경로 path를 만들어 나가면서 인덱스를 1씩 증가하는 형태로 깊이 탐색
    def subsets(self, nums: List[int]) -> List[int]:
        result = []

        def dfs(index, path):
            result.append(path)

            # 경로를 만들면서 dfs
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result
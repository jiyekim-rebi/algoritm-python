# 순열
# https://leetcode.com/problems/permutations
import itertools
from typing import List


# n!
class Solution:
    # DFS를 활용한 순열 생성
    def permute(self, nums: List[int]) -> List[int]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드라면 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:] # 참조가 되지 않도록 값 자체를 복사함
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

    # itertools 모듈 사용?
    # itertools 모듈 : 반복자 생성에 최적화된 기능 제공
    # return : 튜플
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))
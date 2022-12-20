# 조합의 합
# https://leetcode.com/problems/combination-sum
from typing import List


class Solution:
    # dfs 중복 조합 그래프 탐색
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # csum: 합을 갱신해나갈 변수
        # index: 순서(자기 자신을 포함)
        # path: 지금까지의 탐색 경로
        def dfs(csum, index, path):
            # 종료조건: csum < 0 또는 csum = 0
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                # 입력값에 0이 포함되어 있을 수 있으므로 첫번째 값부터 탐색 시도
                dfs(csum - candidates[i], 0, path + [candidates[i]])

        dfs(target, 0, [])
        return result
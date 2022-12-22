# 코스 스케쥴
# https://leetcode.com/problems/course-schedule
import collections
from typing import List

class Solution:
    # dfs로 순환 구조 판별
    def canFinish(self, numCourses: int, prerequistites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        # 그래프 구성
        for x, y in prerequistites:
            graph[x].append(y)

        # 중복 저장이 안됨
        traced = set()

        def dfs(i):
            # 순환 구조라면 false
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료하면 순환 노드 삭제해줘야 함
            traced.remove(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

    # 2. 가지치기를 이용한 최적화
    # 한번 방문했던 그래프는 두번 이상 찾지 않게 true 처리
    def canFinish(self, numCourses: int, prerequistites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequistites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            # 이미 방문했던 노드라면
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
                # 탐색 종료 후 순환노드 삭제
                traced.remove(i)
                # 탐색 종료 후 방문노드 추가
                visited.add(i)

                return True

        # RuntimeError: dictionary changed size during iteration
        # 새로운 복사본을 생성함
        for x in list(graph):
            if not dfs(x):
                return False

        return True
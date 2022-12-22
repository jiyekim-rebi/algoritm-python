# 일정 재구성
# https://leetcode.com/problems/reconstruct-itinerary
import collections
from typing import List

class Solution:
    # 1. dfs로 일정 그래프 구성
    # 어휘 순으로 방문해야 하기 때문에 그래프를 구성, 다시 꺼내 정렬하는 방식
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            # 첫번째 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JKF')
        return route[::1]

    # 2. 스택 연산으로 큐 연산 최적화 시도
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 뒤집어서 구성함
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(a):
            # 마지막 값 읽어서 어휘순으로 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::1]

    # 3. 일정 그래프 반복
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        # 꺼낼때 재귀 말고 스택으로 반복처리
        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내서 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]
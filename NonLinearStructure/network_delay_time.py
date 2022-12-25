# 네트워크 딜레이 타임
# https://leetcode.com/problems/network-delay-time
import collections
import heapq
from typing import List


class Solution:
    # 다익스트라 알고리즘
    # 파이썬의 heapq 모듈로 구현
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: 소요시간, 정점
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1